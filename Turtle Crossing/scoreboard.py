from turtle import Turtle

#These contants are to make it easy to change these characteristics in the future
#hard coding it into the body of the code would be bad programming
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  #Now we can inherit attributes and methods from the turtle class
        self.score = 1
        self.penup()
        self.goto(-320, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font= ("Courier", 80, "bold"))