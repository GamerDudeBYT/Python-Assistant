import tkinter as tk

class DragManager():
    widgets = {}

    def add_dragable_widget(self, widget):
        self.widget = widget
        self.widget.update_idletasks()
        self.norm_height = self.widget.winfo_height()
        self.big_height = self.norm_height + 15

        self.norm_width = self.widget.winfo_width()

        self.widget.bind("<Button-1>", self.drag_start)
        self.widget.bind("<B1-Motion>", self.drag_motion)
        self.widget.bind("<ButtonRelease>", self.drag_stop)

        self.widget.pack_propagate(False)

        self.widgets.update({self.widget: self.widget["bg"]})

        self.widget.config(cursor="hand1", width=self.norm_width, height=self.big_height, bg="red")

        #print(f"[DragManager] Added widget {widget.__class__.__name__}")

    def remove_dragable_widget(self, widget):
        self.widget = widget
        
        self.widget.unbind("<Button-1>")
        self.widget.unbind("<B1-Motion>")
        self.widget.unbind("<ButtonRelease>")
        self.widget.config(cursor="")

        self.widget.pack_propagate(True)
        self.widget.config(bg=self.widgets[self.widget])

        #print(f"[DragManager] Removed widget {widget.__class__.__name__}")

    def drag_start(self, event):
        self.widget._drag_start_x = event.x
        self.widget._drag_start_y = event.y

    def drag_motion(self, event):
        x = self.widget.winfo_x() - self.widget._drag_start_x + event.x
        y = self.widget.winfo_y() - self.widget._drag_start_y + event.y
        self.widget.place(x=x, y=y)

    def drag_stop(self, event):
        self.widget.controller.save_widgets()
