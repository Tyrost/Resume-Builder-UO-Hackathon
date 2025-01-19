import tkinter as tk

class SystemOutputBox(tk.Text):
    """
    A read-only Text widget that the system can write to.
    """
    def __init__(self, parent, initial_text="", width=80, height=5, font=("Arial", 12), **kwargs):
        super().__init__(parent, width=width, height=height, font=font, **kwargs)
        
        self.insert(tk.END, initial_text)
        self.config(state="disabled")

    def set_text(self, new_text):

        if not isinstance(new_text, str):
            raise ValueError("set_text only accepts a string input.")

        self.config(state="normal")
        
        self.delete("1.0", tk.END)
        self.insert(tk.END, new_text)
        
        # Make it read-only again
        self.config(state="disabled")
