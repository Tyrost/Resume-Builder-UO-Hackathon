import tkinter as tk

class Button:
    def __init__(self, root, label="", height=50, width=100, defcolor="black", optcolor=None):
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive numbers")
        self.defcolor = defcolor
        self.optcolor = optcolor
        self.is_pressed = False
        self.button = tk.Button(root, text=label, bg=defcolor, command=self.toggle_button_state)
        self.button.place(width=width, height=height)

    def toggle_button_state(self):
        self.is_pressed = not self.is_pressed
        new_color = self.optcolor if self.is_pressed else self.defcolor
        self.button.configure(bg=new_color)
        print(f"Button is {'pressed' if self.is_pressed else 'not pressed'}")

    def is_button_pressed(self):
        return self.is_pressed

    def click_btn(self, function):
        self.button.config(command=function)
        return self.button

root = tk.Tk()
root.mainloop()
