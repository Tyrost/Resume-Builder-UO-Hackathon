import logging as log
import tkinter as tk

WINDOW  = tk.TK()

WHEIGHT = 600
WWIDTH = 800

container = tk.Frame(WINDOW)

MAIN_FRAME = tk.Frame(container)
CHECKER_FRAME = tk.Frame(container)
COMPARE_FRAME = tk.Frame(container)

frames = [MAIN_FRAME, CHECKER_FRAME, COMPARE_FRAME]
