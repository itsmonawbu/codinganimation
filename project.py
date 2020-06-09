"""
project.py
------------
Cartoon Network inspired graphic program
Utilizing the original cartoon network animation logo
as inspiration in accordance with what we learn in
lecture 10 and lecture 11 - bouncing balls and moving images
"""

import tkinter
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageTk
from simpleimage import SimpleImage




CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels
BALL_SIZE = 50



def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Cartoon Network Throwback')


    # top middle left square with text
    r = canvas.create_rectangle(0, 134, 166, 300, outline='black')
    canvas.create_text(230, 205, font='Sans 200 bold', text="C", fill='black')
    # bottom middle right square with text
    rect = canvas.create_rectangle(600, 300, 766, 466, outline='black', fill='SlateGray1')
    canvas.create_text(380, 370, font='Sans 200 bold', text="N", fill='white')
    # Title text
    title = canvas.create_text(300, 0, font='Sans 20 bold',text="CARTOON NETWORK", fill='black')

    # moves left square to the center
    while get_left_x(canvas,r) < CANVAS_WIDTH/4:
        # update world
        canvas.move(r, 5, 0)
        # redraw canvas
        canvas.update()
        #pause
        time.sleep(1/50)
    # move right square to the center
    while get_right_x(canvas, rect) > 466:
        # update world
        canvas.move(rect, -15, 0)
        #redraw canvas
        canvas.update()
        #pause
        time.sleep(1/50)

    # move title to the center and jump
    while get_top_y(canvas, title) < 300:
        # update world
        canvas.move(title, 0, 15)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50)

    # load the .gif image image
    gif1 = ImageTk.PhotoImage(Image.open("we bare bears movement.gif"))
    gif = canvas.create_image(10, 290, image=gif1)
    image1 = ImageTk.PhotoImage(Image.open("agm.png"))
    image = canvas.create_image(400, -200, image=image1)
    ed = ImageTk.PhotoImage(Image.open("eee.png"))
    ed1 = canvas.create_image(200, 800, image=ed)

    while get_left_x(canvas, gif) < 800:
        # update world
        canvas.move(gif, 20, 0)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50)

    while get_top_y(canvas, image) < 200:
        # update world
        canvas.move(image, 0, 30)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50)

    while get_top_y(canvas, ed1) > 400:
        # update world
        canvas.move(ed1, 0, -30)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50)

    # create ball bouncing
    canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, tags="Bob", outline='black')
    canvas.create_oval(125, 125, 175, 175, tags="Bob", outline='black')
    canvas.create_oval(400, 200, 450, 250, tags="Bob", outline='black')
    canvas.create_oval(150, 400, 200, 450, tags="Bob", outline='black')
    canvas.create_oval(300, 0, 350, 50, tags="Bob", outline='black')
    canvas.create_oval(550, 0, 600, 50, tags="Bob", outline='black')
    canvas.create_oval(500, 500, 550, 550, tags="Bob", outline='black')
    canvas.create_oval(25, 400, 75, 450, tags="Bob", outline='black')
    canvas.create_oval(175, 225, 225, 275, tags="Bob", outline='black')
    canvas.create_oval(400, 425, 450, 475, tags="Bob", outline='black')


    dx = 0.5
    dy = 20

    while True:
        # update world
        canvas.move("Bob", dx,dy)
        # redraw canvas
        if hit_left_wall(canvas, "Bob") or hit_right_wall(canvas, "Bob"):
            dx *= -1
        if hit_top_wall(canvas, "Bob") or hit_bottom_wall(canvas, "Bob"):
            dy *= -2
        canvas.update()
        # pause
        time.sleep(1 / 50.)
        change_color(canvas, "Bob")
    # change the color of the N box

        change_color(canvas, rect)
        canvas.update()
        # pause
        time.sleep(1 / 50.)

    canvas.mainloop()





def change_color(canvas, object):
    '''
    When you call this method, the provided shape will change color to a
    randomly chosen color.
    :param canvas: the canvas where the shape exists
    :param shape: the shape you want to have its color changed
    '''
    # 1. get a random color
    color = random.choice(['SlateGray1', 'salmon', 'red', 'yellow', 'plum', 'snow3', 'VioletRed1',
                           'RosyBrown', 'white smoke', 'tomato3', 'tan1', 'SkyBlue1', 'SeaGreen1', 'RosyBrown4'])
    # 2. use the tkinter method to change the shape's color
    canvas.itemconfig(object, fill=color, outline=color)  # change color





def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 1


def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 1


def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH


def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT


######## These helper methods use "lists" ###########
### Which is a concept you will learn Monday ###########

def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


def mouse_moved(event):
    print('x = ' + str(event.x), 'y = ' + str(event.y))

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()

    canvas.bind("<Motion>", mouse_moved)
    return canvas




if __name__ == '__main__':
    main()
    canvas.postscript(file='filename.ps', colormode='color')