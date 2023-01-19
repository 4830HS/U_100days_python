from tkinter import *
import datetime as dt
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#d90429"
GREEN = "#ccff33"
PASTEL_GREEN = "#8cb369"
BRIGHT_YELLOW = "#f8bc04"
WHITE = "#FFFFFF"
BLACK = "#000000"
GRAY = "#d3d4d9"
ORANGE = "#e36414"
PURPLE = "#cdb4db"

FONT_NAME = "Monoton"
# FONT_NAME = "Monoton"
# FONT_NAME = "Calibri"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer() :
    # 설정했던 after 메소드 취소하여 설정했던 타이머를 취소해야 함. 하지만 window.after 함수(timer)는 def count_down(count) 내의 로컬 변수이기 때문에 그곳에서 꺼내야 함. -> 전역 변수로 만들기(timer = None)
    window.after_cancel(timer)
    # reset해야 하는 목록들
    # 1. timer_text -> 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # 2. title_label -> "Timer"
    title_label.config(text="Timer", fg=PURPLE, bg=BLACK, font=("Monoton", 45, "bold"))
    # 3. reset check_mark -> 0
    check_mark.config(text="")
    # 4. reps reset : reset해도 reps는 계속 증가하기 때문에, reset을 누른 뒤, start를 누르면 다음 단계로 넘어감.
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# start 버튼을 눌렀을 때만 타이머 작동하도록
def start_timer() :
    global reps
    reps += 1

    # count_down(5*60)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        # If it's the 8th rep :
        count_down(long_break_sec)
        title_label.config(text="Break", fg=PASTEL_GREEN)
    elif reps % 2 == 0 :
        # If it's 2nd/4th/6th rep :
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=GREEN)
    else :
        # If it's the 1st/3rd/5th/7th rep :
        count_down(work_sec)
        title_label.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time
# # 시간 지연을 위해 time.sleep() module 사용 -> 1초
# count = 5
# while True :
#     time.sleep(1)
#     count -= 1
# # 하지만, 이미 마지막 줄의 mainloop()에서 지속적으로 프로그램 체크 중. 따라서 while loop는 중복되어 실행되지 못함. -> 대신 tkinter 내장 메소드를 사용해야 함. => after()

def count_down(count) :

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Dynamic typing : 굳이 유형을 정해주지 않아도, 실행시 데이터 유형을 바꿔줌.
    if count_sec < 10 :
        count_sec = f"0{count_sec}"

    # label이 아닌, canvas 요소를 변경하려면 아래의 메소드를 사용해야 함. 이후, 괄호 안에 실제로 구성하려는 특정한 항목을 넣음. 그리고 실제로 변경하려는 구체적인 내용 추가.(kwarg 즉, 키워드 인자)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    # print(count)
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count -1)
        # after 메소드는 일정시간이 지난 뒤에 특정 함수 또는 메소드를 실행시킴. 밀리 초를 단위로 하기 때문에 1초 = 1000밀리초
    # 하나의 rep을 완료하면 0에서 시간이 멈춰버림. 0초가 되었을 때 자동으로 start_timer가 triger 될 수 있도록 하기 위해 'else' 추가.
    else :
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions) :
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #   
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=BLACK)

canvas = Canvas(width=400, height=400, bg=BLACK, highlightthickness=0)
# 사용하려는 사진이나 그림이 캔버스의 중간에 위치하게 하려면 width와 height의 중간값이어야 함.
background_image = PhotoImage(file="Day28/background.png")
canvas.create_image(200, 210, image = background_image)
timer_text = canvas.create_text(200, 180, text = "00:00", fill = "white", font = (FONT_NAME, 60, "bold"))
canvas.grid(column=1, row=2)

# Date Label
date = dt.datetime.now()
date_label = Label(window, text = f"{date:%a, %b %d, %Y}", fg=BRIGHT_YELLOW, bg=BLACK, font=("Monoton", 20, "bold"))
date_label.grid(column=1, row=0)

# Title Label
title_label = Label(text = "Timer", fg=PURPLE, bg=BLACK, font=("Monoton", 45, "bold"))
title_label.grid(column=1, row=1)
title_label.config(pady=20)

# Start Button
start_button = Button(text = "Start", width=7, height=1, bg = GRAY, font=("Calibri", 17, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Reset Button
reset_button = Button(text = "Reset", width=7, height=1, bg = GRAY, font=("Calibri", 17, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

# Check Mark
check_mark = Label(bg = BLACK, fg = ORANGE, font = (300))
check_mark.grid(column=1, row=4)

window.mainloop()