from turtle import Turtle

#These contants are to make it easy to change these characteristics in the future
#hard coding it into the body of the code would be bad programming
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class Score(Turtle):

    def __init__(self, position):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position, 200)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()