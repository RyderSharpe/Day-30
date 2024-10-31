import random
from tkinter import *
from datetime import datetime
from tkinter import messagebox
import random
import json
import string

# CONSTANTS
# colors
DARK_PURPLE = "#522258"
LIGHT_PURPLE = "#8C3061"
RED = "#C63C51"
ORANGE = "#D95F59"
LOCK_COLOR = "#d4483b"
BLACK = "#000000"
# size
SCREEN_LENGTH_X = 200
SCREEN_LENGTH_Y = 200
FONT = ('Helvetica', 12)
BOLD_FONT = ('Helvetica', 10, "bold")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# # Combined list (all characters)
# all_characters = uppercase_alphabet + lowercase_alphabet + symbols + numbers

# ---------------------------- EXIT  ------------------------------- #
def exit_application():
    sure = messagebox.askokcancel(title="You sure?", message=f"Are you sure you want to exit the program?")
    if sure:
        window.destroy()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # # Takes random choices from ascii_letters and digits
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [
        *([random.choice(letters) for i in range(nr_letters)]),
        *([random.choice(symbols) for i in range(nr_symbols)]),
        *([random.choice(numbers) for i in range(nr_numbers)]),
    ]

    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def on_after():
    global saved_label
    saved_label.configure(text="")


def saved():
    global saved_label

    # Get form data
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    # Validate form data
    if not website or not email or not password:
        messagebox.showerror(title="ERROR", message="Please fill in all fields.")
        return

    # Message box
    # messagebox.showinfo(title="x", message="poo")
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \n\nWebsite:{website}\n\nEmail:{email} \n\nPassword:{password} \n\nWould you like to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except:  # (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            # Clear form fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        # Saved label timed
        saved_label = Label(text="Saved! ☻", font=('Helvetica', 25, "bold"), bg=LIGHT_PURPLE, fg=ORANGE)
        saved_label.grid(column=0, row=0, sticky="n")
        saved_label.after(1000, on_after)  # start timer after "Add" button is pressed


# ---------------------------- SEARCH ------------------------------- #
def search():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

    searching = website_entry.get()
    try:
        your_password = data[searching]["password"]
        okay = messagebox.askokcancel(title=f"Here you go",message=f"Website: {searching} \nPassword: {your_password}")
        if okay:
            window.destroy()
    except KeyError:
        messagebox.showerror(title=f"Website not found", message=f"Website: {searching} does not exist")


# ---------------------------- SEARCH CLASS VERSION------------------------------- #
# def find_password():
#     website = website_entry.get()
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No Data File Found.")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
#         else:
#             messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=LIGHT_PURPLE)

# LOGO Image
canvas = Canvas(width=200, height=200, bg=LIGHT_PURPLE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=(FONT), bg=LIGHT_PURPLE)
website_label.grid(column=0, row=1, sticky="e")
email_username_label = Label(text="Email/Username:", font=(FONT), bg=LIGHT_PURPLE)
email_username_label.grid(column=0, row=2, sticky="e")
password_label = Label(text="Password:", font=(FONT), bg=LIGHT_PURPLE)
password_label.grid(column=0, row=3, sticky="e")

# Entries
website_entry = Entry(font=(FONT), width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_username_entry = Entry(font=(FONT), width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_username_entry.insert(0, "rydersharpe@gmail.com")

password_entry = Entry(font=(FONT), width=21)  # show='*',
password_entry.grid(column=1, row=3, sticky="w")

# Buttons

search_button = Button(text="Search", highlightthickness=0, width=16, command=search)
search_button.grid(column=2, row=1, sticky="w")

generate_password_button = Button(text="Generate Password", highlightthickness=0, width=16, command=password_generator)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", highlightthickness=0, width=45, command=saved)
add_button.grid(column=1, row=4, columnspan=2)

exit_button = Button(text="Exit", font=(BOLD_FONT), width=10, height=2, fg=BLACK, bg=LOCK_COLOR,
                     command=exit_application)
exit_button.grid(column=2, row=0)

window.mainloop()
