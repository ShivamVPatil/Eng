import os
import turtle

def main_line():
    tt=turtle.Turtle()
    s=turtle.Screen()
    s.bgcolor("black")
    tt.penup()
    tt.pensize(1)
    tt.pencolor("white")
    tt.hideturtle()
    tt.goto(-630,0)
    tt.pendown()
    tt.fd(1260)
    tt.penup()
    q=turtle.Turtle()
    q.penup()
    q.pencolor("white")
    q.hideturtle()
    q.pensize(1)
    q.goto(0,-720)
    q.lt(90)
    q.pendown()
    q.fd(1440)

    n=turtle.Turtle()
    n.setposition(0,0)
    n.pensize(1)
    n.pencolor("white")
    n.fd(630)
    m1=turtle.Turtle()
    m1.setposition(0,0)
    m1.pensize(1)
    m1.rt(180)
    m1.pencolor("white")
    m1.fd(633)
    





def write():
    wrr=turtle.Turtle()
    wrr.pensize(3)
    wrr.pencolor("white")
    wrr.penup()
    wrr.hideturtle()
    wrr.penup()
    wrr.goto(300,325)
    wrr.pendown()

    wrr.fd(337)
    wrr.rt(90)
    wrr.fd(50)
    wrr.rt(90)
    wrr.fd(337)
    wrr.rt(90)
    wrr.fd(50)
    wrr.rt(90)
    wrr.penup()
    wrr.goto(308,285)
    wrr.pendown()
    wrr.write("PROJECTION OF POINTS",font=("Ariel",20,"normal"))
    wrr.penup()
    wrr.goto(260,-190)
    wrr.pendown()
    wrr.fd(375)
    wrr.rt(90)
    wrr.fd(150)
    wrr.rt(90)
    wrr.fd(375)
    wrr.rt(90)
    wrr.fd(150)
    wrr.rt(90)
    wrr.penup()
    wrr.goto(269,-217)
    wrr.pendown()
    wrr.write("PBL assignment for engineering graphics",font=("Ariel",15,"normal"))
    wrr.penup()
    wrr.goto(269,-240)
    wrr.pendown()
    wrr.write("Made by-",font=("Ariel",15,"normal"))
    wrr.penup()
    wrr.goto(269,-267)
    wrr.pendown()
    wrr.write("YOUR NAME",font=("Ariel",15,"normal"))
    wrr.penup()
    wrr.goto(269,-292)
    wrr.pendown()
    wrr.write("YOUR NAME",font=("Ariel",15,"normal"))
    wrr.penup()
    wrr.goto(269,-320)
    wrr.write("Guided by Prof. name",font=("Ariel",15,"normal"))



   
   
   
def above_hp(k):
    x1=turtle.Turtle()
    x1.penup()
    x1.pensize(5)
    x1.pencolor("blue")
    x1.hideturtle()
    x1.goto(0,k*4)
    x1.pendown()
    x1.fd(1)
    al=turtle.Turtle()
    al.pencolor("white")
    al.penup()
    al.hideturtle()
    al.goto(-9,k*4)
    al.pendown()
    al.write("a'",font=("Ariel",10,"normal"))
   

def below_hp(k):
    x=turtle.Turtle()
    x.penup()
    x.pensize(5)
    x.pencolor("blue")
    x.hideturtle()
    x.goto(0,k*-4)
    x.pendown()
    x.fd(1)
    al=turtle.Turtle()
    al.penup()
    al.hideturtle()
    al.goto(9,k*-4)
    al.pendown()
    al.pencolor("white")
    al.write("a'",font=("Ariel",10,"normal"))

def in_front_vp(k):
    x2=turtle.Turtle()
    x2.penup()
    x2.pensize(5)
    x2.pencolor("blue")
    x2.hideturtle()
    x2.goto(0,k*-4)
    x2.pendown()
    x2.fd(1)
    al=turtle.Turtle()
    al.pencolor("white")
    al.penup()
    al.hideturtle()
    al.goto(-9,k*-4)
    al.pendown()
    al.write("a",font=("Ariel",10,"normal"))

def behind_vp(k):
    x3=turtle.Turtle()
    x3.penup()
    x3.pensize(5)
    x3.pencolor("blue")
    x3.hideturtle()
    x3.goto(0,k*4)
    x3.pendown()
    x3.fd(1)
    al=turtle.Turtle()
    al.pencolor("white")
    al.penup()
    al.hideturtle()
    al.goto(9,k*4)
    al.pendown()
    al.write("a",font=("Ariel",10,"normal"))



   
def hp_measure1(k):
    me1=turtle.Turtle()
    me1.pensize(2)
    me1.pencolor("white")
    me1.hideturtle()
    me1.penup()
    me1.goto(-57,(k*2))
    me1.pendown()
    me1.write(k,font=("Ariel",10,"normal"))

