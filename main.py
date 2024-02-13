from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import customtkinter
from PIL import Image
from logo import project_logo
from logo.project_logo import ProjectLogo


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.cget("text")
    email = email_entry.cget("text")
    password = password_entry.cget("text")

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window = Tk()
app = customtkinter.CTk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)
app.geometry("500x500")
app.title("Password Manager")
app.config(padx=50, pady=50)
customtkinter.set_appearance_mode("dark")
app.configure(background="pink")

# key_lock_image = "assets/key.png"
# image = customtkinter.CTkImage(light_image=Image.open(key_lock_image), size=(150, 150))
# image_label = customtkinter.CTkLabel(app, image=image, text='')
# image_label.grid(row=0, column=1, sticky=S, ipady=20)
logo_obj = ProjectLogo()
logo_obj.showLogo()


# labels
label_font = customtkinter.CTkFont(family="Montserrat", size=14, weight="bold")
website_label = customtkinter.CTkLabel(app, text="Website:", fg_color="transparent",text_color="teal",font=label_font)
website_label.grid(row=1, column=0)
email_label = customtkinter.CTkLabel(app, text="Email:", fg_color="transparent",text_color="teal",font=label_font)
email_label.grid(row=2, column=0)
password_label = customtkinter.CTkLabel(app, text="Password:", fg_color="transparent",text_color="teal",font=label_font)
password_label.grid(row=3, column=0)

# Entries
# website_entry = Entry(width=35)
website_entry = customtkinter.CTkEntry(app, placeholder_text="Type website here",width=250,font=("Noto Sans",12))
website_entry.grid(row=1, column=1, columnspan=2)

# website_entry.focus()

email_entry = customtkinter.CTkEntry(app, placeholder_text="Type email here",width=250,font=("Noto Sans",12))

email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@gmail.com")

password_entry = customtkinter.CTkEntry(app, placeholder_text="Type password here",width=250,font=("Noto Sans",12))

password_entry.grid(row=3, column=1)

# Buttons
button_text_font = customtkinter.CTkFont(family="Noto Sans", size=14, weight="bold")
generate_password_button = customtkinter.CTkButton(app, text="Generate", command=generate_password, corner_radius=12, width=50, font=button_text_font)
# generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=3)
add_button = customtkinter.CTkButton(app, text="Add", command=save, corner_radius=12, font=button_text_font)
add_button.grid(row=4, column=1, columnspan=2)

app.mainloop()
