#!usr/bin/env Python3
import os
import sys
from typing import List, Dict

import tkinter as tk
from tkinter import ttk

from nh_GuiBaseClass import GuiBaseClass
from DGScrolled import DGScrolled
from nh_final_task_2 import UniprotReader

def usage():
    print("nh_* by Nicola Horst, Uni Potsdam, 2023")
    print("""
        Usage: nh_*.py [-h] ?[-gui] ?[FILE]
        Sample Tool by Nicola Horst, 2023
        What does the tool do.
        -------------------------------------------
        Mandatory arguments are:
            FIlE        -  file of type .dat or.dat.gz
            ARG         -  Any other argument
        Optional arguments are (either --help, -h):
            --help      - display this help page
        """)


class SampleGui(GuiBaseClass, UniprotReader):
    def __init__(self, root, file_name: str):
        super().__init__(root=root)

        # setting dir name
        self.file_name: str = file_name if os.path.exists(file_name) else self.open_file_dialog()

        # Add Menu File
        file_menu = self.get_menu("File")
        file_menu.add_separator()
        file_menu.add_command(label='Open New File', command=self.open_file_name, underline=1)

        # Add Menu help
        help_menu = self.get_menu("Help")
        help_menu.add_separator()
        help_menu.add_command(label='Help', command=usage, underline=1)

        # Bottom Container
        self.bottom_frame = ttk.Panedwindow(self.get_frame(), orient=tk.HORIZONTAL)
        # starting the layout
        # first create the frame for the entry and the buttons
        self.top_frame = ttk.Panedwindow(self.bottom_frame, orient="vertical")

        # create the entry and the buttons
        self.entry = ttk.Entry(self.top_frame, width=10)

        # add combobox to the top bar
        self.combobox_values = self.get_up_ids(file_name=self.file_name)
        self.combobox = ttk.Combobox(self.top_frame, values=self.combobox_values, width=10)
        # bind a callback to the combobox
        self.combobox.bind('<<ComboboxSelected>>', self.combobox_on_select)

        # add button in top bar
        self.button = ttk.Button(self.top_frame, text="Search", command=self.button_on_click, width=10)

        # pack components for position change order of pack
        self.top_frame.add(self.combobox)
        self.top_frame.add(self.button)

        # add text widget
        self.text = tk.Text(self.bottom_frame, width=40)
        DGScrolled(self.text)

        # Add listbox
        self.list_box = tk.Listbox(self.bottom_frame, exportselection=False, width=20)
        self.list_box.bind("<<ListboxSelect>>", self.list_on_click)

        # add to frame
        self.bottom_frame.add(self.top_frame)
        self.bottom_frame.add(self.list_box)
        self.bottom_frame.add(self.text)

        # pack bottom frame
        self.bottom_frame.pack(expand=True, fill="both")

        # add status bar
        self.add_status_bar()
        self.set_status_bar_text(self.file_name.split("/")[-1])
        self.set_status_bar_progress(50)

    def get_up_ids(self, file_name: str):
        up_file = self.uniprot_file_to_dict(file_name=file_name, filter_on=["OS"])
        return list(set([key.split("_")[1]for key in up_file.keys()]))

    def button_on_click(self):
        """
        perform action when button 1 is pressed
        :return:
        """
        print(f"combobox text is {self.combobox.get()}")

    def list_on_click(self, event):
        """
        Perform the action when button 2 is pressed
        :return:
        """
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)

        self.text.delete("1.0", "end")
        seq = self.get_entry(file_name=self.file_name, id=value)
        for s in seq:
            self.text.insert(tk.END, s)

    def combobox_on_select(self, event):
        """
        Handle the event when a new element is selected
        :param event: the select event
        :return: None
        """
        element = self.combobox.get()
        up_ids = self.uniprot_file_to_dict(file_name=self.file_name, filter_on=["OS"])
        self.list_box.delete(0, tk.END)
        for key in up_ids.keys():
            if element in key:
                self.list_box.insert(tk.END, key)

    def open_file_name(self):
        self.file_name = self.open_file_dialog()
        up_ids = self.get_up_ids(file_name=self.file_name)
        self.combobox['values'] = up_ids
        self.list_box.delete(0, tk.END)
        self.set_status_bar_text(self.file_name.split("/")[-1])

    def main_loop(self):
        self.root.mainloop()


if __name__ == "__main__":
    args: List = sys.argv

    if "--help" in args:
        usage()

    file_or_dir_name: str = ""

    if len(args) >= 2:
        file_or_dir_name = args[1]

    root = tk.Tk()
    root.title("Sample Application")
    root.geometry("600x400")
    sample_gui: SampleGui = SampleGui(root=root, file_name=file_or_dir_name)
    sample_gui.main_loop()
