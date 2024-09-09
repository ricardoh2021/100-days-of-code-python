from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.after_id = None
        self.question_number = quiz_brain.question_number
        self.quiz = quiz_brain
        self.score = self.quiz.score
        self.buttons = []

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_text = Label(text=f"Score: {self.score}/{self.question_number}")
        self.score_text.config(bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.canvas.grid(row=1, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(150, 100, text="Random Question Here", font=QUESTION_FONT, fill="black", width=280)


        TRUE_IMG = PhotoImage(file="images/true.png")
        FALSE_IMG = PhotoImage(file="images/false.png")

        self.true_button = Button(image=TRUE_IMG, command=self.check_true_answer)
        self.buttons.append(self.true_button)
        self.false_button = Button(image=FALSE_IMG, command=self.check_false_answer)
        self.buttons.append(self.false_button)


        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.enable_buttons()
        self.update_score()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.disable_buttons()
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
        self.after_id = self.window.after(1000, self.get_next_question)
        self.score = self.quiz.score
        self.question_number = self.quiz.question_number
        if is_right:
            print("Displaying green")
            self.canvas.config(bg="green")
        else:
            print("Displaying red")
            self.canvas.config(bg="red")

    def update_score(self):
        self.score_text.config(text=f"Score: {self.score}/{self.question_number}")

    def disable_buttons(self):
        # Disable all buttons
        for button in self.buttons:
            button.config(state=DISABLED)

    def enable_buttons(self):
        # Re-enable all buttons
        for button in self.buttons:
            button.config(state=NORMAL)





