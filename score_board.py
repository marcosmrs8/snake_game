from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score} High Score: {self.high_score}', align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score

        with open('data.txt', 'w') as data:
            data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score +=1
        self.update_score()