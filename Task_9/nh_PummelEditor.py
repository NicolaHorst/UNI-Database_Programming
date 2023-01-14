import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from nh_GuiBaseClass import GuiBaseClass
from tkinter import messagebox
import tkinter.filedialog as fd
from KrokiEncoder import KrokiEncoder
import re
from DGScrolled import DGScrolled

default_image = """
   R0lGODlhEAAQAIMAAPwCBAQCBPz+/ISChKSipMTCxLS2tLy+vMzOzMTGxNTS
   1AAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAQABAAAARlEMgJQqDYyiDG
   rR8oWJxnCcQXDMU4GEYqFN4UEHB+FEhtv7EBIYEohkjBkwJBqggEMB+ncHha
   BsDUZmbAXq67EecQ02x2CMWzkAs504gCO3qcDZjkl11FMJVIN0cqHSpuGYYS
   fhEAIf5oQ3JlYXRlZCBieSBCTVBUb0dJRiBQcm8gdmVyc2lvbiAyLjUNCqkg
   RGV2ZWxDb3IgMTk5NywxOTk4LiBBbGwgcmlnaHRzIHJlc2VydmVkLg0KaHR0
   cDovL3d3dy5kZXZlbGNvci5jb20AOw==
"""

class_diagram_template = """
@startuml
    left to right direction
    skinparam roundcorner 10
    skinparam linetype ortho
    skinparam shadowing false
    skinparam handwritten false
    !theme vibrant
    skinparam class {
        BackgroundColor #eeeeee
        ArrowColor #2688d4
        ArrowThickness 1
        BorderColor #2688d4
        BorderThickness 1
    }
    class BaseClass {
        - self.privar
        # self.protvar
        + self.pubvar
        + self.pubMethod()
        # self.ProtMethod()
        - self.PrivMethod()
    }
    class ChildClass {
        - self.privar
        + self.pubMethod()
    }

    class Component {
        - self.priv
        + self.pubMethod()
    }
    Component --* BaseClass
    ChildClass --> BaseClass
@enduml
"""

database_scheme = """
@startuml
    !define primary_key(x) <b><color:#b8861b><&key></color> x</b>
    !define foreign_key(x) <color:#aaaaaa><&key></color> x
    !define column(x) <color:#efefef><&media-record></color> x
    !define table(x) entity x << (T, white) >>
    
    left to right direction
    skinparam roundcorner 10
    skinparam linetype ortho
    skinparam shadowing false
    skinparam handwritten false
    !theme vibrant
    skinparam class {
        BackgroundColor #eeeeee
        ArrowColor #2688d4
        ArrowThickness 2
        BorderColor #2688d4
        BorderThickness 2
    }
    table( user ) {
      primary_key( id ): UUID 
      column( isActive ): BOOLEAN 
      foreign_key( cityId ): INTEGER <<FK>>
    }
    table( city ) {
      primary_key( id ): UUID 
      column( name ): TEXT
      column( country ): TEXT
      column( postCode ): INTEGER
    }
    user }|--|| city
@enduml
"""


