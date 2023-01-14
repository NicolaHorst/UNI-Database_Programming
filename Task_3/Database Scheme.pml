
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

