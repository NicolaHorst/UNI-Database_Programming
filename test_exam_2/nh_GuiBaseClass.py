import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sys


class GuiBaseClass():
    def __init__(self, root):
        # create widgets
        self.root = root
        self.menu = dict()
        self.menubar = tk.Menu(root)

        # add menu option help
        menu_help = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_help, label="Help", underline=0,)
        menu_help.add_separator()
        menu_help.add_command(label="help", command=self.help, underline=0)

        # add menu option About
        menu_about = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_about, label="About", underline=0, )
        menu_about.add_separator()
        menu_about.add_command(label="about", command=self.about, underline=0)

        # add menu option file
        menu_file = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label='File', underline=0,)
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=self.exit, underline=1)

        # add menu to root.config
        self.root.config(menu=self.menubar)

        # add menus to menu dict
        self.menu['menubar'] = self.menubar
        self.menu['File'] = menu_file
        self.menu['Help'] = menu_help
        self.menu['About'] = menu_about
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

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

    # private functions
    def exit(self, ask=True):
        if ask:
            choice = messagebox.askyesno(title="Cancel", message="Are you want to Cancel")
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
