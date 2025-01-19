import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.main import create_window
import tkinter as tk
from PIL import Image, ImageTk
from components.TextEditor import TextEditor

# _______ Element Creation _______ #

def create_image(frame: tk.Frame, width = 300, height = 400):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    image_path = os.path.join(project_root, "components", "images", "sample_resume1.png")

    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    image = ImageTk.PhotoImage(resized_image)

    image_label = tk.Label(frame, image=image)
    image_label.pack()

    frame.image = image
    return image, image_label

def create_label(frame, text = "", font = ('Lexend', 15)):
    label = tk.Label(frame, text=text, font=font)
    label.pack()
    
    return label

def create_button(frame):
    pass

def create_textbox(window, placeholder_text='Job description:', width='50', height='20', font = ("Arial", 14)):
    editor = TextEditor(window, placeholder_text, width, height, font) # MISSING FONT
    editor.pack()
    return editor

def create_elements(window, frame):
    null, img_label = create_image(frame)
    # button = create_button(frame)
    editor = create_textbox(window)
    
    return img_label, editor

# _______ Encapsulation _______ #

def create_checker_window():
    WINDOW = tk.Tk()
    
    checker_frame = create_window(WINDOW, window_name='checker_frame')
    img_label, text_editor = create_elements(WINDOW, checker_frame)
    
    upload_label = create_label(checker_frame, text='Upload your resume here!')
    description_label = create_label(checker_frame, text='Put your job description here!')
    
    # Placement
    
    img_label.place(x=400, y = 50)
    text_editor.place(x=50, y= 450)
    
    description_label.place(x=80, y = 400)
    
    

    
    # Start the main loop
    WINDOW.mainloop()

create_checker_window()