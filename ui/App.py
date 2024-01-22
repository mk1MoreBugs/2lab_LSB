from tkinter import ttk
from tkinter import Tk

from ui.Screens import HomeScreen


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.style = ttk.Style()
        ttk.Style().configure(
            "TButton",
            padding=6,
            relief="flat",
            background="#ccc",
            font="system"
        )
        ttk.Style().configure(
            "TLabel",
            padding=6,
            relief="flat",
            font="system"
        )

        self.title("Least Significant Bit")
        self.geometry('700x500')
        self._frame = None
        self.switch_frame(HomeScreen)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(pady=10)
