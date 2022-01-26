#TURTLE CROSSING

from turtle import Screen
from timmy import Timmy
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.title("Turtle Crossing")
screen.tracer(0)

scoreboard = Scoreboard()
INITIAL_SPEED = 5
timmy = Timmy(INITIAL_SPEED)
carlist = []

screen.listen()     
screen.onkeypress(timmy.move_up, "Up")

game = True
counter = 0
sleep = 0.1

while game:
    time.sleep(sleep)
    screen.update()
    
    #Spawn cars in randomly
    if counter % 20 == 0:
        for i in range(0, scoreboard.score):
            car = Car(INITIAL_SPEED)
            carlist.append(car)
    
    #Move cars and Detect collisions with cars
    for car in carlist:

        if car.detect_collision(timmy):
            game = False
        
        if car.xcor() < -410:
            carlist.remove(car)

        car.move()

    #Detect successful crossing
    if timmy.ycor() > 280:
        scoreboard.increase_score()
        timmy.reset()
        

    counter += 1

#Detect end of game
scoreboard.game_over()
    

screen.exitonclick()