import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from nh_GuiBaseClass import GuiBaseClass
from tkinter import messagebox
import tkinter.filedialog as fd
from DGScrolled import DGScrolled


class FastaParserGui(GuiBaseClass):
    def __init__(self, root, file_name):
        super().__init__(root)

        self.file_types = (('Fasta Files', '*.fasta*'), ('All Files', '*.*'))
        self.file_name = file_name
        if self.file_name is None:
            self.file_name = self.open_file_dialog()

        # insert menu
        mnu = self.get_menu("File")

        main_frame = self.get_frame()
        self.master_pw = ttk.PanedWindow(main_frame, orient="vertical")

        # add entry and button
        self.paned_window = ttk.PanedWindow(self.master_pw, orient="horizontal")
        self.master_pw.add(self.paned_window)
        self.entry = ttk.Entry(self.paned_window, state=tk.NORMAL)
        self.entry.pack(fill='both', expand=True, anchor="nw", padx=10)
        self.btn = ttk.Button(self.paned_window, text="search")
        self.btn.pack(fill='both', expand=True, anchor="ne", padx=10)

        self.paned_window.add(self.entry)
        self.paned_window.add(self.btn)

        self.textFrame = ttk.Frame(self.master_pw)
        self.text = tk.Text(self.textFrame, undo=True)
        self.text.insert("end", "Hello please type your message")
        DGScrolled(self.text)
        self.textFrame.pack(side="bottom", expand=False)
        self.master_pw.add(self.textFrame)

        self.paned_window.pack(side="top", expand=False)
        self.master_pw.pack(expand=False)



    def open_file_dialog(self):
        return fd.askopenfilename(filetypes=self.file_types)


if __name__ == '__main__':

    if len(sys.argv) > 1 and "--gui" not in sys.argv:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    print(line)
        else:
            print("file does not exists")
    elif sys.argv[1] == "--gui":
        file_name = None
        if len(sys.argv) > 2:
            file_name = sys.argv[2]

        root = tk.Tk()
        root.geometry("300x200")
        fasta_gui = FastaParserGui(root, file_name)
        root.title("Fasta Gui")
        fasta_gui.main_loop()
