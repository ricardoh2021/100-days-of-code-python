import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
data = pd.read_csv("50_states.csv")
score = 0
all_states = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states and (answer_state not in guessed_states):
    #     Add state to the map. Get first the state and its row.
        state_data = data[data["state"] == answer_state]
        x_pos = state_data.get(key="x").iloc[0]
        y_pos = state_data.get(key="y").iloc[0]

        state_title = turtle.Turtle()
        state_title.speed("fastest")
        state_title.penup()
        state_title.goto(x=x_pos,y=y_pos)
        state_title.hideturtle()
        state_title.write(arg=answer_state, font=("Arial", 8, "normal"))
        guessed_states.append(answer_state)
        all_states.remove(answer_state)
        score += 1

    print(answer_state)
    print(all_states)


df = pd.DataFrame(all_states, columns=["Missed States"])
df.to_csv('missed_states.csv', index=False)

