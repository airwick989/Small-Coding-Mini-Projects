#SNAKE GAME

from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    #turns screen animations off

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()     
screen.onkey(snake.face_up, "Up") 
screen.onkey(snake.face_left, "Left")
screen.onkey(snake.face_down, "Down")
screen.onkey(snake.face_right, "Right")   

game = True

def reset_game():
    scoreboard.reset()
    snake.reset()

while game:

    screen.update() #updates whats on the screen
    time.sleep(0.1) #adds a 0.1 second delay
    
    snake.move()

    #Detect collision with food
    if snake.snake_segments[0].distance(food) < 15: #we add a little buffer from 10
        food.refresh()
        scoreboard.increase_score()
        snake.extend_body()
    
    #Detect collision with wall
    if snake.snake_segments[0].xcor() > 290 or snake.snake_segments[0].xcor() < -290 or snake.snake_segments[0].ycor() > 290 or snake.snake_segments[0].ycor() < -290:
        reset_game()

    #Detect collision with self (except the head itself)
    for segment in snake.snake_segments[1:]:    #using slicing here so we don't need an if statement to avoid the head
        if snake.snake_segments[0].distance(segment) < 10:
            reset_game()

    #This is what it would be without slicing
    # for segment in snake.snake_segments:
    #     if segment != snake.snake_segments[0]:
    #         if snake.snake_segments[0].distance(segment) < 10:
    #             end_game()




screen.exitonclick()