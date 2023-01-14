import os
import sys
import tkinter as tk
import tkinter.ttk as ttk


def gui():
    # Must need to be created before any variable is crated
    root = tk.Tk()
    root.title = os.getuid()
    text_string = tk.StringVar()
    text_string.set(value="Exit")
    btn = ttk.Button(root, textvariable=text_string, command=on_exit_button)
    btn.pack()
    root.mainloop()


def on_exit_button():
    exit()


def main(args):
    gui()


if '__main__' == __name__:
    main(sys.argv)
