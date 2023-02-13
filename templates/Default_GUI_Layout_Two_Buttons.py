#!usr/bin/env Python3
import os
import sys
from typing import List, Dict

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd

from gui_base_class.nh_GuiBaseClass import GuiBaseClass
from DGScrolled import DGScrolled


def usage():
    print("nh_* by Nicola Horst, Uni Potsdam, 2023")
    print("""
        Usage: nh_*.py [-h] ?[-gui] ?[FILE]
        Sample Tool by Nicola Horst, 2023
        What does the tool do.
        -------------------------------------------
        Mandatory arguments are:
            FIlE        -  file of type *
            ARG         -  Any other argument
        Optional arguments are (either --help, -h):
            --help      - display this help page
            -gui        - Start gui application

        for GUI:
            Explain what GUI version does
        
            example usage for gui
            nh_task3.py -gui ?[FILE]
            
        for Terminal:
            Explain what Terminal version does
            
            example arguments for terminal mode could be:
            nh_task3.py ?[FILE] [Additional Arg]
        """)


def run_command_line_tool(arguments: List):
    print("Since -gui is not present, commandline version of SampleGui is Executed")


def generic_file_reader_wrapper(fn: str) -> Dict:
    pass


class SampleGui(GuiBaseClass):
    def __init__(self, root, file_name):
        super().__init__(root=root)

        # setting file names
        self.file_name: str = file_name if os.path.isfile(file_name) else self.open_file_dialog()

        # setting dir name
        self.dir_name: str = ""  # = dir_name if os.path.isdir(dir_name) else self.open_dir_name_dialog
        # names = os.listdir(self.dir_name)
        # self.file_names = [name for name in names if name.endswith(".dat") or name.endswith(".dat.gz")]

        # open the given file and add a dictionary representation of it
        self.file_dict = generic_file_reader_wrapper(fn=file_name)

        # Add Menu File
        file_menu = self.get_menu("File")
        file_menu.add_separator()
        file_menu.add_command(label='Open New File', command=self.open_file_name, underline=1)
        file_menu.add_command(label='Open New Directory', command=self.open_dir_name, underline=1)

        # Add Menu help
        help_menu = self.get_menu("Help")
        help_menu.add_separator()
        help_menu.add_command(label='Help', command=usage, underline=1)

        # starting the layout
        # first create the frame for the entry and the buttons
        self.top_frame = ttk.Frame(self.get_frame())

        # create the entry and the buttons
        self.entry = ttk.Entry(self.top_frame, width=30)

        self.btn_frame = ttk.Frame(self.top_frame)
        self.btn1 = ttk.Button(self.btn_frame, text="Button 1", width=20, command=self.button_1_on_ckick)
        self.btn_2 = ttk.Button(self.btn_frame, text="Show Entry", width=20, command=self.button_2_on_ckick)

        self.entry.pack(anchor="center", side="left", expand=False)
        self.btn1.pack(anchor="center", side="left", expand=False)
        self.btn_2.pack(anchor="center", side="right", expand=False)

        self.btn_frame.pack(side="right", anchor="center", expand=False)
        self.top_frame.pack(side="top", anchor="center", expand=False)

        # add text widget
        self.text_frame = ttk.Frame(self.get_frame())
        self.text = tk.Text(self.text_frame)
        DGScrolled(self.text)
        self.text_frame.pack(side="top", expand=True, fill="both")

        # add status bar
        self.add_status_bar()
        self.set_status_bar_text(self.file_name.split("/")[-1])
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

    def open_file_name(self) -> None:
        """
        open file dialog and ask for a file_name and then open the file and transform it to a dictionary
        :return:  None
        """
        self.file_name = self.open_file_dialog()
        self.file_dict = generic_file_reader_wrapper(fn=file_name)
        self.set_status_bar_text(self.file_name.split("/")[-1])

    def open_dir_name(self):
        self.dir_name = self.open_dir_name_dialog()

    def main_loop(self):
        self.root.mainloop()


if __name__ == "__main__":
    args: List = sys.argv
    file_name: str = ""

    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    else:
        if "-gui" in args:
            root = tk.Tk()
            root.title("Sample Application")
            sample_gui: SampleGui = SampleGui(root=root, file_name=file_name)
            sample_gui.main_loop()
        else:
            run_command_line_tool(arguments=args)
