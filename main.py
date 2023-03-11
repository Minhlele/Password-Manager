from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
MY_EMAIL = "my_email@gmail.com"
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range (nr_letters) ]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas  = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(row=0,column=1)



website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0)

username_entry = Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,MY_EMAIL)

password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

def clear_text():
    website_entry.delete(0,END)
    password_entry.delete(0,END)

def add_password():
    entered_website = website_entry.get()
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    str_to_save = f"{entered_website} | {entered_username} | {entered_password} \n"

    if len(entered_website) == 0 or len(entered_password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=entered_website,
                                       message=f"These are the details entered: \nEmail: {entered_username}\nPassword: {entered_password}\n Is it ok to save?")
        if is_ok:
            user_file = open("data.txt","a")
            user_file.write(str_to_save)
            user_file.close()
            clear_text()



add_pass_button = Button(text="Add",command=add_password,width=36)
add_pass_button.grid(row=4,column=1,columnspan=2)
window.mainloop()