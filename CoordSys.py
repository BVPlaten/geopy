import turtle as t
import GeoBase

class CoordSys(GeoBase.GeoBase):
    """Basisklasse für die geometrischen Figuren !"""

    def __init__(self, confg):
        super().__init__(confg)
        self.openWindow()
        # t.up()
        # t.setx(coords[0])
        # t.sety(coords[1])
        # t.down()
        self.zeichneXachse(25)          # zeichne die X-Achse
        # t.setx(coords[0])
        # t.sety(coords[1])
        self.goStart()
        self.zeichneYachse(25)          # zeichne die X-Achse
        # t.setx(coords[0])
        # t.sety(coords[1])
        self.goStart()
        return 

    # setze die Farbe zum Füllen
    #
    #
    def farbeSetzen(self,r,g,b):
        t.fillcolor(r,g,b)

    # Funktion zeichneXachse
    # zeichnet die X-Achse mit Pfeil und Beschriftung
    #
    # Parameter: schrt : Anzahl der Schritte 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 01.06.2020  bvp  erste version
    #
    def zeichneXachse(self,schrt):
        t.setheading(0)
        for i in range(schrt):
            t.fd(schrt)
            pos = t.position()
            t.setpos(pos[0],pos[1] - 7)
            t.setpos(pos[0],pos[1])
        # zeichne pfeilspitze Y
        self.pfeilX()

    # Funktion zeichneYachse
    # zeichnet die Y-Achse mit Pfeil und Beschriftung
    #
    # Parameter: schrt : Anzahl der Schritte 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 01.06.2020  bvp  erste version
    #
    def zeichneYachse(self,schrt):
        t.setheading(90)
        for i in range(schrt):
            t.fd(schrt)
            pos = t.position()
            t.setpos(pos[0]-7,pos[1] )
            t.setpos(pos[0]  ,pos[1] )
        # zeichne pfeilspitze Y
        self.pfeilY()



    # Funktion pfeilX
    # zeichnet die die Pfeilspitze am Ende der X-Achse
    #
    # Parameter: schrt : Anzahl der Schritte 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 01.06.2020  bvp  erste version
    #
    def pfeilX( self ):
        pos = t.position()
        t.setpos(pos[0]   ,pos[1]-7 )
        t.setpos(pos[0]+13,pos[1]   )
        t.setpos(pos[0]   ,pos[1]+7 )
        t.setpos(pos[0]   ,pos[1]   )
        t.up()
        t.setpos(pos[0]+15,pos[1]-15)
        t.down()
        t.write("X-Achse")
        t.up()
        t.setpos(pos[0]   ,pos[1]   )
        t.down()

    # Funktion pfeilY
    # zeichnet die die Pfeilspitze am Ende der Y-Achse
    #
    # Parameter: schrt : Anzahl der Schritte 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 01.06.2020  bvp  erste version
    #
    def pfeilY( self ):
        pos = t.position()
        t.setpos(pos[0]-7 ,pos[1]   )
        t.setpos(pos[0]   ,pos[1]+13)
        t.setpos(pos[0]+7 ,pos[1]   )
        t.setpos(pos[0]   ,pos[1]   )
        t.up()
        t.setpos(pos[0]-15,pos[1]+15)
        t.down()
        t.write("Y-Achse")
        t.up()
        t.setpos(pos[0]   ,pos[1]   )
        t.down()




def main():
    strtPos = (-300,-300)
    s = CoordSys(strtPos)
    
    
if __name__ == "__main__":
    main()



