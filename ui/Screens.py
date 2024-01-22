from tkinter import ttk
from tkinter import filedialog

from decode import decode
from encode import encode


class HomeScreen(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        ttk.Label(self, text="Выберите действие").grid(column=1, row=0)

        ttk.Button(self, text="Зашифровать", command=lambda: master.switch_frame(EncodeScreen)).grid(
            column=1,
            row=2,
            pady=10
        )
        ttk.Button(self, text="Рисшифровать", command=lambda: master.switch_frame(DecodeScreen)).grid(
            column=1,
            row=4,
        )


class EncodeScreen(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        ttk.Label(self, text="Выберите файл").grid(column=0, row=0, pady=10)
        ttk.Button(self, text="Выбрать файл", command=self.get_open_file_path).grid(column=1, row=0)

        ttk.Button(self, text="Вернуться назад", command= lambda: master.switch_frame(HomeScreen)).grid(
            column=1,
            row=7,
            pady=10
        )

    def get_open_file_path(self):
        open_filepath = filedialog.askopenfilename()
        if open_filepath != "":
            ttk.Label(self, text=f"Выбранный файл: \n {open_filepath}").grid(
                columnspan=3,
                column=0,
                row=1,
                pady=10,
            )

        ttk.Label(self, text="Введите секретное сообщение").grid(
            column=1,
            row=2,
            pady=10,
        )
        message = ttk.Entry(self)
        message.grid(column=1, row=3)

        ttk.Label(self, text="Куда сохранить файл?").grid(
            column=0,
            row=4,
            pady=10,
        )
        ttk.Button(
            self,
            text="Выбрать",
            command=lambda: self.get_save_file_path(open_filepath, message)
        ).grid(
            column=1,
            row=4,
            pady=10,
        )

    def get_save_file_path(self, open_filepath, message):
        save_filepath = filedialog.asksaveasfilename(
            filetypes=(
                ("png files","*.png"),
                ("all files", "*.*")
            )
        )
        ttk.Button(
            self,
            text="Сгенерировать изображение",
            command=lambda: self.generate_img(open_filepath, message, save_filepath)
        ).grid(
            column=1,
            row=5,
            pady=10
        )

    def generate_img(self, open_filepath, message, save_filepath):
        try:
            encode(open_filepath, save_filepath, message.get())
            ttk.Label(self, text="Изображение сгенерировано!").grid(
                column=1,
                row=6,
                pady=10
                )
        except AssertionError:
            ttk.Label(self, text="Вы не ввели сообщение").grid(
                column=1,
                row=6,
                pady=10
            )



class DecodeScreen(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Label(self, text="Выберите файл").grid(column=0, row=0, pady=10)
        ttk.Button(self, text="Выбрать файл", command=self.get_open_file_path).grid(column=1, row=0)

        ttk.Button(self, text="Вернуться назад", command=lambda: master.switch_frame(HomeScreen)).grid(
            column=1,
            row=5,
            pady=10
        )

    def get_open_file_path(self):
        open_filepath = filedialog.askopenfilename()
        if open_filepath != "":
            ttk.Label(self, text=f"Выбранный файл: \n {open_filepath}").grid(
                columnspan=3,
                column=0,
                row=1,
                pady=10,
            )
            ttk.Button(
                self,
                text="Расшифровать",
                command=lambda: self.decode_img(open_filepath)
            ).grid(
                column=1,
                row=2,
            )

    def decode_img(self, file):
        try:
            message = decode(file)
            ttk.Label(self, text=f"Зашифрованное сообщение:").grid(
                column=1,
                row=3,
                pady=10,
            )
            ttk.Label(self, text=message).grid(
                column=1,
                row=4,
            )
        except IndexError:
            ttk.Label(self, text=f"Сообщение не найдено(").grid(
                column=1,
                row=3,
                pady=10,
            )
