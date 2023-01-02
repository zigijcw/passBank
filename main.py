from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def passgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_entry.delete(0, END)
    nr_letters = random.randint(1, 5)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entries.get()
    email = entry_mail_user.get()
    password_en = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_en,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password_en) == 0:
        messagebox.showerror(title="Oops", message="Please mack su re you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            web_entries.delete(0, END)
            pass_entry.delete(0, END)


def search():
    website = web_entries.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"no info for {website}")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="message mot fund", message=f"no info for {website}")

# ---------------------------- SEARCH FUNCTION ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
mail_user = Label(text="Email/Username:")
mail_user.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
# Entry
web_entries = Entry(width=35)
web_entries.grid(column=1, row=1)
web_entries.focus()
entry_mail_user = Entry(width=35)
entry_mail_user.grid(column=1, row=2, columnspan=2)
entry_mail_user.insert(0, "MyMail@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
# Buttons
search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)
pass_generate_button = Button(text="Generate Password", command=passgen)
pass_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
