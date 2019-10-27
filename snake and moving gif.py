
# Simple snake game using Python 3 and Turtle module JJ 21 Oct 2019
# Sounds in Mac os only - using afplay or os.system
# Windows use winsound:
# import winsound
# winsound.PlaySound('laser.WAV, winsound.SND_ASYNC')
# linux uses aplay

# Place image/gif in same directory or simply use build in shapes

import turtle
import time
import random
import os


win = turtle.Screen()
win.title('Snake with Python3 and Turtle')
win.setup(width=500, height=500)
win.bgcolor('blue')
win.tracer(0)
win.register_shape('mouse1.gif')
win.register_shape('mouse2.gif')

pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.goto(0,220)
pen.color('red')
pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))

head = turtle.Turtle()
head.shape('square')
head.color('red')
head.up()
head.direction='stop'

segments = []
score = 0
segments.append(head)

food = turtle.Turtle()
food.s = 'mouse1.gif'   # Had to make this in order to change later
food.shape(food.s)
food.up()
food.goto(random.randint(-230,230), random.randint(-230,230))

def go_up():
    if head.direction != 'down':
        head.direction = "up"

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'
    
def move():
    if head.direction=='up':
        head.sety(head.ycor()+20)
        
    elif head.direction=='down':
        head.sety(head.ycor()-20)
        
    elif head.direction=='left':
        head.setx(head.xcor()-20)
        
    elif head.direction=='right':
        head.setx(head.xcor()+20)

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.shape('square')
    new_segment.color('grey')
    new_segment.up()
    segments.append(new_segment)
    segments.append(new_segment)
    segments.append(new_segment)
    os.system('say "ouch"&')
    

def border_crash():
    if head.xcor()>240 or head.xcor()<-240 \
       or head.ycor()>240 or head.ycor()<-240:
        os.system('afplay hit_sound.wav&')
        game_over()
        print('You crashed into the border!!')
        

def body_crash():
    for segment in segments[1:]:
        if segment.distance(head) < 10:
            os.system('afplay hit_sound.wav&')
            game_over()
            print('You crashed into your own body!!')

def game_over():
    time.sleep(1)
    head.direction = 'stop'
    for segment in segments:
        segment.goto(1000,1000)
    segments.clear()
    head.goto(0,0)
    segments.append(head)
    pen.clear()
    pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
    os.system('say "Game Over"')
    
win.listen()
win.onkeypress(go_up, 'Up')
win.onkeypress(go_down, 'Down')
win.onkeypress(go_left, 'Left')
win.onkeypress(go_right, 'Right')


def change_gif():   # Looping through the 2 gifs
    if food.s == 'mouse1.gif':
        food.s = 'mouse2.gif'
        food.shape(food.s)
    else:
        food.s = 'mouse1.gif'
        food.shape(food.s)

counter = 1

while True:
    win.update()
    border_crash()
    
    if head.distance(food)<20:
        food.goto(random.randint(-230,230), random.randint(-230,230))
        add_segment()
        score += 1
        pen.clear()
        pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
        
    for i in range(len(segments)-1,0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
            
    move()
    body_crash()
    time.sleep(0.1)
    
    change_gif()
    
