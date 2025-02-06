import tkinter as tk

class Widget(tk.Frame):
    instances = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Widget.instances.append(self)
        self.parent = parent
        self.controller = controller