import customtkinter

from fonts.project_fonts import ProjectFonts


class LabelWidget:

    def __init__(self, root=None, title=None, text_color="black"):
        self._root = root
        self._title = title
        self._text_color = text_color

    def make_label(self):
        return customtkinter.CTkLabel(self._root, text=self._title, fg_color="transparent",
                                      text_color=self._text_color, font=ProjectFonts.label_font.value)

    def place_label_grid(self, row=None, column=None):
        label = self.make_label()
        label.grid(row=row, column=column)
        label.configure(padx=15, pady=15)
