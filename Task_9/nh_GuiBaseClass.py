import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
from DGStatusBar import DGStatusBar


class GuiBaseClass():
    def __init__(self, root):
        # create widgets
        self.root = root
        self.menu = dict()
        self.menubar = tk.Menu(root)

        # add menu option help
        menu_help = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_help, label="Help", underline=0, )
        menu_help.add_separator()
        menu_help.add_command(label="help", command=self.help, underline=0)

        # add menu option About
        menu_about = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_about, label="About", underline=0, )
        menu_about.add_separator()
        menu_about.add_command(label="about", command=self.about, underline=0)

        # add menu option file
        menu_file = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label='File', underline=0, )
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=self.exit, underline=1)

        # add menu option Template
        menu_template = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_template, label="Templates", underline=0)
        menu_file.add_command(label="load class Diagram", command=self.load_class_diagram, underline=0)

        # add menu to root.config
        self.root.config(menu=self.menubar)

        # add menus to menu dict
        self.menu['menubar'] = self.menubar
        self.menu['File'] = menu_file
        self.menu['Help'] = menu_help
        self.menu['About'] = menu_about
        self.menu["Templates"] = menu_template
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

    def load_class_diagram(self):
        pass


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
