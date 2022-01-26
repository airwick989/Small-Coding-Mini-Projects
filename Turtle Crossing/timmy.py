#TIMMY CLASS

from turtle import Turtle

class Timmy(Turtle):

    def __init__(self, movement_speed):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        
        self.movement_speed = abs(movement_speed)
        self.shape("turtle")
        self.color("chartreuse4")
        self.penup()
        self.reset()
        self.setheading(90)

    def move_up(self):
        self.forward(self.movement_speed)

    def reset(self):
        self.goto(0, -280)