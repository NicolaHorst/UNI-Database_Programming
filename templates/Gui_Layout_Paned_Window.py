#!usr/bin/env Python3
import os
import sys
from typing import List, Dict

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd

from templates.gui_base_class.nh_GuiBaseClass import GuiBaseClass
from DGScrolled import DGScrolled

def usage():
    print("nh_* by Nicola Horst, Uni Potsdam, 2023")
    print("APP-NAME by Nicola Horst, Uni Potsdam, 2023")
    print("""
        $ python3 nh_task_1.py
        Usage: nh_task_1.py --help [DIR NAME]
        Uniprot-Parser by Nicola Horst, 2023
        Extract information from Uniprot data files.
        -------------------------------------------
        Optional arguments are:
            --help - display this help pag
        Mandatory arguments are:
        DIR NAME - directory name

        Example usage: nh_task_1.py --go uniprot-corona-virus-data-2022-02.dat
        """)


def run_command_line_tool(arguments: List):
    print("Since -gui is not present, commandline version of SampleGui is Executed")


def generic_file_reader_wrapper(fn: str) -> Dict:
    pass


class SampleGui(GuiBaseClass):
    def __init__(self, root, dir_name):
        super().__init__(root=root)

        # generic file name check
        if not os.path.isdir(dir_name):
            self.dir_name: str = self.open_dir_name_dialog()
        else:
            self.dir_name: str = dir_name

        names = os.listdir(self.dir_name)
        self.file_names = [name for name in names if name.endswith(".dat") or name.endswith(".dat.gz")]

        # Add Menu help
        help_menu = self.get_menu("Help")
        help_menu.add_separator()
        help_menu.add_command(label='Help', command=usage, underline=1)

        # Add Menu File
        file_menu = self.get_menu("File")
        file_menu.add_separator()
        file_menu.add_command(label='Open New File', command=self.open_dir_name, underline=1)

        # starting the layout
        # first create the frame for the entry and the buttons
        self.pw = ttk.Panedwindow(self.get_frame(), orient=tk.HORIZONTAL)

        # list box and bind some callback to it
        l1 = tk.Listbox(self.pw, exportselection=False)
        l1.bind("<<ListboxSelect>>", self.l1_on_ckick)
        for item in self.file_names:
            l1.insert(tk.END, item)

        l2 = tk.Listbox(self.pw, exportselection=False)
        l2.bind("<<ListboxSelect>>", self.l2_on_ckick)
        list_items: List = ["Hello", "Hello2", "Hello3"]
        for item in list_items:
            l2.insert(tk.END, item)

        self.text = tk.Text(self.pw)
        DGScrolled(self.text)

        self.pw.add(l1)
        self.pw.add(l2)
        self.pw.add(self.text)

        self.pw.pack(fill="both", expand=True)

        # add status bar
        self.add_status_bar()
        self.set_status_bar_text(self.dir_name.split("/")[-1])
        self.set_status_bar_progress(50)

    def l1_on_ckick(self, event):
        """
        perform action when button 1 is pressed
        :return:
        """
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print(f"clicked {value}")

    def l2_on_ckick(self, event):
        """
        Perform the action when button 2 is pressed
        :return:
        """
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print(f"clicked {value}")

    def open_dir_name(self) -> None:
        """
        open file dialog and ask for a file_name and then open the file and transform it to a dictionary
        :return:  None
        """
        self.dir_name = self.open_dir_name_dialog()
        self.set_status_bar_text(self.dir_name)

    def main_loop(self):
        self.root.mainloop()


if __name__ == "__main__":
    args: List = sys.argv
    directory_name: str = ""
    if len(args) == 2:
        directory_name = args[1]

    root = tk.Tk()
    root.title("Sample Application")
    root.geometry("600x400")
    sample_gui: SampleGui = SampleGui(root=root, dir_name=directory_name)
    sample_gui.main_loop()
