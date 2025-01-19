import tkinter as tk

class SystemOutputBox(tk.Text):
    """
    A read-only Text widget that the system (your code) can write to.
    """
    def __init__(self, parent, initial_text="", width=80, height=5, font=("Arial", 12), **kwargs):
        super().__init__(parent, width=width, height=height, font=font, **kwargs)
        
        # Insert initial text (if any) and make widget read-only.
        self.insert(tk.END, initial_text)
        self.config(state="disabled")

    def set_text(self, new_text):
        """
        Replace the entire text with `new_text`, keeping the widget read-only.
        """
        # Temporarily make it writable.
        self.config(state="normal")
        
        # Clear previous content, insert new text
        self.delete("1.0", tk.END)
        self.insert(tk.END, new_text)
        
        # Make it read-only again
        self.config(state="disabled")

    def append_text(self, additional_text):
        """
        Append text at the end (e.g. for logs).
        """
        self.config(state="normal")
        
        # Move to end and insert the new text
        self.insert(tk.END, additional_text)
        
        self.config(state="disabled")
