#'
#' Links: [DGBaseGui](DGBaseGui.html) - [DGAutoScrollBar](DGAutoScrollbar.html) - 
#'  [DGBalloon](DGBalloon.html) - [DGLabEntry](DGLabEntry.html) - [DGScrolled](DGScrolled.html) - [DGStatusBar](DGStatusBar.html) -
#'  [DGTableView](DGTableView.html) - [DGTreeView](DGTreeView.html)
#'
#' ## Name
#'  
#'  `DGAutoScrollbar` - scrollbars with autohide functionality if not needed.
#'  
#'  This a scrollbar which will hide itself if the widget for which they are configured do not acutally need
#'  scrollbars, for instance a text widget, where the current geometry is large enought to display all text.
#'  The widget and the the scrollbars will be gridded within the same geometry manager, so it usually required to place the scrollbars and the widget into the same frame without other widgets. This widget requires some effort to create scollbars, if you just like to have a simpler procedure to add those scrollbars use the class [DGScrolled](DGScrolled.html).
#'
#' ## Commands
#'  
#'  Except for the constructor there is no method available for the DGAutoScrollbar class, at object instantiation. 
#'  Simply provide the parent widget as usually and the standard arguments for ttk.Scrollbars.
#'  
#'  **DGAutoScrollbar(parent,...)**
#'  
#'  Arguments:
#'  
#'  - _parent_ - the parent widget wherein the scrollbar will be added
#'  - _..._ - standard ttk.Scrollbar arguments which will be delegated to the ttk.Scrollbar
#'  
#'  Example:
#' 
#'  ```
#'  import tkinter as tk
#'  import tkinter.ttk as ttk
#'  from dpb.widgets.DGAutoScrollbar import DGAutoScrollbar
#'  root=tk.Tk()
#'  nframe=ttk.Frame(root)
#'  tsbv=DGAutoScrollbar(nframe)
#'  tsbh=DGAutoScrollbar(nframe,orient='horizontal')
#'  text=tk.Text(nframe,
#'      yscrollcommand=tsbv.set,
#'      xscrollcommand=tsbh.set,wrap="none")
#'  tsbv.grid(row=0, column=1, sticky='ns')
#'  tsbh.grid(row=1, column=0, sticky='ew')
#'  text.grid(row=0, column=0, sticky='nsew')
#'  tsbv.config(command=text.yview)
#'  tsbh.config(command=text.xview)
#'  for i in range(0,30):
#'      text.insert('end',"Hello Text ...\n")
#'  
#'  nframe.grid_rowconfigure(0, weight=1)
#'  nframe.grid_columnconfigure(0, weight=1)
#'  nframe.pack(side='top',fill='both',expand=True)
#'  root.mainloop()
#'  ```
#'  
#'  Copyright: @ Detlef Groth, Caputh-Schwielowsee
#'  
#'  
#'  See also: [DGBaseGui](DGBaseGui.html), [DGScrolled](DGScrolled.html)
#'  
#'  License: MIT
#'  

#from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk 

class DGAutoScrollbar(ttk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        pass
       # raise TclError, "cannot use pack with this widget"
    def place(self, **kw):
        pass
        #    raise TclError, "cannot use place with this widget"

if __name__ == '__main__':
    
    root = tk.Tk()
    vscrollbar = DGAutoScrollbar(root)
    vscrollbar.grid(row=0, column=1, sticky='ns')
    hscrollbar = DGAutoScrollbar(root, orient='horizontal')
    hscrollbar.grid(row=1, column=0, sticky='ew')
    
    canvas = tk.Canvas(root,
                    yscrollcommand=vscrollbar.set,
                    xscrollcommand=hscrollbar.set)
    canvas.grid(row=0, column=0, sticky='nsew')
    
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)
    
    # make the canvas expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    #
    # create canvas contents
    
    frame = tk.Frame(canvas)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(1, weight=1)
    
    rows = 5
    for i in range(1,rows):
        for j in range(1,10):
            button = tk.Button(frame, padx=7, pady=7, text="[%d,%d]" % (i,j))
            button.grid(row=i, column=j, sticky='news')
    
    canvas.create_window(0, 0, anchor='nw', window=frame)
    
    frame.update_idletasks()
    
    canvas.config(scrollregion=canvas.bbox("all"))
    root.mainloop()

