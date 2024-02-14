import customtkinter

from fonts.project_fonts import ProjectFonts


class EntryWidget:

    def __init__(self, root=None, hint_text="Type here", width=50):
        self._root = root
        self._hint_text = hint_text
        self._width = width

    def make_entry(self):
        return customtkinter.CTkEntry(self._root, placeholder_text=self._hint_text, width=self._width,
                                      font=ProjectFonts.entry_font.value)

    def place_entry_grid(self, row=None, column=None, columnspan=1):
        entry = self.make_entry()
        entry.grid(row=row, column=column, columnspan=columnspan)
