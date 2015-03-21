# Implementation of classic arcade game Pong
# author: Papaefstathiou Anargyros (based on template)
#An Introduction to Interactive Programming in Python (Part 1)

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
#constant multiple of velocity vector. Controls how fast the ball moves.
a = 1.0/60

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel = [0,0]
    ball_pos = [WIDTH / 2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240) # pixels per update (1/60 seconds)
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120, 240) # pixels per update (1/60 seconds)
    ball_vel[1] = -random.randrange(160, 180)
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = HEIGHT/2 
    paddle2_pos = HEIGHT/2
    score1 = 0
    score2 = 0
    #random choice for RIGHT or LEFT spawning
    choice = random.randrange(0,2)
    if choice == 0:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += a*ball_vel[0]
    ball_pos[1] += a*ball_vel[1]
    #update after collision with walls (top and bottom)
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen 
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    #keep paddle1 on screen
    if paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
        
    #keep paddle2 on sreen
    if paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH-HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide   
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: #check for left paddle and gutter
        #paddle and ball colission - check y coordinate
        #check for paddle1
        if paddle1_pos + HALF_PAD_HEIGHT >= ball_pos[1] - BALL_RADIUS and paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] + BALL_RADIUS:
            #update velocity - increase by 10% in every bounce
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            #spawn ball to different direction
            spawn_ball(RIGHT)
            score2 += 1
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH: #check for right paddle and gutter
        #check for paddle2
        if paddle2_pos + HALF_PAD_HEIGHT >= ball_pos[1] - BALL_RADIUS and paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] + BALL_RADIUS:
            #update velocity - increase by 10% in every bounce
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            #spawn ball to different direction
            spawn_ball(LEFT)
            score1 += 1
    
    # draw scores in the middle of every subfield
    canvas.draw_text(str(score1), ((WIDTH-PAD_WIDTH-frame.get_canvas_textwidth(str(score1),50)/2)/4 , HEIGHT/2 - 130), 50, 'Red')
    canvas.draw_text(str(score2), (3*(WIDTH-PAD_WIDTH-frame.get_canvas_textwidth(str(score1),50)/2)/4, HEIGHT/2 - 130), 50, 'Red')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel=4
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel     

def keyup(key):
    global paddle1_vel, paddle2_vel
    vel = 0
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#add button for restarting the game
restart = frame.add_button('Restart', new_game)


# start frame
new_game()
frame.start()
