import turtle as t

class Shape(object):
    """Basisklasse für die geometrischen Figuren !"""

    # setze die Farbe zum Füllen
    #
    #
    def farbeSetzen(self,r,g,b):
        t.fillcolor(r,g,b)

    # zeichne ein 2D koordinatensystem
    #
    #
    def zeichneAchsen(self):
        xStrt = -250
        yStrt = -250
        schrt = 25
        t.up()
        t.setpos(xStrt,yStrt)
        t.setheading(0)
        t.down()

        start = t.position()
        for i in range(schrt):
            pos = t.position()
            t.setpos(pos[0]+schrt,pos[1])
            t.setpos(pos[0]+schrt,pos[1]+5)
            t.setpos(pos[0]+schrt,pos[1])
        
        t.setpos(start)
        t.setheading(90)
        for i in range(schrt):
            pos = t.position()
            t.setpos(pos[0]+schrt,pos[1])
            t.setpos(pos[0]+schrt,pos[1]+5)
            t.setpos(pos[0]+schrt,pos[1])



def main():
    s = Shape()
    s.zeichneAchsen()
    
if __name__ == "__main__":
    main()



