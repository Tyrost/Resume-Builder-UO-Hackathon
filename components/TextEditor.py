import tkinter as tk

class TextEditor:
    '''
    A custom Text Editor class with placeholder text functionality and event handling.

    This class creates a text editor widget using Tkinter that includes a placeholder\n
    text feature. The placeholder text appears in the editor until the user focuses\n
    on the widget, at which point the placeholder is removed. If the user unfocuses\n
    the widget without entering any text, the placeholder reappears.

    Attributes:
        window (tk.Tk or tk.Frame): The parent window or frame where the text editor is placed.
        placeholder_text (str): The placeholder text that appears when the editor is empty.
        font (tuple): The font style and size for the text editor.
        current_text (str): The current text content of the editor, excluding the placeholder.
        text_editor (tk.Text): The Tkinter Text widget used as the text editor.
    '''
    def __init__(self, window, placeholder_text, width, height, font):

        self.window:tk.Tk = window
        self.placeholder_text = placeholder_text
        self.current_text = ''
        
        self.text_editor = tk.Text(window, font=font, width=width, height=height, wrap='word')
        
        self.text_editor.insert('1.0', placeholder_text)
        self.text_editor.config(fg='grey')
        
        self.text_editor.bind('<FocusIn>', self.__remove_placeholder)
        self.text_editor.bind('<FocusOut>', self.__add_placeholder)
        self.text_editor.bind('<Return>', self.__return_pressed)
        self.text_editor.bind('<Escape>', self.__escape_pressed)

    def pack(self, **kwargs):
        self.text_editor.pack(**kwargs)

    def place(self, **kwargs):
        self.text_editor.place(**kwargs)

    def get_text(self):
        return self.current_text
    
    # Discrete Methods__
    
    def __show_temporary_placeholder(self, temp_text):
        self.text_editor.delete('1.0', 'end')
        self.text_editor.insert('1.0', temp_text)
        self.text_editor.config(fg='grey')
        
        def reset_placeholder():
            self.text_editor.delete('1.0', 'end')
            self.text_editor.insert('1.0', self.placeholder_text)
            self.text_editor.config(fg='grey')
        
        self.window.after(5000, reset_placeholder)
        
    def __stop_editing(self):
        self.text_editor.config(state='disabled')
        self.window.focus_set()
        
        def enable_editing():
            self.text_editor.config(state='normal')
        
        self.window.after(100, enable_editing) 
        
    def __return_pressed(self, event):
        current_text = self.text_editor.get('1.0', 'end-1c').strip()
        if current_text and current_text != self.placeholder_text:
            print(f"Text Submitted: {current_text}")
            self.current_text = current_text
            self.__show_temporary_placeholder(f"{self.placeholder_text.split()[0]} Set")
        self.__stop_editing()
        return 'break'
    
    # Attribute modifiers
    
    def __remove_placeholder(self, event):
        if self.text_editor.get('1.0', 'end-1c') == self.placeholder_text:
            self.text_editor.delete('1.0', 'end')
            self.text_editor.config(fg='white')
    
    def __add_placeholder(self, event):
        if not self.text_editor.get('1.0', 'end-1c'):
            self.text_editor.insert('1.0', self.placeholder_text)
            self.text_editor.config(fg='grey')
    
    def __escape_pressed(self, event):
        self.text_editor.delete('1.0', 'end')
        self.text_editor.insert('1.0', self.placeholder_text)
        self.text_editor.config(fg='grey')
        
        return 'break'
    
    def update_current_text(self, event):
        self.current_text = self.text_editor.get('1.0', 'end-1c').strip()
        if self.current_text == self.placeholder_text:
            self.current_text = ''
            
    def get(self):
        """
        Retrieve the current text from the TextEditor, excluding the placeholder.

        Returns:
            str: The current text content of the editor. If the placeholder is present,
                an empty string is returned.
        """
        content = self.text_editor.get('1.0', 'end-1c').strip()  # Get text from the Text widget
        if content == self.placeholder_text:  # Return an empty string if placeholder is present
            return ''
        return content
    
    def bind(self, sequence, callback):
        self.text_editor.bind(sequence, callback)
        
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Return>", self.handle_enter)

    def handle_enter(self, event=None):
        print("Custom Enter key behavior!")  # Replace with your logic
        return 'break'  # Prevent default action