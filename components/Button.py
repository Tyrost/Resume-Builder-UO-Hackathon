import tkinter as tk

class Button:
    def __init__(self, root, label="", height=50, width=100, defcolor="black", optcolor=None, command=None):
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive numbers")
        
        self.width = width
        self.height = height
        self.defcolor = defcolor
        self.optcolor = optcolor
        self.is_pressed = False
        self.command = command

        self.button = tk.Button(
            root,
            text=label,
            bg=self.defcolor,
            width=self.width,
            height=self.height,
            command=self.toggle_button_state
        )
        self.button.place(width=width, height=height)

    def toggle_button_state(self):
        """
        Toggles the button state and invokes the user-provided function, if any.
        """
        current_state = "pressed" if self.is_pressed else "not pressed"
        print(f"Button is now {'pressed' if self.is_pressed else 'not pressed'}")

        self.is_pressed = not self.is_pressed
        new_color = self.optcolor if self.is_pressed else self.defcolor
        self.button.configure(bg=new_color)

        if self.command:
            self.command()


    def is_button_pressed(self):
        """
        Check if the button is pressed.
        """
        return self.is_pressed

    def click_btn(self, function):
        """
        Change the command associated with the button.
        """
        self.command = function
        self.button.config(command=self.toggle_button_state)  # Ensure toggle logic remains
        return self.button

    def pack(self, **kwargs):
        """
        Pack the button using the Tkinter pack manager.
        """
        self.button.pack(**kwargs)
    
    def place(self, **kwargs):
        """
        Place the button using the Tkinter place manager.
        """
        self.button.place(**kwargs)
