from random import choice, randint, shuffle
import pyperclip


class GeneratePassword:
    _letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u',
                'v',
                'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q',
                'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    _numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    _symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self, password_field=None):
        self._password_field = password_field

    def generate(self):
        password_letters = [choice(self._letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(self._symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(self._numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers

        shuffle(password_list)

        password = "".join(password_list)

        self._password_field.insert(0, password)
        pyperclip.copy(password)
