from graphics import *
from math import floor

BACKGROUND_COLOR="white"
LINE_COLOR="black"


# define window to work with 
win = GraphWin('Bresenham’s Circle',750,750)
win.setBackground(BACKGROUND_COLOR)


label = Text(Point(750/2,50),"Specify radius of the circle please.")
label.draw(win) 


def draw_point(pt):
    """ Accepts a point instance and draws the point """
    pt.setFill(LINE_COLOR) 
    pt.draw(win)


def plot_circle(xi,yi,x,y):
    """Given four points it plots the circle using 8 arcs"""
    point_1 = Point(xi+x, yi+y) 
    draw_point(point_1);

    point_2 = Point(xi-x, yi+y) 
    draw_point(point_2);

    point_3 = Point(xi+x, yi-y) 
    draw_point(point_3);

    point_4 = Point(xi-x, yi-y) 
    draw_point(point_4);

    point_5 = Point(xi+y, yi+x) 
    draw_point(point_5);

    point_6 = Point(xi-y, yi+x) 
    draw_point(point_6);

    point_7 = Point(xi+y,yi-x)
    draw_point(point_7);

    point_8 = Point(xi-y, yi-x) 
    draw_point(point_8);


def draw_bresenhams_circle(x_initial,y_initial,radius):
    """Loop using x and plot and generate 4 points used to draw an arc"""

    # initial 
    x,y,r= 0, radius , radius

    # define decision parameter
    d = 3 - 2 * r

    xi=x_initial
    yi=y_initial

    # initial points 
    plot_circle(xi,yi,x,y)


    # while loop to iterate until x == y 
    # where angle = 45deg
    
    while x <= y :
        x = x + 1
        if d<0:
            d = d + (4*x) +6
        else:
            y = y - 1;
            d = d + 4*(x-y) + 10
        plot_circle(xi,yi,x,y) 


# get initial x,y points from user
point_one = win.getMouse()
x_initial = point_one.getX()
y_initial = point_one.getY()

# get final x,y points from user and
# calculate radius

point_two = win.getMouse()
x_final = point_two.getX()

radius = abs(x_initial - x_final)

#draws the circle
draw_bresenhams_circle(x_initial,y_initial,radius)


win.getMouse()
win.close()