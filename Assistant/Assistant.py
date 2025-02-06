import tkinter as tk
from Widget import Widget
import Window

from datetime import datetime


class time_widget(Widget):
    def __init__(self, parent, controller):
        Widget.__init__(self, parent, controller)
        self.placeoptions = {"x": 0, "y": 10}

        self.config(bg="green")

        self.time_label = tk.Label(self, text="nothing right now")
        self.time_label.pack()

        self.set_time_label()

    def set_time_label(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        self.time_label.config(text=date_time)

        self.after(500, self.set_time_label)

class override_widget(Widget):
    def __init__(self, parent, controller):
        Widget.__init__(self, parent, controller)
        self.placeoptions = {"x": 100, "y": 10}

        self.config(bg="blue")

        overridebtn = tk.Button(self, text="Override Locations", command=controller.override_widget_location).pack()

assistant = Window.window()

time_widget(assistant.container, assistant)
override_widget(assistant.container, assistant)

assistant.menubar.add_command(label="Move Widgets True", command=lambda:assistant.move_widgets_mode(True))
assistant.menubar.add_command(label="Move Widgets False", command=lambda:assistant.move_widgets_mode(False))

assistant.initialise_widgets()

assistant.mainloop()