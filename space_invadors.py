#space Invader
#Set up the screen
#python 3.x
#The turtle module provides turtle graphics primitives,
#in both object-oriented and procedure-oriented ways
#The OS module in python provides functions
#for interacting with the operating system
#raw input takes input as string
#use space key to fire bullet

import turtle
import os
import math



#set up the screen

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
#Picks up the turtle’s pen
border_pen.setposition(-200,-200)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(400)
    border_pen.lt(90)
    
border_pen.hideturtle()

#create the player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-150)
player.setheading(90)

playerspeed=15



#set the enemy
enemy=turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.setposition(-150,180)
enemyspeed=5
#move the player left and right
#xcor returns turtle's x coordinate


#create the player's bullet

bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=15
bulletstate="ready"

def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-180:
        x=-180
    player.setx(x)


def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>180:
        x=180
    player.setx(x)

def fire_bullet():
    #declear variable to be global if it needs to be changed
    #move the bullet straight above the player
    global bulletstate
    if bulletstate == "ready":
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if(distance<20):
        return True
    else:
        return False
    
#creat keyboard binding
turtle.listen()
#call to function move_left on left click
turtle.onkey(move_left,"Left")
#call to function move_right on left click
turtle.onkey(move_right,"Right")

turtle.onkey(fire_bullet,"space")
#main game loop
while True:
    #move the enemy
    x=enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)

    if enemy.xcor()>180:
        y=enemy.ycor()
        y-=20
        enemyspeed*=-1
        enemy.sety(y)
    if enemy.xcor()<-180:
        y=enemy.ycor()
        y-=20
        enemyspeed*=-1
        enemy.sety(y)
    if bulletstate == "fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

#check to see if bullet goes to the top
    if bullet.ycor()>180:
        bullet.hideturtle()
        bulletstate="ready"
    if isCollision(bullet,enemy):
        bullet.hideturtle()
        bulletstate="ready"
        x=player.xcor()
        bullet.setposition(x,-150)
        enemy.setposition(-180,180)
        
    if isCollision(player,enemy):
        player.hideturtle()
        enemy.hideturtle()
        wn.bye()        
        print("Game Over")
        break
    if enemy.ycor()<-195:
        enemy.setposition(-150,180)

