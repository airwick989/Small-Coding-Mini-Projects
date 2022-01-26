#PADDLE CLASS
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates, movement_speed):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        #Essentially makes our Paddle object a Turtle object
        self.coordinates = coordinates
        self.movement_speed = abs(movement_speed)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.color("white")
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        self.move(+self.movement_speed)

    def move_down(self):
        self.move(-self.movement_speed)

    def move(self, direction):
        new_y = self.ycor() + direction
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(self.coordinates)



    