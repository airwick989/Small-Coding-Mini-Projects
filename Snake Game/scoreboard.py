from turtle import Turtle
import time

#These contants are to make it easy to change these characteristics in the future
#hard coding it into the body of the code would be bad programming
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.penup()
        self.initialise()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align= ALIGNMENT, font= FONT)

    def initialise(self):
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        
        self.score = 0
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align= "center", font= FONT)

        time.sleep(5)
        
        #Does a countdown before next game starts
        for i in range(3,0, -1):
            self.clear()
            self.write(f"{i}", align= "center", font= FONT)
            time.sleep(1)

        self.initialise()