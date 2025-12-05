import tkinter as tk
from tkinter import ttk
from visu import VisualizadorProcesos

if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizadorProcesos(root)
    root.mainloop()
