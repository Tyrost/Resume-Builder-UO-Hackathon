import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.main import create_window
import tkinter as tk

def create_checker_window():
    WINDOW = tk.Tk()
    
    checker_frame = create_window(WINDOW, window_name='checker_frame')
    
    image = tk.PhotoImage(file="/Users/danielcorzo/Documents/Github/Resume-Builder-UO-Hackathon/components/images/sample_resume1.png")
    image_label = tk.Label(checker_frame, image=image)
    
    image_label.pack(pady=20)
    
    WINDOW.mainloop()
    
create_checker_window()