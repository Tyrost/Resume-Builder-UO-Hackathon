import logging as log
import tkinter as tk
from components.main import create_window

WINDOW = tk.Tk()
frame = create_window(WINDOW, "ResumAI", 600, 800)

label = tk.Label(frame, text="Input text here", font= ("Times New Roman", 14))
label.pack(pady=20)

WINDOW.mainloop()