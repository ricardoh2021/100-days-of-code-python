from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Initial set up
        self.speed("fastest")
        self.p1_score = 0
        self.p2_score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.p1_score}                  {self.p2_score}", align="center", font=('Arial', 40, 'normal'))

    def increase_score(self, player):
        if player == 1:
            self.p1_score += 1
        else:
            self.p2_score += 1

        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))

    def display_restart_quit(self):
        self.goto(0, -50)
        self.write("Press 'R' to Restart or 'Q' to Quit", align="center", font=('Arial', 20, 'normal'))

    def reset_score(self):
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()