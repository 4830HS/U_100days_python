from tkinter import *

# 1mile = 1.609344km

def result() :
    new_result = Label(text="result", font=("Arial",20))
    mile = float(input.get())
    km = round(mile*1.609344,2)
    new_result.config(text = km)
    new_result.grid(column=1, row=1)

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label_1
label_1 = Label(text="Miles", font=("Arial",24,"bold"))
label_1.config(text="Miles")
label_1.grid(column=2, row=0)
label_1.config(padx=10, pady=10)

# Label_2
label_2 = Label(text="is equal to", font=("Arial", 20, "bold"))
label_2.config(text="is equal to")
label_2.grid(column=0, row=1)

# Label_3
label_3 = Label(text="Km", font=("Arial", 20, "bold"))
label_3.config(text="Km")
label_3.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=result)
button.config(text="Calculate")
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()