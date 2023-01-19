# Step 1 : Convert the guess to Title case
# Step 2 : Check if the guess is among the 50 states
# Step 3 : Write correct guesses onto the map
# Step 4 : Use a loop to allow the user to keep guessing
# Step 5 : Record the correct guesses in a list
# Step 6 : Keep track of the score

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day25/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y) :
#     print(x,y)

# # Event listener 만들기
# turtle.onscreenclick(get_mouse_click_coor)

# # 코드가 실행을 끝내도 화면이 계속 열려있도록 하기
# turtle.mainloop()

# Step 2 : Check if the guess is among the 50 states
data = pandas.read_csv("Day25/us_states_game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # if answer_state == "Exit" :
    #     # 대소문자 구분해야 하므로 "E"
    #     missing_states = []
    #     for state in all_states :
    #         if state not in guessed_states :
    #             missing_states.append(state)
    #     # 맞추지 않은 목록들을 csv 파일로 바꾸기
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv("Day25/us_states_game/states_to_learn.csv")
    #     break

    if answer_state == "Exit" :
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day25/us_states_game/states_to_learn.csv")
        break

    # If anwer_state is one of the states in all the states of the 50_states
    if answer_state in all_states :
        guessed_states.append(answer_state)
        # If they got it right :
            # Create a turtle to wrtie the name of the state at the state's x and y coodinate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state)
        # t.write(state_data.state.item())
        t.write(answer_state)

# states_to_learn.csv -> user가 게임을 끝냈을 때까지 맞추지 못한 주의 이름이 포함된 csv 파일 만들기(Save the missing states to a .csv)