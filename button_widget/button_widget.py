import customtkinter

from fonts.project_fonts import ProjectFonts


class ButtonWidget:
    def __init__(self, root=None, on_tap=None, title=None, width=50, corner_radius=10):
        self._root = root
        self._on_tap = on_tap
        self._title = title
        self._width = width
        self._corner_radius = corner_radius
        pass

    def make_button(self):
        return customtkinter.CTkButton(self._root, text=self._title, command=self._on_tap,
                                       corner_radius=self._corner_radius, width=self._width,
                                       font=ProjectFonts.button_font.value)
