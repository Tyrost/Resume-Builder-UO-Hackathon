from components.main import create_window
import tkinter as tk

def create_checker_window():
    WINDOW = tk.Tk()
    
    checker_frame = create_window(WINDOW, window_name='checker_frame')
    
    image = tk.PhotoImage(file="../components/images/sample_resume1.png")
    image_label = tk.Label(checker_frame, image=image)
    
    image_label.pack(pady=20)
    
    WINDOW.mainloop()

create_checker_window()