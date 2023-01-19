from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# 화면 가장자리에 여유자리를 넣고 싶다면?
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# 만약 정확한 위치에 Label을 위치시키고 싶다면? place() 사용
# my_label.place(x=100,y=200)
# 하지만, place는 정확한 위치를 정의해야 한다는 점에서 불편함 초래. -> grid 사용(다만, grid는 pack과 함께 사용 불가)
my_label.grid(column=0, row=0)
# 특정 위젯에서 가장자리에 여유자리를 넣고 싶다면?(위젯 주변 여유자리)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()