from Task_8.nh_GuiBaseClass import GuiBaseClass
import tkinter as tk
import sys
import os

class FastaParserGui(GuiBaseClass):
    def __init__(self, root, file=None):
        super().__init__(root)
        mnu = self.get_menu("File")
        mnu.insert_command(0, label="Open", command=self.file_open)
        help_mnu = self.get_menu("Help")

        self.pw = tk.PanedWindow(root)
        self.input = tk.Entry(self.pw)
        self.button = tk.Button(self.pw, text="Search")
        self.pw.add(self.input)
        self.pw.add(self.button)
        self.pw.pack(side="top", fill="both", expand=True)



    def file_open(self):
        pass

    def help(self):
        pass


if __name__ == '__main__':
    if len(sys.argv) < 1:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    print(line)
        else:
            print("file does not exists")
    elif "--gui" in sys.argv:
        root = tk.Tk()
        root.geometry("1200x800")
        fasta = FastaParserGui(root)
        root.title("PumlEditor 2022")
        fasta.main_loop()
