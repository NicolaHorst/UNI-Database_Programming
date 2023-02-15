import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
from templates.DGStatusBar import DGStatusBar
import tkinter.filedialog as fd


class GuiBaseClass:
    def __init__(self, root):
        # create widgets
        self.root = root
        self.menu = dict()
        self.menubar = tk.Menu(root)

        # add menu option file
        menu_file = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label='File', underline=0,)
        menu_file.add_separator()

        # add menu option help
        menu_help = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_help, label="Help", underline=0, )
        menu_help.add_command(label='Exit', command=self.exit, underline=0)

        # add menu to root.config
        self.root.config(menu=self.menubar)

        # add menus to menu dict
        self.menu['menubar'] = self.menubar
        self.menu['File'] = menu_file
        self.menu['Help'] = menu_help

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # add status bar
        self.status_bar = DGStatusBar(self.root)

    # public functions
    def main_loop(self):
        self.root.mainloop()

    def get_frame(self):
        return self.frame

    def get_menu(self, entry):
        if entry in self.menu:
            return self.menu[entry]
        else:
            # we create a new one
            last = self.menu['menubar'].index('end')
            self.menu[entry] = tk.Menu(self.menubar)
            self.menu['menubar'].insert_cascade(
                last, menu=self.menu[entry], label=entry)
            return self.menu[entry]

    # Add the status barS
    def add_status_bar(self):
        self.status_bar.pack(fill="x", expand=False)

    def set_status_bar_text(self, msg: str):
        self.status_bar.set(msg)

    def set_status_bar_progress(self, progress: float):
        self.status_bar.progress(progress)

    # private functions
    def exit(self, ask=True):
        if ask:
            choice = messagebox.askyesno(title="Cancel", message="Are you sure you want to Cancel")
            if choice:
                sys.exit(0)
            else:
                pass
        else:
            sys.exit(0)

    def help(self):
        print("help menu")

    def about(self):
        print("about menu")

    def open_file_dialog(self) -> str:
        """
        open a file dialog and return the file name
        :return: file_name
        """
        return fd.askopenfilename(initialdir=os.getcwd())

    def open_dir_name_dialog(self) -> str:
        """
        open a file dialog and return dir name
        :return: dir_name
        """
        return fd.askdirectory(initialdir=os.getcwd())


if __name__ == '__main__':
    root = tk.Tk()
    bapp = GuiBaseClass(root)
    # example for using the BaseClass in other applications
    mnu = bapp.get_menu('Edit')
    mnu.add_command(label='Copy', command=lambda: print('Copy'))
    # example for using getFrame
    frm = bapp.get_frame()
    btn = ttk.Button(frm, text="Button X", command=lambda: sys.exit(0))
    btn.pack()
    bapp.main_loop()
