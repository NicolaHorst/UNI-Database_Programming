import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from nh_GuiBaseClass import GuiBaseClass
from tkinter import messagebox
import tkinter.filedialog as fd


class PumlEditor(GuiBaseClass):
    def __init__(self,root):
        super().__init__(root)
        # use getMenu to get file menu (mnu)
        # use mnu.insert_command(index,options) for
        # insering new menues at a certain index
        # before File->Exit for instance
        mnu = self.get_menu("File")
        mnu.insert_command(0, label="Open", command=self.file_open)
        mnu.insert_command(1, label="Save", command=self.file_save)
        mnu.insert_command(2, label="Save as", command=self.file_save_as)
        mnu.insert_command(3, label="New file", command=self.new_file)

        self.text = tk.Text(self.frame, undo=True)
        self.text.insert("end", "Hello please type your message")
        self.text.pack(fill="both", expand=True)

        # insert new menu points
        frame = self.get_frame()
        # insert Listbox
        # Have fun!

    def file_open(self, filename=''):
        print("file open menu")
        filename = fd.askopenfilename()
        print(filename)#
        if filename != "":
            self.text.delete('1.0', 'end')
            with open(filename, "r") as file:
                for line in file:
                    self.text.insert("end", line)

    def new_file(self, filename=""):
        print("new file")

    def file_save(self):
        print("file save menu")

    def file_save_as(self):
        print("file save as menu")

    def about(self):
        print("test")
        messagebox.showinfo(title="About Pummel Editor", message="By Nicola Horst in 2022\nUniversity of Potsdam")


if __name__ == '__main__':
    root=tk.Tk()
    root.geometry("300x200")
    pedit = PumlEditor(root)
    root.title("PumlEditor 2022")

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    print(line)
        else:
            print("file does not exists")
    else:
        pedit.main_loop()
