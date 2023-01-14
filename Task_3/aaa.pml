@startuml
class GuiBaseClass {
    - self.frame
    - self.status
    + getFrame()
    + getMenu()
    + addStatusBar()
    + message()
    + progress()
    + mainLoop()
    # Exit()
    # About()
}

class PumlEditor {
    - self.kroki
    - self.img
    + fileNew()
    + fileOpen()
    + fileSave()
    + fileSaveAs()
    - About()
}

class DGStatusBar {
    + clear()
    + set()
    + message()
}

Class KrokiEncoder {
     + dia2kroki()
     + kroki2dia()
     + dia2file()
}
GuiBaseClass <- PumlEditor
DGStatusBar -* GuiBaseClass
PumlEditor *- KrokiEncoder
@enduml
