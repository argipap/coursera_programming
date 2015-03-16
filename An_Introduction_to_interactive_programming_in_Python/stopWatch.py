#author: Papaefstathiou Anargyros
#based on template for "Stopwatch: The Game"
#An Introduction to Interactive Programming in Python (Part 1)
#The game is as follows: The user wins when stops the timer to 1.0, 2.0 or x.0 generally seconds

import simplegui
import time

# define global variables
t=0
width=300
height=200
number_of_stops=0
number_of_accurate_stops=0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #local variables for tenth of seconds, seconds and minutes
    tsec="00"
    sec="00"
    minute="0"
    #basic convert logic
    if t < 10:
        tsec = str(t%10)
    else:
        if t/600 == 0:
            tsec = str(t%10)
            sec = str(t/10)
        else:
            minute = str(t/600)
            sec = str(t%600/10)
            tsec = str(t%600%10)
    #helper statement for adding a "0" if sec involves only one digit
    if len(sec)==1:
                sec = "0"+sec
    #return statement in the corresponding format
    return minute+":"+sec+"."+tsec
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    timer.start()
    running = True
    
def stop_handler():
    global number_of_stops, number_of_accurate_stops ,t ,running
    timer.stop()
    if running == True:
        #number of total stops increment
        number_of_stops+=1
        #number of stops if user entered the button at 1.0, 2.0, 3.0 sec , etc..
        if t%10 == 0:
            number_of_accurate_stops+=1
    running = False
    
def reset_handler():
    global t, number_of_stops, number_of_accurate_stops, running
    timer.stop()
    t=0
    number_of_stops=0
    number_of_accurate_stops=0
    running = False

# define event handler for timer with 0.1 sec interval
def timer_increment():
    global t;
    t+=1;

# define draw handler
def draw(canvas):
    #draw time on the center of the canvas
    '''Compute values in order to draw text on the center of the canvas.
       Use of get_canvas_textwidth function for the computation'''
    centered_width = width/2 - frame.get_canvas_textwidth(format(t), 40)/2
    # adding 20 because font size = 40. (40/2 = 20)
    centered_height = height/2 + 20
    canvas.draw_text(format(t), (centered_width, centered_height), 40, "Blue")
    #draw text for x/y (number of accurate stop times /number of total stop times
    xy = str(number_of_accurate_stops) + "/" + str(number_of_stops)
    centered_width_xy = width - frame.get_canvas_textwidth(xy, 20)
    canvas.draw_text(xy, (centered_width_xy, 20), 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# register event handlers
timer = simplegui.create_timer(100, timer_increment)
frame.set_draw_handler(draw)
frame.add_button("Start", start_handler, 200)
frame.add_button("Stop", stop_handler, 200)
frame.add_button("Reset", reset_handler, 200)
#print frame.get_canvas_textwidth(str(time.time()), 20)

# start frame
frame.start()
