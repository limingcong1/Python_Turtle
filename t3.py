#需求:一开始显示中山大学及Sun-Yat-sen University,然后两只鸭子游进来挡住了
#中字的位置,要么中字被鸭子推走了
#最后在横匾中央显示时间，地点
from turtle import *
import random
import time

def head(x,y):
    penup()
    goto(x,y)
    setheading(-90)
    forward(45)
    setheading(-70)
    circle(70,extent=330)
    
def mouth(x,y):
    #color(239,69,19)
    setposition(x,y)
    setheading(0)
    setheading(200)
    forward(70)
    circle(10,extent=165)
    setheading(0)
    forward(65)
    penup()
    goto(x-20,y-20)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
       

def eyes(x,y):
    goto(x+45,y-10)
    
    color('black')
    begin_fill()
    circle(15)
    end_fill()
    
def ellipse(x,y):
    goto(x+80,y-80)
    setheading(-90)
    a=0.1
    for i in range(180):
        if 0<=i<45 or 90<=i<135:
            a=a+0.15
            left(2)
            fd(a)
        else:
            a=a-0.15
            lt(2)
            fd(a)
    

    
def mkduck(name):
    reset()
    begin_poly()
    x=0
    y=0
    head(x,y)
    mouth(x,y)
    eyes(x,y)
    ellipse(x-15,y-50)
    end_poly()
    
    newlow=get_poly()
    ht()
    register_shape(name,newlow)


def randomposition():
    x=random.randint(-300,150)

    y=random.randint(150,300)

    return x,y

   
    
    

if __name__=='__main__':
    
    tracer(False)
    mkduck('duck')
    clear()
    tracer(True)
     #初始化所有的画笔，并安排好大小
    tracer(False)
    printer=Turtle()
    printer.shape('duck')
    printer.shapesize(0.1,0.1,0.1)
    printer.setheading(90)
    printer.speed(1)
    printer.ht()
    mover1=Turtle()
    mover1.shape('duck')
    mover1.shapesize(0.1,0.1,0.1)
    mover1.ht()
    mover1.penup()
    mover1.goto(-70,500)
    mover2=mover1.clone()
    
    
    
    tracer(True)
    #printer出场
    printer.penup()
    printer.goto(0,300)
    printer.st()
    printer.goto(0,100)
    printer.pendown()
    word_list=['Sun Yat-sen University','中山大学毕业照','June 12th/13th, 2018','6月12日至6月13日','Leo,里奥,青铜玩家徘徊者,珠江边跑王,广州塔底常客暨祖国未来接班人','带你游中大,走珠江,看广州最贵的房子,可能还包饭']
    length=len(word_list)
    font=[('Courier',14,'bold'),('楷体',14,'bold')]
    counter=0
    for word in word_list[:4]:
        if counter%2==0:
            fontfont=font[0]
        else:
            fontfont=font[1]
        counter+=1
        printer.penup()
        printer.setheading(90)
        printer.backward(40)
        printer.setheading(0)
        printer.setheading(90)
        printer.pendown()
        printer.write(word,align='center',font=fontfont)
    #介绍自己
    printer.penup()
    printer.setheading(90)
    printer.backward(40)
    printer.setheading(0)
    printer.pendown()
    printer.write(word_list[4],align='center',font=fontfont)


    
    for word in word_list[5:]:
        printer.penup()
        printer.setheading(90)
        printer.backward(40)
        printer.setheading(0)
        #printer.goto(randomposition())
        printer.pendown()
        printer.write(word,align='center',font=fontfont)
    printer.ht()

    time.sleep(1) 

    #鸭子掉下来盖住yat
    mover1.st()
    mover1.speed(3)
    mover1.setheading(90)
    mover1.goto(-70,80)
    for i in range(1):
        a=mover2.clone()
        a.st()
        a.speed(5)
        a.fd(3)
        a.setheading(90)
        a.goto(-40+i*15,80)

    time.sleep(20)
        
    

    
    
    
    

