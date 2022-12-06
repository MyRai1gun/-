import turtle as t #优点：不会出现重复的函数名
t.setup(650,350,200,200)
t.penup()
t.bk(250) #或 t.fd(-250)
t.pendown()
t.pensize(25)
t.colormode(255)
t.pencolor(255,215,0)
t.seth(-40)
for i in range(4):
    t.circle(40,80) #向下画弧线
    t.circle(-40,80) #向上画弧线
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done() #需要手动关闭窗体退出程序
