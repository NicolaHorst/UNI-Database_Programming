#'
#' Links: [DGBaseGui](DGBaseGui.html) - [DGAutoScrollBar](DGAutoScrollbar.html) - 
#'  [DGBalloon](DGBalloon.html) - [DGLabEntry](DGLabEntry.html) -  [DGScrolled](DGScrolled.html) - [DGStatusBar](DGStatusBar.html) -
#'  [DGTableView](DGTableView.html) - [DGTreeView](DGTreeView.html)
#'
#' ## Name
#'  
#'  `DGScrolled` - add easily scrollbars to a widget
#'  
#'  This is a convinience function to add scrollbars which can optionally autohide to 
#'  an existing widget which is placed already within a tk.Frame or a ttk.Frame
#'
#' ## Commands
#'  
#'  Except for the constructor there is no method available for the DGScrolled. 
#'  Simply provide the  widget which should get the two scrollbars. 
#'  The widget should be placed in its own frame before. 
#'  Don't pack or grid the widget itself, just pack or grid the parent frame.
#'  
#'  **DGScrolled(widget,...)**
#'  
#'  Arguments:
#'  
#'  - _widget_ - the widget which should get scrollbars,  must be placed within a frame already
#'  
#'  Example:
#' 
#'  ```
#'  import tkinter as tk
#'  import tkinter.ttk as ttk
#'  from dbp.widgets.DGScrolled import DGScrolled
#'  root=tk.Tk()
#'  nframe=ttk.Frame(root)
#'  text=tk.Text(nframe,wrap='none')
#'  DGScrolled(text)
#'  for i in range(0,30):
#'     text.insert('end',"Hello very long line text ...\n")
#'  nframe.pack(side='top',fill='both',expand=True)
#'  root.mainloop()
#'  ```
#'  
#'  Copyright: @ Detlef Groth, Caputh-Schwielowsee
#'  
#'  
#'  See also: [DGBaseGui](DGBaseGui.html), [DGAutoScrollbar](#DGAutoScrollbar)
#'  
#'  License: MIT
#'  

#from tkinter import *
import tkinter as tk 
import tkinter.ttk as ttk
from DGAutoScrollbar import DGAutoScrollbar

def DGScrolled(widget):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    nframe = widget.nametowidget(widget.winfo_parent())
    tsbv=DGAutoScrollbar(nframe)
    tsbh=DGAutoScrollbar(nframe,orient='horizontal')
    widget.configure(yscrollcommand=tsbv.set,
            xscrollcommand=tsbh.set)
    tsbv.grid(row=0, column=1, sticky='ns')
    tsbh.grid(row=1, column=0, sticky='ew')
    widget.grid(row=0, column=0, sticky='nsew')
    tsbv.config(command=widget.yview)
    tsbh.config(command=widget.xview)
    nframe.grid_rowconfigure(0, weight=1)
    nframe.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    root = tk.Tk()
    nframe=ttk.Frame(root)

    text=tk.Text(nframe,wrap='none')
    DGScrolled(text)
    for i in range(0,30):
      text.insert('end',"Hello very long line text ...\n")
    nframe.pack(side='top',fill='both',expand=True)
    root.mainloop()

