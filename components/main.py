import tkinter as tk

def create_window(window, window_name="NULL", WHEIGHT=800, WWIDTH=1200):
    """
    Configure an existing Tkinter window and return a frame for adding elements.

    Parameters:
        window (tk.Tk): The existing Tkinter window object to configure.
        window_name (str): The title of the window.
        WHEIGHT (int): The height of the window.
        WWIDTH (int): The width of the window.

    Returns:
        tk.Frame: A single frame for adding widgets and elements.
    """
   
    window.title(window_name)
    window.geometry(f"{WWIDTH}x{WHEIGHT}")

    container = tk.Frame(window)
    container.pack(fill="both", expand=True)

    frame = tk.Frame(container)
    frame.pack(fill="both", expand=True)

    
    return frame
