#SNAKE CLASS
from turtle import Turtle

class Snake:

    def __init__(self):

        self.snake_segments = []

        #create the initial 3 segments of the snake
        x = 0
        for snake_segment in range(0,3):
            self.add_segment((x, 0))
            x -= 20




    def add_segment(self, position):
        snake_segment = Turtle(shape= "square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)
    



    def extend_body(self):
        self.add_segment(self.snake_segments[-1].position())   
        #IN PYTHON, IF YOU PUT A NEGATIVE NUMBER AS A LIST INDEX, IT GETS THE LAST ELEMENT IN THE LIST


    
    
    def move(self):
        #make each segment of the snake go to the position of the segment before it
        for snake_segment in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[snake_segment].goto(self.snake_segments[snake_segment-1].pos())

        #move the first segment forwards
        self.snake_segments[0].forward(20)
    



    def face_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def face_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

    def face_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)

    def face_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)

    


    def reset(self):

        #eliminates all segments (turtles) in the snake body
        for segment in self.snake_segments:
            segment.reset()
        
        self.snake_segments.clear()     #Clears the snakes segments list
        self.__init__()     #Creates a new snake

    