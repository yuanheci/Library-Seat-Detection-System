import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized
import re
import turtle
import mySerial

Empty = 0
Occupancy = 0
Used = 0
# pos = {'Empty seat status': [], 'Occupancy status': [], 'Used seat status': []}
pos = {}  #从左上方点的元组映射到lable
ps = []
avgh = 0
tot = 0
cnt = 0
mn, mx = 1000000, 0
#开一个二维数组存row
posid = []
rid = 0   #当前行id

def detect(save_img=False):
    source, weights, view_img, save_txt, imgsz = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
    save_img = not opt.nosave and not source.endswith('.txt')  # save inference images
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://', 'https://'))

    # Directories
    save_dir = Path(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok))  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Initialize
    set_logging()
    device = select_device(opt.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    t0 = time.time()
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t2 = time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # img.jpg
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # img.txt
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    global tot, cnt, mn, mx
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh)  # label format
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img or view_img:  # Add bbox to image
                        label = f'{names[int(cls)]} {conf:.2f}'
                        llb = f'{names[int(cls)]}'
                        cp = plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=6)
                        print("llb = ", llb)
                        print("label = ", label)
                        # pos[llb].append((cp[0], cp[1], cp[2], cp[3]))  #以元组形式添加
                        pos[(cp[0], cp[1])] = llb
                        tot += + cp[3] - cp[1]
                        mn = min(mn, cp[3] - cp[1])
                        mx = max(mx, cp[3] - cp[1])
                        cnt += 1
                        ps.append((cp[0], cp[1]))   #根据左上角坐标来排号
            # Print time (inference + NMS)
            print(f'{s}Done. ({t2 - t1:.3f}s)')

            # Stream results
            if view_img:
                im0 = cv2.resize(im0, (1080, 540), interpolation=cv2.INTER_CUBIC)  # 修改图片和视频检测时输出的窗口大小
                cv2.imshow(str(p), im0)
                cv2.waitKey(1)  # 1 millisecond
                match1 = re.search(r'\d+(?= Empty)', s)
                match2 = re.search(r'\d+(?= Occupancy)', s)
                match3 = re.search(r'\d+(?= Used)', s)

                if (re.search(r'\d+(?= Empty)', s) != None):
                    global Empty
                    Empty = int(match1.group())
                if (re.search(r'\d+(?= Occupancy)', s) != None):
                    global Occupancy
                    Occupancy = int(match2.group())
                if (re.search(r'\d+(?= Used)', s) != None):
                    global Used
                    Used = int(match3.group())

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'image':
                    cv2.imwrite(save_path, im0)
                else:  # 'video' or 'stream'
                    if vid_path != save_path:  # new video
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release()  # release previous video writer
                        if vid_cap:  # video
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else:  # stream
                            fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path += '.mp4'
                        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                    vid_writer.write(im0)

    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
        print(f"Results saved to {save_dir}{s}")

    print(f'Done. ({time.time() - t0:.3f}s)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='weights/best.pt', help='model.pt path(s)')
    # parser.add_argument('--source', type=str, default='VOCdevkit/VOC2007/JPEGImages/64.jpg', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--source', type=str, default='VOCdevkit/VOC2007/test/116.jpg', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results',default=True)
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    opt = parser.parse_args()
    print(opt)
    check_requirements(exclude=('pycocotools', 'thop'))

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()

# print("打印坐标信息")
# for k, v in pos.items():
#     print("k = ", k, "v = ", v)

avgh = (tot - mn - mx) / (cnt - 2) / 3
# avgh = tot / cnt / 2
# avgh = 200
print("avgh = %d" % avgh)

lasty = 0
print(ps)
ps.sort(key = lambda x : x[1])
print(ps)
tmp = []
for x in ps:
    print("(%d, %d) = %s" % (x[0], x[1], pos[(x[0], x[1])]))
    if x[1] - avgh > lasty:
        if len(tmp) > 0:
            posid.append(tmp)
            tmp = []
    tmp.append(x)
    lasty = x[1]
posid.append(tmp)

print("开始验证！")
print("pid len = %d" % len(posid))
#行内排序
for t in posid:
    t.sort(key = lambda x : x[0])

cmx = 0
for t in posid:
    cmx = max(cmx, len(t))
    for x in t:
        print(x, end=' ')
    print("")
    # print()

# 隐藏画笔
turtle.hideturtle()
# 绘制所有椅子的状态
def draw_chairs(num_occupied, num_in_use, num_vacant):
    turtle.penup()
    turtle.setpos(-300, 150)
    turtle.pendown()
    turtle.write("绿色: 空闲   黄色: 占座   红色: 正在使用", font=("Arial", 16, "bold"))

    turtle.penup()
    turtle.setpos(-300, 0)
    turtle.pendown()
    turtle.write("图书馆座位状态", font=("Arial", 24, "bold"))

    turtle.penup()
    turtle.setpos(-300, -50)
    turtle.pendown()
    turtle.write("空闲：%d 把" % num_vacant, font=("Arial", 16, "normal"))

    turtle.penup()
    turtle.setpos(-300, -100)
    turtle.pendown()
    turtle.write("占座：%d 把" % num_occupied, font=("Arial", 16, "normal"))

    turtle.penup()
    turtle.setpos(-300, -150)
    turtle.pendown()
    turtle.write("正在使用：%d 把" % num_in_use, font=("Arial", 16, "normal"))

    turtle.penup()
    turtle.setpos(-300, 50)
    turtle.pendown()
    turtle.setheading(0)

draw_chairs(Occupancy, Used, Empty)  #基本信息显示

# 设置画笔和填充颜色
turtle.penup()
turtle.speed(0)
turtle.setx(-100)
turtle.sety(-50)
turtle.pendown()

colors = {"Free":"green", "Reserved":"yellow", "Used":"red"}

# 画出空闲椅子
for i in range(Empty):
    turtle.fillcolor(colors["Free"])
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
# 设置画笔和填充颜色
turtle.penup()
turtle.speed(0)
turtle.setx(-100)
turtle.sety(-100)
turtle.pendown()
# 画出占座椅子
for i in range(Occupancy):
    turtle.fillcolor(colors["Reserved"])
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
# 设置画笔和填充颜色
turtle.penup()
turtle.speed(0)
turtle.setx(-100)
turtle.sety(-150)
turtle.pendown()
# 画出正在使用的椅子
for i in range(Used):
    turtle.fillcolor(colors["Used"])
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
# 设置画笔和填充颜色
turtle.penup()
turtle.speed(0)
turtle.setx(-10)
turtle.sety(-300)
turtle.pendown()

# 初始化画笔和绘制参数
turtle.Turtle()
turtle.speed(0)
turtle.pensize(5)
turtle.penup()
x, y = -300, -200
iloop = 20  #正方形大小为20*20

#计算外层边框大小
rsize = len(posid) * iloop
csize = cmx * iloop

# 循环外层边框
turtle.goto(x, y)
turtle.setheading(0)
turtle.pendown()
turtle.forward(csize)
turtle.right(90)
turtle.forward(rsize)
turtle.right(90)
turtle.forward(csize)
turtle.right(90)
turtle.forward(rsize)
turtle.penup()

mp = {'Used seat status': "red", 'Empty seat status': "green", 'Occupancy status': "yellow"}

# at1 = [(32, 11), (2969, 242), (3902, 278)]
# at2 = [(0, 1001), (1328, 483), (3065, 855), (4335, 663)]
# at3 = [(4082, 1437)]
# posid.clear()
# posid.append(at1)
# posid.append(at2)
# posid.append(at3)

for t in posid:
    print("t.size = %d" % len(t))
    xx, yy = x, y
    for ct in t:
        turtle.right(90)
        color = mp[pos[(ct[0], ct[1])]]
        turtle.goto(xx, yy)
        turtle.begin_fill()
        turtle.fillcolor(color)
        turtle.pendown()
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
        turtle.end_fill()
        xx += 20
    y -= 20

data = ""
data += str(Empty) + str(Occupancy) + str(Used)

for t in posid:
    for ct in t:
        color = mp[pos[(ct[0], ct[1])]]
        if color == "green":
            data += '0'
        elif color == "yellow":
            data += '1'
        elif color == "red":
            data += '2'
    data += '3'

data += 'a'

print("data = " + data)

mySerial.open_ser()
mySerial.send_msg(data)
mySerial.read_msg()
mySerial.close_ser()

turtle.done()