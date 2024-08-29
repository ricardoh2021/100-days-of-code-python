from tkinter import *
from tkinter import messagebox
import random
import pyperclip


WHITE = "#FFFFFF"
FONT_NAME = "Arial"
BLUE = "#0000FF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():

    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list = [random.choice(letters) for char in range(nr_letters)]


    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("Hello world")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                           f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(f"{website.ljust(20)} | {email.ljust(20)} | {password.ljust(20)}\n")

        # Delete entries from tkinter
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=(FONT_NAME, 15), bg=WHITE, fg="black")
website_label.grid(row=1, column=0)

website_entry = Entry(width=39, fg="black",bg="white", highlightthickness=1)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username: ", font=(FONT_NAME, 15), bg=WHITE, fg="black")
email_label.grid(row=2, column=0)

email_entry = Entry(width=39, fg="black",bg="white", highlightthickness=1)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"example@gmail.com")

password_label = Label(text="Password: ", font=(FONT_NAME, 15), bg=WHITE, fg="black")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21, bg=WHITE, fg="black",highlightthickness=1)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", highlightbackground=WHITE, command=gen_password)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightbackground=WHITE, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
