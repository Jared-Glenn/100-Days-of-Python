import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

states = pd.read_csv("50_states.csv")
running = True
guesses = set()
lives = 3

while running:
    score = len(guesses)

    if score >= 50:
        running = False
        writer.goto(0, 150)
        writer.write("YOU WON!", align="center", font=("Arial", 25, "bold"))
        continue

    if lives <= 0:
        running = False
        writer.goto(0, 150)
        writer.write("YOU LOST!", align="center", font=("Arial", 25, "bold"))
        continue

    answer_state = (screen.textinput(title="Guess the State", prompt=f"Correct States: {score}, Lives: {lives}/3\nWhat's another state's name?")).capitalize()
    if answer_state in guesses:
        continue
    elif answer_state == "Exit":
        missing = []
        for index, row in states.iterrows():
            if row.state not in guesses:
                missing.append(row.state)
        df = pd.DataFrame(missing)
        df.to_csv("states_you_missed.csv", index=False)
        break

    if answer_state in states["state"].unique():
        guesses.add(answer_state)
        x = int((states[states["state"] == answer_state]).x)
        y = int((states[states["state"] == answer_state]).y)
        writer.goto(x, y)
        writer.write(answer_state, align="center", font=("Arial", 10, "normal"))
    else:
        lives -= 1
        continue





screen.exitonclick()