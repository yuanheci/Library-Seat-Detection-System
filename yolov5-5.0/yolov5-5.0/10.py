# Python program to draw color filled square in turtle programming
import turtle

for i in range(3):
    turtle.goto(0, 0)
    turtle.begin_fill()
    turtle.fillcolor("red")
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
# t = turtle.Turtle()
# t.fillcolor('blue')
# t.begin_fill()
# x, y = 0, 0
# for j in range(4):
#     t.goto(x, y)
#     for i in range(4):
#         t.forward(50)
#         t.right(90)
#     x += 60
# t.end_fill()




# import turtle
# turtle.color("red") #画笔改为红色
# turtle.goto(50,0) #去坐标（50,0）
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
#
# #右上角第一个矩形
# turtle.left(90) #箭头左转90度
# turtle.penup() #抬起画笔
# turtle.goto(70,0) #去坐标（70,0）
# turtle.pendown() #放下画笔
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
#
# turtle.left(90) #箭头左转90度
# turtle.penup() #抬起画笔
# turtle.goto(150,0) #去坐标（70,0）
# turtle.pendown() #放下画笔
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
# turtle.left(90) #箭头左转90度
# turtle.forward(50) #前进50像素
#
# #右下角第一个矩形
# turtle.penup()
# turtle.goto(70,-20)
# turtle.pendown()
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
#
# #左下角第一个矩形
# turtle.penup()
# turtle.goto(50,-20)
# turtle.pendown()
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)



# #导入画图库
# import turtle
#
# pe = []
# po = []
# pu = []
#
# # 输入每种状态的数量
# Empty = int(input("请输入空闲椅子数量：")) #空闲
#
# for i in range(0, Empty):
#     x = int(input("x = "))
#     y = int(input("y = "))
#     pe.append((x, y))
#
# Occupancy = int(input("请输入占座椅子数量："))#占座
#
# for i in range(0, Occupancy):
#     x = int(input("x = "))
#     y = int(input("y = "))
#     po.append((x, y))
#
# Used = int(input("请输入正在使用椅子数量："))#使用
# for i in range(0, Used):
#     x = int(input("x = "))
#     y = int(input("y = "))
#     pu.append((x, y))
#
# print("输出所有椅子坐标")
# for p in pe:
#     print("x = %d, y = %d" % (p[0], p[1]))
# print("--------------")
#
#
# # 隐藏画笔
# turtle.hideturtle()
# # 绘制所有椅子的状态
# def draw_chairs(num_occupied, num_in_use, num_vacant):
#     turtle.penup()
#     turtle.setpos(-300, 150)
#     turtle.pendown()
#     turtle.write("绿色: 空闲   黄色: 占座   红色: 正在使用", font=("Arial", 16, "bold"))
#
#     turtle.penup()
#     turtle.setpos(-300, 0)
#     turtle.pendown()
#     turtle.write("图书馆座位状态", font=("Arial", 24, "bold"))
#
#     turtle.penup()
#     turtle.setpos(-300, -50)
#     turtle.pendown()
#     turtle.write("空闲：%d 把" % num_vacant, font=("Arial", 16, "normal"))
#
#     turtle.penup()
#     turtle.setpos(-300, -100)
#     turtle.pendown()
#     turtle.write("占座：%d 把" % num_occupied, font=("Arial", 16, "normal"))
#
#     turtle.penup()
#     turtle.setpos(-300, -150)
#     turtle.pendown()
#     turtle.write("正在使用：%d 把" % num_in_use, font=("Arial", 16, "normal"))
#
#     turtle.penup()
#     turtle.setpos(-300, 50)
#     turtle.pendown()
#     turtle.setheading(0)
# draw_chairs(Occupancy, Used, Empty)
# # 设置画笔和填充颜色
# turtle.penup()
# turtle.speed(0)
# turtle.setx(-100)
# turtle.sety(-50)
# turtle.pendown()
#
# colors = {"Free":"green", "Reserved":"yellow", "Used":"red"}
#
# # 画出空闲椅子
# for i in range(Empty):
#     turtle.fillcolor(colors["Free"])
#     turtle.begin_fill()
#     for j in range(4):
#         turtle.forward(20)
#         turtle.left(90)
#     turtle.end_fill()
#     turtle.penup()
#     turtle.forward(30)
#     turtle.pendown()
#
# # 设置画笔和填充颜色
# turtle.penup()
# turtle.speed(0)
# turtle.setx(-100)
# turtle.sety(-100)
# turtle.pendown()
#
# # 画出占座椅子
# for i in range(Occupancy):
#     turtle.fillcolor(colors["Reserved"])
#     turtle.begin_fill()
#     for j in range(4):
#         turtle.forward(20)
#         turtle.left(90)
#     turtle.end_fill()
#     turtle.penup()
#     turtle.forward(30)
#     turtle.pendown()
#
# # 设置画笔和填充颜色
# turtle.penup()
# turtle.speed(0)
# turtle.setx(-100)
# turtle.sety(-150)
# turtle.pendown()
#
# # 画出正在使用的椅子
# for i in range(Used):
#     turtle.fillcolor(colors["Used"])
#     turtle.begin_fill()
#     for j in range(4):
#         turtle.forward(20)
#         turtle.left(90)   #逆时针移动
#     turtle.end_fill()
#     turtle.penup()
#     turtle.forward(30)
#     turtle.pendown()
# # 设置画笔和填充颜色
# turtle.penup()
# turtle.speed(0)
# turtle.setx(-10)
# turtle.sety(-300)
# turtle.pendown()
#
# # 计算总数量和长方形数量
# total_num = Empty + Occupancy + Used
# if((total_num % 4) != 0):
#     rect_num = total_num // 4 + 1
# else:
#     rect_num = total_num // 4
# # 初始化画笔和绘制参数
# turtle.Turtle()
# turtle.speed(0)
# turtle.pensize(5)
# turtle.penup()
# x, y = -300, -200
# iloop = 20
# # 循环绘制长方形和方块
# for i in range(rect_num):
#     turtle.goto(x, y)
#     turtle.setheading(0)
#     turtle.pendown()
#     turtle.forward(70)
#     turtle.right(90)
#     turtle.forward(40)
#     turtle.right(90)
#     turtle.forward(70)
#     turtle.right(90)
#     turtle.forward(40)
#     turtle.penup()
#
#     for j in range(4):
#         if Used > 0:
#             turtle.goto(x + 35, y - iloop)
#             turtle.begin_fill()
#             turtle.fillcolor("red")
#             turtle.pendown()
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.penup()
#             turtle.end_fill()
#             Used -= 1
#         elif Occupancy > 0:
#             turtle.goto(x + 35 , y - iloop)
#             turtle.begin_fill()
#             turtle.fillcolor("yellow")
#             turtle.pendown()
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.penup()
#             turtle.end_fill()
#             Occupancy -= 1
#         elif Empty > 0:
#             turtle.goto(x + 35 , y - iloop)
#             turtle.begin_fill()
#             turtle.fillcolor("green")
#             turtle.pendown()
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.right(90)
#             turtle.forward(20)
#             turtle.penup()
#             turtle.end_fill()
#             Empty -= 1
#
#     y -= 60
# #画图结束
# turtle.done()
#
