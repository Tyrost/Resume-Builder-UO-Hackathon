from checker.checker import create_checker_window
from components import create_window
import tkinter as tk

'''
Main Python File
'''

def destroy_all(frame_list):
    pass

def main():
    MASTER_WINDOW = tk.Tk()
    
    MAIN_FRAME = create_window(MASTER_WINDOW)
    CHECKER_FRAME = create_window(MASTER_WINDOW)
    INTERVIEW_FRAME = create_window(MASTER_WINDOW)
    
    frames = [MAIN_FRAME, CHECKER_FRAME, INTERVIEW_FRAME]
    
    current_frame = MAIN_FRAME
    
    if current_frame == CHECKER_FRAME:
        pass
    
    MASTER_WINDOW.mainloop()
    
    
