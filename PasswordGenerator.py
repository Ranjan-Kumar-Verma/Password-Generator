# Import the required Libraries
from tkinter import *
from tkinter import ttk
import string
import random
import pyperclip

# Master window
root = Tk()
Master = Toplevel()
root.withdraw()
# Master.withdraw()

# All usernames and passwords for using password generator
user = [["ranjan", "Ranjan@123"],
        ["kumar", "Kumar@123"], ["verma", "Verma@123"]]

# Set the geometry of Tkinter frame
Master.geometry("450x250")
root.geometry("450x250")

# Function to validate login
def validate():
    print("Function called ")
    for n in range(len(user)):
        global authentication
        if username_input.get() == user[n][0] and password_input.get() == user[n][1]:
            authentication = "valid"
            # print("Valid User")
            break

    if authentication == "valid":
        Master.withdraw()
        root.deiconify()

# Title Label
title = Label(Master, text="Verma Password Generator",
              font=("Courier 22 bold"))
title.grid(row=0, column=0, columnspan=2, pady=5, padx=10)

# Title of the window
Master.title("Verma Password Generator")
root.title("Verma Password Generator")

# Username
Label(Master, text="Username: ", font=("Courier 15")).grid(row=1, column=0, padx=10, pady=5)
username_input = Entry(Master, width=40)
username_input.focus_set()
username_input.grid(row=1, column=1)

# Password Entry
Label(Master, text="Password: ", font=("Courier 15")).grid(row=2, column=0)
password_input = Entry(Master, width=40)
password_input.grid(row=2, column=1)

# Validate Button
validate_btn = Button(Master, text="Log In",
                      command=validate, font=("Courier 15"))
validate_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=15)


# Root window
root_title = Label(root, text="Verma Password Generator",
                   font=("Courier 22 bold"))
root_title.grid(row=0, column=0, columnspan=2, pady=5, padx=10)

# Function of root window

# Function to generate new password
def generate():
    list = string.ascii_letters + string.digits
    global login_password

    # print(login_username.get(), website.get(), int(Password_length_string.get()))
    length = int(Password_length_string.get())
    login_password = "".join(random.choices(list, k=length))
    # print(login_password)
    Label(root, text="Password: ", font=("Courier 15")).grid(
        row=5, column=0, sticky='w')
    Password_display = Label(root, text=login_password, font=("Courier 15"))
    Password_display.grid(row=5, column=1, sticky='w')


# Function to copy password to clipboard
def copy():
    pyperclip.copy(login_password)
    paste_password = pyperclip.paste()


global count
count = 0

# Function to save the Username, Website and Password in a list
def save():
    user_accounts = []
    user_accounts.append([login_username.get(), website.get(), login_password])
    print(user_accounts)

# Login username of website
Label(root, text="Login Username: ", font=("Courier 15")).grid(row=1, column=0, padx=10, pady=5, sticky="w")
login_username = Entry(root, width=40)
login_username.focus_set()
login_username.grid(row=1, column=1)

# Website
Label(root, text="Website: ", font=("Courier 15")).grid(row=2, column=0, sticky="w", padx=10, pady=5)
website = Entry(root, width=40)
website.grid(row=2, column=1)

# Password Length
Label(root, text="Password Length: ", font=("Courier 15")).grid(row=3, column=0, sticky="w", padx=10, pady=5)
Password_length_string = StringVar()
Password_length = Entry(root, width=40, textvariable=Password_length_string)
Password_length.grid(row=3, column=1)

# Generate button
generate_btn = Button(root, text="Generate Password",
                      command=lambda: generate(), font=("Courier 15"))
generate_btn.grid(row=4, column=0, padx=10, pady=5, sticky='w')

# Copy button
copy_btn = Button(root, text="Copy",
                  command=lambda: copy(), font=("Courier 15"))
copy_btn.grid(row=4, column=1, padx=5, pady=5, sticky='w')

#Save button
save_btn = Button(root, text="Save",
                  command=lambda: save(), font=("Courier 15"))
save_btn.grid(row=4, column=1, padx=5, pady=5, sticky='e')


Master.mainloop()
