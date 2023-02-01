import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from nh_GuiBaseClass import GuiBaseClass
import tkinter.filedialog as fd
from DGScrolled import DGScrolled


def file_to_dict(file_name) -> dict:
    file_dict = {}
    is_first: bool = True
    key: str = ""
    seq: str = ""
    with open(file_name, "r") as reader:
        for line in reader:
            if line.startswith(">sp"):
                if is_first:
                    key = line.split(" ")[0][1:]
                    is_first = False
                else:
                    file_dict.update({key: seq})
                    key = line.split(" ")[0][1:]
                    seq = ""
            else:
                seq += line.strip('\n')

        file_dict.update({key: seq})

    return file_dict


class FastaParserGui(GuiBaseClass):
    def __init__(self, root, file_name):
        super().__init__(root)
        self.root = root
        self.file_types = (('Fasta Files', '*.fasta*'), ('All Files', '*.*'))
        self.file_name = file_name
        if self.file_name is None:
            self.file_name = self.open_file_dialog()

        self.file_dict = file_to_dict(file_name=file_name)

        # insert menu
        mnu = self.get_menu("File")

        main_frame = self.get_frame()

        # paned Window
        self.paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)

        # add basic entry and label
        self.entry = ttk.Entry(main_frame)
        self.button = ttk.Button(main_frame, text="Search", command=self.search)
        self.paned_window.add(self.entry)
        self.paned_window.add(self.button)

        self.paned_window.pack(fill="x")

        # text widget
        self.text_frame = ttk.Frame(main_frame)
        self.text = tk.Text(self.text_frame)
        DGScrolled(self.text)
        self.text_frame.pack(expand=True, fill="both")

        # add Status bar
        self.add_status_bar()
        self.set_status_bar_text(self.file_name)
        self.set_status_bar_progress(100)

    def open_file_dialog(self):
        return fd.askopenfilename(filetypes=self.file_types)

    def search(self):
        fasta_id: str = self.entry.get()
        results = [f"{key:<30}    {self.file_dict[key]} \n\n" for key in self.file_dict.keys() if fasta_id in key]
        for result in results:
            self.text.insert(tk.END, result)

        if not results:
            self.set_status_bar_text(f"No Sequences found for ID: {fasta_id}")
        else:
            self.set_status_bar_text(f"added {len(results)} new sequences")

    def main_loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    file_name = None

    if len(sys.argv) > 1 and "-gui" not in sys.argv:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    print(line)
        else:
            print("file does not exists")
    elif sys.argv[1] == "-gui" or os.path.exists(sys.argv[1]):
        if os.path.exists(sys.argv[1]):
            file_name = sys.argv[1]

        fasta_gui = FastaParserGui(root, file_name)
        root.title("Fasta Gui")
        fasta_gui.main_loop()

#%%
