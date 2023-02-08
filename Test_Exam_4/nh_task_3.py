#!usr/bin/env Python3
import os
import sys
from typing import List, Dict

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd

from nh_GuiBaseClass import GuiBaseClass
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
            self.dir_name: str = self.open_dir_dialog()
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

        # list box
        l1 = tk.Listbox(self.pw)
        for item in self.file_names:
            l1.insert(tk.END, item)

        l2 = tk.Listbox(self.pw)
        for item in self.file_names:
            l2.insert(tk.END, item)

        l3 = tk.Listbox(self.pw)
        for item in self.file_names:
            l3.insert(tk.END, item)

        self.pw.add(l1)
        self.pw.add(l2)
        self.pw.add(l3)

        self.pw.pack(fill="both", expand=True)
        # add status bar
        self.add_status_bar()
        self.set_status_bar_text(self.dir_name.split("/")[-1])
        self.set_status_bar_progress(50)

    def button_1_on_ckick(self):
        """
        perform action when button 1 is pressed
        :return:
        """
        print("Button 1 was pressed")

    def button_2_on_ckick(self):
        """
        Perform the action when button 2 is pressed
        :return:
        """
        print("Button 2 was pressed")

    @staticmethod
    def open_dir_dialog() -> str:
        """
        Open a file dialog and return the file name
        :return: file name
        """
        return fd.askdirectory()


    def open_dir_name(self) -> None:
        """
        open file dialog and ask for a file_name and then open the file and transform it to a dictionary
        :return:  None
        """
        self.dir_name = self.open_dir_dialog()
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
    sample_gui: SampleGui = SampleGui(root=root, dir_name=directory_name)
    sample_gui.main_loop()