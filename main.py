import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height= 491, width= 725)
turtle.shape(image)

#code for getting the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    states_data = pandas.read_csv("50_states.csv")
    states_list = states_data["state"].to_list()
    if answer_state in states_list:
        row = states_data[states_data.state == answer_state]
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)

    elif answer_state == "Exit":
        missing_states = []
        for items in states_list:
            if items not in guessed_states:
                missing_states.append(items)
                row = states_data[states_data.state == items]
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(int(row.x), int(row.y))
                t.write(items)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()