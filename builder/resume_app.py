import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import components.intit_components
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

def create_output_box(frame, width=50, height=10, font= ("Arial", 14)):
    output_box = tk.Text(frame, width=width, height=height)
    output_box.pack()
    return output_box


# _______ Encapsulation _______ #

def on_button_click1(output_box):
    output_box.insert(tk.END, "10\n")

#def on_button_click2(output_box):
    #output_box.insert(tk.END, "9\n")



def create_app_window():
    WINDOW = tk.Tk()
    
    builder_frame = create_window(WINDOW, window_name='builder_frame')
    img_label, text_editor = create_elements(WINDOW, builder_frame)

    upload_label = create_label(builder_frame, text='Your Resume', font = ('Lexend', 30))
    #description_label = create_label(builder_frame, text='Put your job description here!')
    build_generate_button = create_button(builder_frame, text= "Generate Questions", height = 60, width = 120, defcolor = "red")
    generate_label = create_label(builder_frame, text="Generates questions based off weaknesses in Resume",font = ('Lexend', 15))
    build_rating_button = create_button(builder_frame, text="Rate Resume", height=60, width=120, defcolor='red')
    #text_box = create_textbox(builder_frame, placeholder_text='Input information for Resume', width='100', height='10', font = ("Arial", 14))
    rate_label = create_label(builder_frame, text="Gives your resume a rating on a scale of 1-10", font = ('Lexend', 15))
    output_rate_box = create_output_box(builder_frame, width=5, height=2)
    output_generate_box = create_output_box(builder_frame, width=60, height=40)
    textbox_label = create_label(builder_frame, text="Input Job Description Here", font = ('Lexend', 15))
    #Button Output
    build_rating_button.click_btn(lambda:on_button_click1(output_rate_box))
    #build_generate_button.click_btn(lambda:on_button_click2(output_generate_box))
    

    
    # Placement
    img_label.place(x=450, y = 50)
    generate_label.place(x=5, y=20)
    text_editor.place(x=150, y= 600)
    build_generate_button.place(x=50, y = 50)
    build_rating_button.place(x=50,y=150)
    rate_label.place(x=5,y=120)
    textbox_label.place(x=150,y=570)
    #text_box.place(x=100,y=100)
    output_rate_box.place(x=200, y=160)
    output_generate_box.place(x=800,y=50)
    

    #description_label.place(x=80, y = 500)

    #Right Frame  
    
    # Start the main loop
    WINDOW.mainloop()

create_builder_window()