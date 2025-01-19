import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import components.init_components
from components.main import create_window
import tkinter as tk
from PIL import Image, ImageTk
from components.TextEditor import TextEditor
from components.Button import Button

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

def create_button(frame, text="Click Me", height=2, width=10, defcolor="black", optcolor="green"):
    button = Button(frame, label=text, height=height, width=width, defcolor=defcolor, optcolor=optcolor)
    return button

def create_textbox(window, placeholder_text='Input information for Resume', width='100', height='10', font = ("Arial", 14)):
    editor = TextEditor(window, placeholder_text, width, height, font="white") # MISSING FONT
    editor.pack()
    return editor

def create_elements(window, frame):
    null, img_label = create_image(frame)
    # button = create_button(frame)
    editor = create_textbox(window)
    
    return img_label, editor

# _______ Encapsulation _______ #

def create_builder_window():
    WINDOW = tk.Tk()
    
    builder_frame = create_window(WINDOW, window_name='builder_frame')
    img_label, text_editor = create_elements(WINDOW, builder_frame)

    upload_label = create_label(builder_frame, text='Your Resume!')
    #description_label = create_label(builder_frame, text='Put your job description here!')
    build_generate_button = create_button(builder_frame, text= "Generate Questions", height = 60, width = 120, defcolor = "red")

    build_rating_button = create_button(builder_frame, text="Rate Resume", height=60, width=120, defcolor='red')
    

    
    # Placement
    img_label.place(x=400, y = 50)
    text_editor.place(x=150, y= 600)
    build_generate_button.place(x=50, y = 50)
    build_rating_button.place(x=50,y=150)
    

    #description_label.place(x=80, y = 500)

    #Right Frame  
    
    # Start the main loop
    WINDOW.mainloop()

create_builder_window()