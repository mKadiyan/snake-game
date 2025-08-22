from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "bold"))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "bold"))

