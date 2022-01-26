#PONG


from score import Score
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0), 30)
paddle_left = Paddle((-350, 0), 30)
ball = Ball(10, 10)
score_left = Score(-270)
score_right = Score(270)

screen.listen()     
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

game = True
SPEED_RAMP = 0.5

while game:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #make it bounce
        ball.y_bounce()
    
    #Detect collision with paddle
    #We would usually do this
    # if ball.distance(paddle_left) < 20 or ball.distance(paddle_right) < 20:
    #     x *= -1
    #But we need to detect a hit anywhere on the paddle, not just the centre of the paddle
    #So the logic behind this, is that if its gone left or right past a point on the screen, and if its within a 50 distance of a paddle,
    #then it hit the paddle
    #look at the udemy video if you need a visual
    if ball.xcor() > 330 or ball.xcor() < -330:
       if ball.distance(paddle_left) < 50 or ball.distance(paddle_right) < 50:
            
            ball.x_bounce()
            
            if ball.x > 0:
                ball.x += SPEED_RAMP
            else:
                ball.x -= SPEED_RAMP
            
            if ball.y > 0:
                ball.y += SPEED_RAMP
            else:
                ball.y -= SPEED_RAMP

            paddle_left.movement_speed += SPEED_RAMP
            paddle_right.movement_speed += SPEED_RAMP

            #ALTERNATIVELY, YOU COULD SLOWLY SPEED EVERYTHING UP BY SHORTENING THE LENGTH OF TIME THE SCREEN SLEEPS, BUT WE ALREADY DID
            #IT THIS WAY SO, OH WELL


    #Detect ball out of bounds
    if ball.xcor() > 380:
        score_left.increase_score()
        ball.respawn(paddle_left, paddle_right)
    if ball.xcor() < -380:
        score_right.increase_score()
        ball.respawn(paddle_left, paddle_right)

screen.exitonclick()