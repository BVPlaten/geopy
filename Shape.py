import turtle as t

class Shape(object):
    """Basisklasse für die geometrischen Figuren !"""

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
            pos = t.position()
            t.setpos(pos[0]+schrt,pos[1])
            t.setpos(pos[0]+schrt,pos[1]+5)
            t.setpos(pos[0]+schrt,pos[1])
        # zeichne Pfeilspitze X
        pos = t.position()
        t.setpos(pos[0]  ,pos[1]+5 )
        t.setpos(pos[0]+7,pos[1]   )
        t.setpos(pos[0]  ,pos[1]-5 )
        t.setpos(pos[0]  ,pos[1]   )
        t.up()
        t.setpos(pos[0]+12,pos[1]+12)
        t.down()
        t.write("X")

    # Funktion zeichneYachse
    # zeichnet die X-Achse mit Pfeil und Beschriftung
    #
    # Parameter: schrt : Anzahl der Schritte 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 01.06.2020  bvp  erste version
    #
    def zeichneYachse(self,schrt):
        t.setheading(90)
        for i in range(schrt):
            pos = t.position()
            t.setpos(pos[0]  ,pos[1]+schrt)
            t.setpos(pos[0]+5,pos[1]+schrt)
            t.setpos(pos[0]  ,pos[1]+schrt)
        # zeichne pfeilspitze Y
        pos = t.position()
        t.setpos(pos[0]+5,pos[1]  )
        t.setpos(pos[0]  ,pos[1]+7)
        t.setpos(pos[0]-5,pos[1]  )
        t.setpos(pos[0]  ,pos[1]  )
        t.up()
        t.setpos(pos[0]-12,pos[1]+12)
        t.down()
        t.write("Y")

    # Funktion KoordSystem 
    #
    # zeichne ein 2D koordinatensystem
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 01.06.2020  bvp  erste version
    #
    def KoordSystem(self):
        xStrt = -250
        yStrt = -250
        t.speed(2)
        t.up()
        t.setpos(xStrt,yStrt)
        t.down()

        # zeichne die X-Achse
        self.zeichneXachse(25)

        t.up()
        t.setpos(xStrt,yStrt)
        t.down()
        

        # zeichne die Y-Achse
        self.zeichneYachse(25)



def main():
    s = Shape()
    s.KoordSystem()
    
if __name__ == "__main__":
    main()



