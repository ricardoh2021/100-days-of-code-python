from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Initial set up
        self.speed("fastest")
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.goto(0,280)
        self.color("white")
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()

