import customtkinter


class ScreenFrame:

    def __init__(self, root=None, geometry="500x500", title=None, padx=50, pady=50, theme_mode="dark"):
        self._tkinter_obj = root
        self._geometry = geometry
        self._title = title
        self._padx = padx
        self._pady = pady
        self._theme_mode = theme_mode

    def show_frame(self):
        self._tkinter_obj.geometry(self._geometry)
        self._tkinter_obj.title(self._title)
        self._tkinter_obj.config(padx=self._padx, pady=self._pady)
        customtkinter.set_appearance_mode(self._theme_mode)
