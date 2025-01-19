import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.intit_components import *
from components.main import create_window
import tkinter as tk
# from PIL import Image, ImageTk
# from components.TextEditor import TextEditor
# from components.Button import Button
 
# _______ Encapsulation _______ #

def create_checker_window():
    WINDOW = tk.Tk()
    
    checker_frame = create_window(WINDOW, window_name='checker_frame')
    img_label, text_editor = create_elements(WINDOW, checker_frame)
    
    upload_btn = create_button(checker_frame, "Upload")
    check_btn = create_button(checker_frame, "Check Now!")
    
    upload_label = create_label(checker_frame, text='Upload your resume here!')
    description_label = create_label(checker_frame, text='Put your job description here!')
    
    # Placement
    
    upload_btn.place(x=50, y=300)
    check_btn.place(x=600, y = 50)
    
    img_label.place(x=400, y = 50)
    text_editor.place(x=50, y= 450)
    
    upload_label.place(x=80, y=200)
    description_label.place(x=80, y = 400)
    
    # Start the main loop
    WINDOW.mainloop()

create_checker_window()