
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

