import tkinter as tk

def create_window(window: tk.Tk, WHEIGHT=800, WWIDTH=1200):
    """
    Configure the Tkinter root window and return a frame.

    Returns:
        tk.Frame: A frame placed inside the root window.
    """
    window.geometry(f"{WWIDTH}x{WHEIGHT}")
    window.minsize(WWIDTH, WHEIGHT)
    window.maxsize(WWIDTH, WHEIGHT)

    # Create just one frame (instead of container + frame).
    frame = tk.Frame(window, width=WWIDTH, height=WHEIGHT)
    frame.pack(fill="both", expand=True)

    return frame

