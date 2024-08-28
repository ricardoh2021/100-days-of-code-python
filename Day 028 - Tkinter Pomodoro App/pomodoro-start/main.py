import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    start_button.config(state=NORMAL)

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    reps = 0
    pomodoros_complete_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # Increasing to show the current rep one is on.
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    start_button.config(state=DISABLED)

    print(reps)

    if reps % 8 == 0 and reps % 2 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
        bring_to_front()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        bring_to_front()
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_minute = int(count / 60)
    count_second = count % 60

    display_minute = str(count_minute).zfill(2)
    display_second = str(count_second).zfill(2)

    print(count_minute, count_second)
    canvas.itemconfig(timer_text, text=f"{display_minute}:{display_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            marks += CHECK_MARK
        pomodoros_complete_label.config(text=marks)


def bring_to_front():
    window.attributes("-topmost", True)  # Set window to topmost
    window.after(2000, lambda: window.attributes("-topmost", False))  # Reset after 1 second


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

pomodoros_complete_label = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
pomodoros_complete_label.grid(row=3, column=1)

window.mainloop()
