import customtkinter as tk
from PIL import Image


class ProjectLogo:
    def __init__(self, tkinter_obj=None, image_path=None, height=150, width=150, row=0, column=1):
        # Check if tkinter_obj is a valid tkinter object
        if tkinter_obj is not None and not isinstance(tkinter_obj, tk.CTk):
            raise ValueError("tkinter_obj must be a valid Tkinter object")

        # Check if my_string is a string
        if image_path is not None and not isinstance(image_path, str):
            raise ValueError("my_string must be a string")

        # Assign values to the instance variables
        self.tkinter_obj = tkinter_obj
        self.image_path = image_path
        self.height = height
        self.width = width
        self.row = row
        self.column = column

    def show_logo(self):
        image = tk.CTkImage(light_image=Image.open(self.image_path), size=(self.height, self.width))
        image_label = tk.CTkLabel(self.tkinter_obj, image=image, text='')
        image_label.grid(row=self.row, column=self.column, ipady=20)
