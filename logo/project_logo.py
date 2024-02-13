import customtkinter
from PIL import Image


class ProjectLogo:
    _key_lock_image = "assets/key.png"

    def __init__(self):
        

    def show_logo(self, root):
        image = customtkinter.CTkImage(light_image=Image.open(ProjectLogo._key_lock_image), size=(150, 150))
        image_label = customtkinter.CTkLabel(root, image=image, text='')
        image_label.grid(row=0, column=1, ipady=20)
