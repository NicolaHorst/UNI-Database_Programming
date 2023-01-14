import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
import tkinter.filedialog as filedialog
from GuiBaseClass import GuiBaseClass
from KrokiEncoder import KrokiEncoder
import os, sys, re

class PumlEditor(GuiBaseClass):
    def __init__(self,root):
        super().__init__(root)
        # use getMenu to get file menu (mnu)
        # use mnu.insert_command(index,options) for 
        # insering new menues at a certain index
        # before File->Exit for instance
        mnu_file=self.getMenu('File')      
        mnu_file.insert_command(0,label="Open ...",underline=0,command=self.fileOpen)
        mnu_file.insert_command(1,label="Save ...",underline=0,command=self.fileSave)        
        mnu_file.insert_command(2,label="Save As ...",underline=1,command=self.fileSaveAs)                
        self.root.bind("<Control-s>", self.fileSave)
        self.root.bind("<Control-o>", self.fileOpen)
        
        mnu_url=self.getMenu('URL')
        self.menubar.entryconfig(1,underline=0)
        mnu_url.insert_command(0,label="Convert Text to URL",underline=8,command=self.text2url)
        mnu_url.insert_command(1,label="Convert URL to Text",underline=8,command=self.url2text)        
        
        # insert new menu points
        frame=self.getFrame()
        # insert tk.Text now in a PanedWindow
        self.pw = ttk.PanedWindow(frame,orient="horizontal")
        self.text = tk.Text(self.pw,wrap='word',undo=True)
        self.text.insert('end',"Hello start writing, please ...")  
        self.text.delete('1.0','end')      
        
        self.pw.add(self.text)
        # now the image widget
        self.imagewidget = ttk.Label(self.pw,text="Image Widget",anchor="center")
        self.pw.add(self.imagewidget)
        self.filename = ""
        self.lastfiledir = os.getcwd()
        self.addStatusBar()
        self.message("Hello I am Puml!!")
        self.filetypes=(
            ('Puml files', '*.pml'),
            ('Erd files', '*.erd'),
            ('Graphviz files', '*.dot'),
            ('Ditaa files', '*.dit'),            
            ('Text files', '*.txt'),
            ('All Files', '*.*'))
        self.pw.pack(side="top",fill="both",expand=True)
        self.kroki = KrokiEncoder()
        imgdata="""
           R0lGODlhEAAQAIMAAPwCBAQCBPz+/ISChKSipMTCxLS2tLy+vMzOzMTGxNTS
           1AAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAQABAAAARlEMgJQqDYyiDG
           rR8oWJxnCcQXDMU4GEYqFN4UEHB+FEhtv7EBIYEohkjBkwJBqggEMB+ncHha
           BsDUZmbAXq67EecQ02x2CMWzkAs504gCO3qcDZjkl11FMJVIN0cqHSpuGYYS
           fhEAIf5oQ3JlYXRlZCBieSBCTVBUb0dJRiBQcm8gdmVyc2lvbiAyLjUNCqkg
           RGV2ZWxDb3IgMTk5NywxOTk4LiBBbGwgcmlnaHRzIHJlc2VydmVkLg0KaHR0
           cDovL3d3dy5kZXZlbGNvci5jb20AOw==
        """
        self.image = tk.PhotoImage(data=imgdata)
        self.imagewidget.configure(image=self.image)
        # Have fun!
    def fileOpen (self,filename=''):
        if (type(filename) == tk.Event):
            filename=""
        if filename == "":
            filename = filedialog.askopenfilename(
                initialdir=os.path.dirname(self.filename),
                filetypes=self.filetypes)
        if filename != "":
            self.text.delete('1.0','end')
            file = open(filename,"r")
            for line in file:
                self.text.insert('end',line)
            self.filename = filename
            self.message(f"File {filename} was opened!")
            self.ImageUpdate()
    def fileSave (self,evt=None):
        if self.filename == "":
            self.fileSaveAs
        else:
            fin = open(self.filename, "w")
            fin.write(self.text.get("1.0","end"))
            fin.close()
            self.ImageUpdate()            
    def fileSaveAs (self):        
        filename=filedialog.asksaveasfilename(
            title='Select filename to save',
            filetypes=self.filetypes,
            initialdir=os.path.dirname(self.filename))
        if filename != "":
            self.filename = filename
            self.fileSave()
    def text2url (self):
        txt=self.text.get('1.0','end')
        dia = self.getDiaType()
        url=self.kroki.text2kroki(txt,dia=dia,ext="png")
        self.text.insert('end',"\n"+url)
    def url2text (self):
        url=self.text.get('1.0','end')
        url=re.sub("^\s+","",url)
        if not(bool(re.search("^https://kroki.io.+",url))):
            self.message("Error: Text in Editor seems not to be a kroki URL")
            bg=self.text.cget("background")
            self.text.configure(background="salmon")
            self.root.update_idletasks()
            self.root.after(2000)
            self.text.configure(background=bg)            
        else:
            txt=self.kroki.kroki2dia(url)
            self.text.insert("end","\n"+txt)
    def getDiaType (self):
        if bool(re.search("\\.pml$",self.filename)):
            dia="plantuml"
        elif bool(re.search("\\.dot$",self.filename)):
            dia="graphviz"
        elif bool(re.search("\\.erd$",self.filename)):
            dia="erd"            
        elif bool(re.search("\\.dit$",self.filename)):
            dia="ditaa"
        else:
            dia="ditaa"
        return(dia)
    def ImageUpdate (self):
        imgfile = re.sub(".[a-z]{3,4}$",".png", self.filename)
        dia = self.getDiaType()            
        self.kroki.dia2file(self.filename, dia=dia, imagefile=imgfile)
        if os.path.exists(imgfile):
            self.image.configure(file=imgfile)
            self.message(f"Displaying {imgfile}")
            self.root.title("PumlEditor 2022 - " + os.path.basename(self.filename))
        else:
            self.message("Image file was not downloaded!")
            
    def About (self):
        mbox.showinfo(title="About PumlEditor",message="PumlEditor 2022\nAuthor: Detlef Groth\nUniversity of Potsdam")
        
if __name__ == '__main__':
    root=tk.Tk()
    root.geometry("300x200")
    pedit = PumlEditor(root)
    root.title("PumlEditor 2022")
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            pedit.fileOpen(sys.argv[1])
    pedit.mainLoop() 
