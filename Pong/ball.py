#BALL CLASS
from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        #Essentially makes our Paddle object a Turtle object

        self.initial_x = abs(x)
        self.initial_y = abs(y)
        self.x = self.initial_x
        self.y = self.initial_y
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x *= -1
    
    def y_bounce(self):
        self.y *= -1

    def respawn(self, paddle1, paddle2):
        paddle1.reset()
        paddle2.reset()
        time.sleep(5)
        self.goto(0, 0)
        
        if self.x > 0:
            self.x = self.initial_x * -1
        else:
            self.x = self.initial_x

        if self.y > 0:
            self.y = self.initial_y * -1
        else:
            self.y = self.initial_y