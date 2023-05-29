## 基于Yolov5的图书馆座位监测系统

一款用于检测图书馆座位使用情况的系统，可以检测座位的三种状态：空座、正在使用、占座。

使用基于Pytorch的Yolov5训练该模型，并用STM32F1作为下位机通过串口通信接收识别结果，将一片区域的座位情况显示到LCD显示屏上。

该工程仅作为一个Demo实现了基本功能。存在的问题有：
+ 模型识别准确率一般，因为训练所用的数据集较少
+ 将图像中的座位信息还原成行列情况用于显示的算法有待优化，目前仅能处理人与人之间重叠较少且图像中座位均为水平或垂直排布的情况，对于有一定角度的图像难以处理。

**注**：`hat.py`为主程序所在文件。

---

## 结果展示

### 图片1：
![47](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/9c2b2693-03d3-4b6a-bbe7-132d07cb5586)

### 上位机端：
![11](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/caa62dd0-4e94-4cda-8487-2b080b261261)

![111](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/1f668685-f9fe-467f-8719-922f992576df)


### 下位机端：
![00CDDE65BBA384536A32A23BDCB77D28](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/dd9370a6-df89-4e4c-a9a6-959c84616790)

---

### 图片2：
![120](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/ef87b6c7-cdd2-4d2b-8cf0-4151b8a9dd63)


### 上位机端：
![22](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/586760b6-96f2-41cd-9639-7c9a1efc15d4)

![222](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/14d4fc8c-bbe6-4fd4-87fe-13b367069f4c)

### 下位机端：
![33CEF0FBF44B8AE177DEE5DEEB6CF34F](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/bc7c1c61-c14a-4e6f-9765-efaf38322e57)

---

![6AB576DA186C2BC5DDF77BFDB225B4FC](https://github.com/yuanheci/Library-Seat-Detection-System/assets/97277559/f7d5377a-eb32-412c-9cb7-29733ad74565)
