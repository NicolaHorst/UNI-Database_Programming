import os
import re
import sys
from typing import Dict
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd

from nh_GuiBaseClass import GuiBaseClass
from nh_task_2 import file_to_dict
from DGScrolled import DGScrolled

def usage():
    print("nh_task3 by Nicola Horst, Uni Potsdam, 2023")
    print("""
    Usage: nh_task3.py [-h] ?[-gui] ?[FILE]? ?[Letter]
    Fasta-Parser Nicola Horst, 2022
    Extract information from FASTA data files.
    -------------------------------------------
    Mandatory arguments are:
        FILE        -  FASTA file
        Letter      -  An Amino Acid such as M, N, O (only considered in terminal mode)
    Optional arguments are (either --help, -h):
        --help      - display this help page
        -gui        - Start gui application
    
    for GUI:
        Show Statistics shows the number of occurrences of a given amino acid
        Show Entry shows the IDs of partially provided fasta id. e.g. P59 will print all IDs that contain P59
        
    example arguments for terminal mode could be:
        nh_task3.py uniprot-proteome-UP000464024.fasta M
    
    example usage for gui
        nh_task3.py -gui uniprot-proteome-UP000464024.fasta
    """)
    exit()

class FasterParser(GuiBaseClass):
    def __init__(self, root, file_name=""):
        super().__init__(root=root)

        if not os.path.isfile(file_name):
            self.file_name: str = self.open_file_dialog()
        else:
            self.file_name = file_name

        self.file_dict: Dict = file_to_dict(file_name=self.file_name)

        # starting the layout
        # first create the frame for the entry and the buttons
        self.top_frame = ttk.Frame(self.get_frame())

        # create the entry and the buttons
        self.entry = ttk.Entry(self.top_frame, width=30)

        self.btn_frame = ttk.Frame(self.top_frame)
        self.btn1 = ttk.Button(self.btn_frame, text="Show Statistics", width=20, command=self.show_statistics)
        self.btn_show_entry = ttk.Button(self.btn_frame, text="Show Entry", width=20, command=self.show_entry)

        self.entry.pack(anchor="center", side="left", expand=False)
        self.btn1.pack(anchor="center", side="left", expand=False)
        self.btn_show_entry.pack(anchor="center", side="right", expand=False)

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

    @staticmethod
    def open_file_dialog() -> str:
        return fd.askopenfilename()

    def main_loop(self):
        self.root.mainloop()

    def show_statistics(self):
        acid: str = self.entry.get().upper()
        if len(acid) > 1:
            acid = acid[:1]

        results = [f"{key}:\t {acid}\t {self.file_dict[key].count(acid)}\n" for key in self.file_dict.keys()]
        for result in results:
            self.text.insert(tk.END, result)

    def show_entry(self):
        id: str = self.entry.get()
        results = [f"{key}\n" for key in self.file_dict.keys() if id in key]
        for result in results:
            self.text.insert(tk.END, result)


if __name__ == "__main__":
    args = sys.argv
    root = tk.Tk()
    root.title("Fasta Gui")
    file_name = ""

    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) > 1:
        if args[1] == "-gui":
            if len(args) == 3:
                file_name = args[2]

            if os.path.isfile(file_name):
                parser = FasterParser(root=root, file_name=file_name)
            else:
                print(f"WARN:   filename: {file_name} does not exist")
                parser = FasterParser(root=root)

            parser.main_loop()
        else:
            file_name = args[1]
            if os.path.exists(file_name):
                file_dict = file_to_dict(file_name)
                acid: str = args[2].upper()
                if len(acid) > 1:
                    acid = acid[:1]

                results = [f"{key}:\t {acid}\t {file_dict[key].count(acid)}" for key in file_dict.keys()]
                for result in results:
                    print(result)