def hp_measure2(k):
    me2=turtle.Turtle()
    me2.pensize(2)
    me2.pencolor("white")
    me2.hideturtle()
    me2.penup()
    me2.goto(-22,(k*2))
    me2.pendown()
    me2.write(k,font=("Ariel",10,"normal"))


   

def vp_measure1(k):
    me3=turtle.Turtle()
    me3.pensize(2)
    me3.pencolor("white")
    me3.hideturtle()
    me3.penup()
    me3.goto(-57,(k*-2))
    me3.pendown()
    me3.write(k,font=("Ariel",10,"normal"))

def vp_measure2(k):
    me4=turtle.Turtle()
    me4.pensize(2)
    me4.pencolor("white")
    me4.hideturtle()
    me4.penup()
    me4.goto(-22,(k*-2))
    me4.pendown()
    me4.write(k,font=("Ariel",10,"normal"))
   
   
def turtle_arrowup1(k):
    ro1=turtle.Turtle()
    ro1.pensize(1)
    ro1.pencolor("yellow")
    ro1.penup()
    ro1.goto(-37,0)
    ro1.lt(90)
    ro1.pendown()
    ro1.fd(k*4)
    roa=turtle.Turtle()
    roa.penup()
    roa.pencolor("yellow")
    roa.goto(-37,3)
    roa.rt(90)


def turtle_arrowup2(k):
    ro2=turtle.Turtle()
    ro2.pensize(1)
    ro2.pencolor("yellow")
    ro2.penup()
    ro2.goto(-27,0)
    ro2.lt(90)
    ro2.pendown()
    ro2.fd(k*4)
    rob=turtle.Turtle()
    rob.penup()
    rob.pencolor("yellow")
    rob.goto(-27,3)
    rob.rt(90)
   
   



   
def turtle_arrowdown1(k):
    ro1=turtle.Turtle()
    ro1.pensize(1)
    ro1.pencolor("yellow")
    ro1.penup()
    ro1.goto(-35,0)
    ro1.rt(90)
    ro1.pendown()
    ro1.fd(k*4)
    roc=turtle.Turtle()
    roc.penup()
    roc.pencolor("yellow")
    roc.goto(-35,-3)
    roc.lt(90)

def turtle_arrowdown2(k):
    ro1=turtle.Turtle()
    ro1.pensize(1)
    ro1.pencolor("yellow")
    ro1.penup()
    ro1.goto(-50,0)
    ro1.rt(90)
    ro1.pendown()
    ro1.fd(k*4)
    rod=turtle.Turtle()
    rod.penup()
    rod.pencolor("yellow")
    rod.goto(-50,-3)
    rod.lt(90)

def load():
    lod=turtle.Turtle()
    lod.hideturtle()
    lod.pensize(3)
    lod.pencolor("blue")
    lod.penup()
  
    lod.goto(-50,50)
    lod.pendown()
    lod.fd(100)
    lod.rt(90)
    lod.fd(100)
    lod.rt(90)
    lod.fd(100)
    lod.rt(90)
    lod.fd(100)
    lod.penup()
    lod.clear()

def load1():
    load=turtle.Turtle()
    load.hideturtle()
    load.pensize(3)
    load.pencolor("blue")
    load.penup()
    
    load.goto(-50,50)
    load.pendown()
    load.rt(90)
    load.fd(100)
    load.lt(90)
    load.fd(100)
    load.lt(90)
    load.fd(100)
    load.lt(90)
    load.fd(100)
    load.penup()
    load.clear()
    
def loading():
    gg=turtle.Turtle()
    gg.hideturtle()
    gg.pensize(5)
    gg.pencolor("black")
    gg.penup()
    gg.goto(-50,-80)
    gg.write("LOADING...",font=("ariel",15,"normal"))


    
    


    


    

        

    
        
    
    
   
   
         
   


print("hello!\n")
print("If the point is in vp or in hp, please select any option and enter distance from hp and vp '0' respectively\n")
ch=int(input("enter 1 for above hp, 2 for below hp\n"))
vp=input("Enter 1 for front vp and 2 for behind vp\n")
dist=int(input("Enter distance from vp\n"))
distance=int(input("enter distance from hp\n"))

for i in range(1,5):
    loading()
    load()
    load1()
    
    
main_line()
write()

if ch==1:
     above_hp(distance)
     hp_measure1(distance)
     turtle_arrowup1(distance)
else:
     below_hp(distance)
     vp_measure2(distance)
     turtle_arrowdown1(distance)

if vp==1:
        in_front_vp(dist)
        vp_measure1(dist)
        turtle_arrowdown2(dist)
else:
     behind_vp(dist)
     hp_measure2(dist)
     turtle_arrowup2(dist)
