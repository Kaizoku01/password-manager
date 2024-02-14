from tkinter import messagebox
from tkinter.constants import END


class SavePassword:
    def __init__(self, website_field=None, email_field=None, password_field=None):
        self._website_field = website_field
        self._email_field = email_field
        self._password_field = password_field

    def save(self):
        website = self._website_field.get()
        email = self._email_field.get()
        password = self._password_field.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                                  f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    self._website_field.delete(0, END)
                    self._password_field.delete(0, END)
