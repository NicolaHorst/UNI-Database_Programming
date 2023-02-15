#!usr/bin/env Python3
import os
import sys
from typing import List, Dict

import tkinter as tk
from tkinter import ttk

from nh_GuiBaseClass import GuiBaseClass
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
        #self.dir_name: str = ""  # = dir_name if os.path.isdir(dir_name) else self.open_dir_name_dialog
        #names = os.listdir(self.dir_name)
        #self.file_names = [name for name in names if name.endswith(".dat") or name.endswith(".dat.gz")]
        #self.absolute_path_mapping: Dict = {file_name: self.dir_name + "/" + file_name for file_name in self.file_names}

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
        self.entry = ttk.Entry(self.top_frame, width=10)

        # add combobox to the top bar
        self.combobox_values = ["Entry 1", "Entry 2"]
        self.combobox = ttk.Combobox(self.top_frame, values=self.combobox_values, width=10)
        # set active value
        # self.combobox.current(0)
        # bind a callback to the combobox
        self.combobox.bind('<<ComboboxSelected>>', self.combobox_on_select)

        # add button in top bar
        self.button = ttk.Button(self.top_frame, text="Click Me", command=self.button_on_click, width=10)

        # pack components for position change order of pack
        self.entry.pack(side="left", expand=True, fill="x")
        self.combobox.pack(side="left", expand=True, fill="x")
        self.button.pack(side="left", expand=True, fill="x")

        self.top_frame.pack(side="top", anchor="center", expand=False, fill="x")

        # Bottom Container
        self.bottom_frame = ttk.Panedwindow(self.get_frame(), orient=tk.HORIZONTAL)

        # add text widget
        self.text = tk.Text(self.bottom_frame, width=40)
        DGScrolled(self.text)

        # Add listbox
        self.list_box = tk.Listbox(self.bottom_frame, exportselection=False, width=20)
        self.list_box.bind("<<ListboxSelect>>", self.list_on_click)
        self.list_items: List = ["List Entry 1", "List Entry 2", "List Entry 3"]
        for item in self.list_items:
            self.list_box.insert(tk.END, item)

        # add to frame
        self.bottom_frame.add(self.list_box)
        self.bottom_frame.add(self.text)

        # pack bottom frame
        self.bottom_frame.pack(expand=True, fill="both")

        # add status bar
        self.add_status_bar()
        self.set_status_bar_text(self.file_name.split("/")[-1])
        self.set_status_bar_progress(50)

    def button_on_click(self):
        """
        perform action when button 1 is pressed
        :return:
        """
        combobox_text = self.combobox.get()
        if combobox_text not in self.combobox['values']:
            self.combobox['values'] = (*self.combobox['values'], combobox_text)
        print(f"combobox text is {combobox_text}")

    def list_on_click(self, event):
        """
        Perform the action when button 2 is pressed
        :return:
        """
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print(f"clicked {value}")

    def combobox_on_select(self, event):
        """
        Handle the event when a new element is selected
        :param event: the select event
        :return: None
        """
        print(self.combobox.get())

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
    file_or_dir_name: str = ""

    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    else:
        if "-gui" in args:
            # if file or directory name is provided get it
            if len(args) > 2:
                file_or_dir_name = args[2]

            root = tk.Tk()
            root.title("Sample Application")
            root.geometry("600x400")
            sample_gui: SampleGui = SampleGui(root=root, file_name=file_or_dir_name)
            sample_gui.main_loop()
        else:
            run_command_line_tool(arguments=args)
