from turtle import *
import random
import time
import math

setup(700,700)
bgcolor("black")
title("Snake Game")
tracer(0)
hideturtle()

head = Turtle()
head.shape("triangle")
head.color("#00FF00")
head.shapesize(1.4, 1.8)
head.penup()
head.speed(0)

tongue = Turtle()
tongue.shape("triangle")
tongue.color("red")
tongue.shapesize(0.2, 1.2)
tongue.penup()
tongue.speed(0)
tongue.hideturtle()

germ = Turtle()
germ.shape("circle")
germ.color("#FF0000")
germ.shapesize(1.6)
germ.penup()
germ.speed(0)
germ.goto(150,150)

spikes = []
for _ in range(8):
    s = Turtle()
    s.shape("circle")
    s.color("#FF7777")
    s.shapesize(0.35)
    s.penup()
    s.speed(0)
    spikes.append(s)

blood = []
for _ in range(15):
    b = Turtle()
    b.shape("circle")
    b.color("red")
    b.shapesize(0.2)
    b.penup()
    b.hideturtle()
    b.speed(0)
    blood.append(b)

segments = []
score = 0
flick_timer = 0

pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,310)
pen.color("white")
pen.write(f"Viruses Eaten:{score}", align="center", font=("Arial", 24, "normal"))

def tongue_flick():
    global flick_timer
    flick_timer += 1
    if flick_timer % 20 < 6:
        tongue.showturtle()
        ang = math.radians(head.heading())

        tx = head.xcor() + math.cos(ang) * 22
        ty = head.ycor() + math.sin(ang) * 22
        tongue.goto(tx, ty)
        tongue.setheading(head.heading())
    else:
        tongue.hideturtle()

def move_towards_germ():
    dx = germ.xcor() - head.xcor()
    dy = germ.ycor() - head.ycor()
    angle = math.atan2(dy,dx)
    angle += random.uniform(-0.35,0.35)
    head.setheading(math.degrees(angle))
    head.forward(10)

def move_germ():
    germ.setheading(germ.heading() - random.randint(-35,35))
    germ.forward(7)
    if abs(germ.xcor()) > 310 or abs(germ.ycor()) > 310:
        germ.setheading(germ.towards(0,0))
    for i, sp in enumerate(spikes):
        ang = i * 45 + time.time()*150%360
        r = 20
        x = germ.xcor() + math.cos(math.radians(ang)) * r
        y = germ.ycor() + math.sin(math.radians(ang)) * r
        sp.goto(x,y)

def blood_splash(x,y):
    for p in blood:
        p.goto(x,y)
        p.showturtle()
        p.setheading(random.randint(0,360))
        p.color(random.choice(["red","orange","darkred"]))
    for _ in range(8):
        update()
        for p in blood:
            p.forward(8)
            p.shapesize(p.shapesize()[0]*0.9)
        time.sleep(0.02)
    for p in blood:
        p.hideturtle()

while True:
    update()
    tongue_flick()
    move_towards_germ()
    move_germ()

    if head.distance(germ) < 22:
        blood_splash(germ.xcor(), germ.ycor())

        germ.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
        germ.color(random.choice(["#FF0000","#FF00FF","#FFFF00","#FFFFFF"]))

        b = Turtle()
        b.shape("circle")

        b.color(random.choice(["#228822","#32CD32","#006400"]))
        b.shapesize(0.95)
        b.penup()
        b.speed(0)
        segments.append(b)

        score += 1
        pen.clear()
        pen.write(f"Viruses Eaten:{score}", align="center", font=("Arial", 24, "normal"))

    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    time.sleep(0.025)

