import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
global label_1, label_2_text, click_count


def clicked():
    global label_1, label_2_text, click_count
    click_count += 1

    label_1.configure(text=f"{click_count}")
    label_2_text.set(f"Label: {click_count}")


def gui():
    global label_1, label_2_text, click_count
    click_count = 0
    # Must need to be created before any variable is crated
    root = tk.Tk()
    root.title = os.getuid()

    # define vars
    label_1_text = tk.StringVar()
    label_2_text = tk.IntVar()
    btn_1_text = tk.StringVar()
    btn_2_text = tk.StringVar()

    # create Frame
    frame_1 = ttk.Frame(root)

    # create labels
    label_1_text.set("label_1")
    label_1 = ttk.Label(frame_1, text="label_1", justify="left")

    label_2_text.set(0)
    label_2 = tk.Label(frame_1, textvariable=label_2_text, justify="right")

    # create buttons
    btn_1_text.set("button 1")
    btn_1 = tk.Button(root, textvariable=btn_1_text, command=clicked)

    btn_2_text.set("button 2")
    btn_2 = tk.Button(root, textvariable=btn_2_text, command=on_exit_button)

    # pack when two components have same side they get stacked first come, first served
    label_1.pack(padx=3, pady=3, expand=True, fill='both', side='left')
    label_2.pack(padx=3, pady=3, expand=True, fill='both', side='right')
    frame_1.pack(padx=3, pady=3, expand=True, fill='both', side="top")
    btn_1.pack(padx=3, pady=3, expand=True, fill='both', side='top')
    btn_2.pack(padx=3, pady=3, expand=True, fill='both', side='top')

    root.mainloop()


def on_exit_button():
    exit()


def main(args):
    gui()


if '__main__' == __name__:
    main(sys.argv)
