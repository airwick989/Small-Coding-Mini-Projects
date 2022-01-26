#CAR CLASS

from turtle import Turtle
from random import choice, randint

class Car(Turtle):

    def __init__(self, movement_speed):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class

        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        self.movement_speed = abs(movement_speed)
        self.shape("square")
        self.shapesize(stretch_len= 2, stretch_wid= 1)
        self.color(choice(self.colors))
        self.penup()
        self.setheading(180)
        self.setpos(410, randint(-230, 250))
    
    def detect_collision(self, timmy):
        if timmy.ycor() >= self.ycor() - 20 and timmy.ycor() <= self.ycor() + 20 and self.distance(timmy) < 30:
            return True
    
    def move(self):
        self.forward(self.movement_speed)