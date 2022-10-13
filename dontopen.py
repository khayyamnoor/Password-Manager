from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters = int(input("How many letters would you like in your password?\n"))
    # nr_symbols = int(input("How many symbols would you like?\n"))
    # nr_numbers = int(input("How many numbers would you like?\n"))

    password = []
    for item in range(1, 3 + 1):
        password.append(random.choice(letters))
    for item in range(1, 3 + 1):
        password.append(random.choice(symbols))
    for item in range(1, 3 + 1):
        password.append(random.choice(numbers))
    random.shuffle(password)
    password_entry.insert(0,password)
# copying the password to the clipboard
# cannot import pyperclip



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    my_dict = {
        website:
            {"Email": email, "Password": password}
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("OOPS", "Warning\nFill All Fields")


    else:
        with open("data.json") as file_data:
            data = json.load(file_data)
            data.update(my_dict)
        with open("data.json", "w") as file_data:
            json.dump(my_dict, file_data, indent=4)
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=40)
email_entry.insert(0, "admin@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
