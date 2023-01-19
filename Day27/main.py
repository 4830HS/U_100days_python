# import tkinter
from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label 만들기
# my_label = tkinter.Label(text = "I am a Label", font = ("Arial", 24, "bold"))
my_label = Label(text = "I am a Label", font = ("Arial", 24, "bold"))

# 위의 라벨대로 코드를 실행하면 화면에 아무것도 나오지 않음. 컴포넌트를 배치하는 방법 중 가장 쉬운 방법 중 하나는 그 컴포넌트에 pack() method를 호출하는 것. -> 스크린에 컴포넌트를 배치하고 자동적으로 화면 중앙으로 가도록 함.
my_label.pack()
# **kw

# 만약 Label을 왼쪽으로 치우치게 배치하고 싶다면?
# my_label.pack(side="left")
# 밑으로 치우치게 하고 싶다면? bottom
# 화면의 중간으로 배치하고 싶다면?
# my_label.pack(expand=True)

# Label의 이름을 변경하고 싶다면?
my_label["text"] = "New Text"
my_label.config(text = "New Text")

# Button 만들기
# Challenge : Show "Button Got Clicked" on my_label when the button get's clicked.

def button_clicked() : 
    print("I got clicked")
    # Challenge : Title에 input에 넣은 값이 출력되도록
    new_text = input.get()
    my_label["text"] = new_text

button = Button(text = "Click Me", command = button_clicked)
button.pack()

# Entry component : 기본적으로 텍스트를 입력받는 컴포넌트
input = Entry(width=10)
input.pack()

# mainloop() : 윈도우가 스크린에 계속 유지되도록 하는 역할(코드의 맨 마지막에 위치해야 함)
window.mainloop()