class PumlEditor(GuiBaseClass):
    def __init__(self, root):
        super().__init__(root)
        # use getMenu to get file menu (mnu)
        # use mnu.insert_command(index,options) for
        # inserting new menus at a certain index
        # before File->Exit for instance

        # define basic vars
        self.file_name = ""
        self.file_types = (
            ('Puml files', '*.pml'),
            ('Erd files', '*.erd'),
            ('Graphviz files', '*.dot'),
            ('Ditaa files', '*.dit'),
            ('Text files', '*.txt'),
            ('All Files', '*.*'))

        # insert the File Menu
        mnu = self.get_menu("File")
        mnu.insert_command(0, label="Open", command=self.file_open)
        mnu.insert_command(1, label="Save", command=self.file_save)
        mnu.insert_command(2, label="Save as", command=self.file_save_as)
        mnu.insert_command(3, label="New file", command=self.new_file)
        mnu.insert_command(4, label="Insert File", command=self.insert_file)

        # insert the Template Menu
        template_mnu = self.get_menu("Templates")
        template_mnu.insert_command(0, label="UML Class Diagram", command=self.load_template)
        template_mnu.insert_command(2, label="clear", command=self.clear_text)
        template_mnu.insert_command(1, label="Database Scheme", command=self.load_db_template)

        main_frame = self.get_frame() # root
        self.paned_window = ttk.PanedWindow(main_frame, orient="horizontal")

        # add text widget with scroll bar
        self.textFrame = ttk.Frame(self.paned_window)
        self.text = tk.Text(self.textFrame, undo=True)
        self.text.insert("end", "Hello please type your message")
        DGScrolled(self.text)
        self.paned_window.add(self.textFrame)

        # add image label
        self.image_label = ttk.Label(self.paned_window, text="hello", anchor="center")
        self.image_label.pack(fill='both', expand=True, anchor="center", side='top', padx=10, pady=10)
        self.paned_window.add(self.image_label)

        # pack pane
        self.paned_window.pack(side="top", fill="both", expand=True)

        # Change img
        self.korki_encoder = KrokiEncoder()
        self.image = tk.PhotoImage(data=default_image)
        self.image_label.configure(image=self.image)

        # add status bar
        self.add_status_bar()
        self.set_status_bar_text("TestText")
        self.set_status_bar_progress(100)

        # insert new menu points
        frame = self.get_frame()
        # insert Listbox
        # Have fun!

    def file_open(self, filename=''):
        print("file open menu")
        self.set_status_bar_text(msg="Opening File")
        self.set_status_bar_progress(10)
        filename = fd.askopenfilename()
        print(filename)  #
        if filename != "":
            self.text.delete('1.0', 'end')
            with open(filename, "r") as file:
                for line in file:
                    self.text.insert("end", line)

        success_message = f"Successfully opened file:\t {filename.split('/')[-1]}"
        self.set_status_bar_text(msg=success_message)

    def new_file(self, filename=""):
        print("new file")

    def file_save(self):
        print("file save menu")
        if self.file_name == "":
            self.file_save_as()

        if os.path.exists(self.file_name):
            self.set_status_bar_text("Error File already exists")
        else:
            file = open(self.file_name, "w")
            file.write(self.text.get("1.0", "end"))
            file.close()
            imgfile = re.sub(".[a-z]{3,4}$", ".png", self.file_name)
            self.korki_encoder.dia2file(self.file_name, dia="plantuml", imagefile=imgfile)
            if os.path.exists(imgfile):
                self.image.configure(file=imgfile)
            else:
                self.set_status_bar_text("File was not downloaded")

        print(self.file_name)

    def file_save_as(self):
        print("file save as menu")
        self.file_name = fd.asksaveasfilename(title='Select filename to save',
                                        filetypes=self.file_types,
                                        initialdir=os.path.dirname(self.file_name))

    def load_template(self):
        self.clear_text()
        self.text.insert("1.0", class_diagram_template)

    def load_db_template(self):
        self.clear_text()
        self.text.insert("1.0", database_scheme)

    def clear_text(self):
        self.text.delete("1.0", "end")

    def insert_text(self, filename):
        file = open(filename, "r")
        data = file.read()
        self.text.insert("insert", data)

    def change_img(self, file_name: str):
        imgfile = re.sub(".[a-z]{3,4}$", ".png", file_name)
        if os.path.exists(imgfile):
            self.image.configure(file=imgfile)
        else:
            self.set_status_bar_text("File was not downloaded")

    def insert_file(self):
        filename = fd.askopenfilename(
            title='select filename', filetypes=(
                ("Txt files", "*.txt"),
                ("Puml files", "*.pml"),
                ("All files", "*.*")))
        if filename.endswith(".txt") or filename.endswith(".pml"):
            self.clear_text()
            self.insert_text(filename)
            if filename.endswith(".pml"):
                self.change_img(file_name=filename)




    def about(self):
        print("test")
        messagebox.showinfo(title="About Pummel Editor", message="By Nicola Horst in 2022\nUniversity of Potsdam")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1200x800")
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
