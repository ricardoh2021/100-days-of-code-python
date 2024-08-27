from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(row=0, column=2)

entry = Entry(width=10)
entry.grid(row=0, column=1)

is_equal_to_label = Label(text="is equal to", font=("Arial", 24))
is_equal_to_label.grid(row=1, column=0)

converted_num_label = Label(text="0", font=("Arial", 24))
converted_num_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(row=1, column=2)


def button_clicked():
    input_miles = int(entry.get())
    km = int(input_miles * 1.60934)
    converted_num_label.config(text=km)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Button


window.mainloop()
