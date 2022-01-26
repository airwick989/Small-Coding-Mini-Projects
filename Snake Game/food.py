from turtle import Turtle
from random import randint

AREA_DIMENSION = 260

class Food(Turtle):

    def __init__(self):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        self.shape("circle")
        self.penup()
        
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)  #the normal height and width of a shape is 20x20
        #we are essentially halfing the size of the shape, making it 10x10

        self.color("blue")
        self.speed("fastest")   #so we dont have to watch the food go to its position, its sort of already there
        self.refresh()
    
    def refresh(self):
        self.goto(randint(-AREA_DIMENSION, AREA_DIMENSION), randint(-AREA_DIMENSION, AREA_DIMENSION))  
        #puts it in a random location within our canvas