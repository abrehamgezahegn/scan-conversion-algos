from graphics import *
from math import floor

window = GraphWin('DDA Line',750,750) 
window.setBackground('black')
label = Text(Point(300,100),"Click on two different points to get a DDA line.")
label.draw(window)

def draw_DDA_line( x1, y1, x2, y2):
    # calc change in x and y
    x_delta = x2 - x1 
    y_delta = y2 - y1 

    # calc slope
    m = y_delta / x_delta 

    # if slope (m) is <= 1 set steps to x_delta
    if abs(x_delta) >= abs(y_delta):
        steps = x_delta 
  
    # if slope (m) is > 1 set steps to y_delta
    else:
        steps = y_delta 

    steps = abs(steps);

    x=x1;
    y=y1;

    point_1 = Point(floor(x1 + 0.5), floor(y1 + 0.5))
    point_1.draw(window) 

    point_2 = Point(floor(x2 + 0.5), floor(y2 + 0.5))
    point_2.draw(window)

    # calculate x increment and y increment
    x_inc = x_delta / steps;
    y_inc = y_delta / steps;

    # draw line by incrementing 
    # x and y until step is reached
 
    while steps >= 0:
        x = x_inc + x
        y = y_inc + y
   
        pt = Point(floor(x + 0.5), floor(y + 0.5))
        pt.setFill("white")
        pt.draw(window)
        steps -= 1




def ask_for_coords():
    """Function to capture points from user"""
    point_1 = window.getMouse()
    point_2 = window.getMouse()
    return point_1.getX() , point_1.getY(), point_2.getX() , point_2.getY();

# ask for two points, ask again if x1 == x2. 
# this filters out vertical lines
x_initial,y_initial,x_final,y_final = ask_for_coords()
while  x_initial == x_final:
    x_initial,y_initial,x_final,y_final = ask_for_coords()


draw_DDA_line(x_initial,y_initial,x_final,y_final)


window.getMouse()
window.close()