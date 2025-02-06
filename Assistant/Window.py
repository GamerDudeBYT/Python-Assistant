import tkinter as tk
from Tooltip import CreateToolTip
from Widget import Widget
import tkinter.messagebox
from DragManager import DragManager

class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        title = "Ethan's Homemade Assistant"
        self.title(title)

        #self.attributes("-fullscreen", True)
        self.state("zoomed")

        self.attributes("-topmost", True)

        self.tp_colour = "#ffa8e5"

        self.attributes("-transparentcolor", self.tp_colour)

        self.config(bg=self.tp_colour)

        self.drag_enabled = False

        self.lift()

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.container = tk.Frame(self, bg=self.tp_colour)
        self.container.pack(fill="both", expand=True)

    def initialise_widgets(self):
        loaded_locations = {}
        with open('locations.txt', 'r') as f:
            for line in f:
                formatted_line = line.rstrip()
                loaded_locations.update({formatted_line.split(":")[0]: formatted_line.split(":")[1]})
        print(loaded_locations)
        for i in Widget.instances:
            if not isinstance(i, Widget): continue
            name = i.__class__.__name__

            if name in list(loaded_locations.keys()):
                i.place(x=loaded_locations[name].split(',')[0], y=loaded_locations[name].split(',')[1])
                print(f"Using saved location {loaded_locations[name].split(',')} for {name}")
            else:
                print(f"No Saved location found for {name}")
                i.place(i.placeoptions)

            CreateToolTip(i, name)

    def save_widgets(self):
        savelocations = []

        for child in self.container.winfo_children():
            if not isinstance(child, Widget): continue
            savelocations.append(f"{child.__class__.__name__}:{child.winfo_rootx()},{child.winfo_rooty()}")
            print(f"{child.__class__.__name__}:{child.winfo_rootx()},{child.winfo_rooty()}")
        
        with open('locations.txt', 'w') as f:
            for loc in savelocations:
                f.write(f"{loc}\n")
        print("Saved Locations")

    def override_widget_location(self):
        for child in self.container.winfo_children():
            if not isinstance(child, Widget): continue
            child.place(child.placeoptions)

    def move_widgets_mode(self, move):
        if move:
            if self.drag_enabled == True:
                return
            self.drag_enabled = True
            self.container.config(bg="white")
            for child in self.container.winfo_children():
                child.update()
                if not isinstance(child, Widget): continue
                DragManager().add_dragable_widget(child)
            tkinter.messagebox.showinfo(title="Move Widgets Enabled", message="Click and drag the red bars to move the widgets.")
        else:
            self.drag_enabled = False
            self.container.config(bg=self.tp_colour)
            for child in self.container.winfo_children():
                child.update()
                if not isinstance(child, Widget): continue
                DragManager().remove_dragable_widget(child)