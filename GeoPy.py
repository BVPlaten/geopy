# GeoPy.py 
# ein script zum zeichnen einfacher formen
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 31.05.2019  bvp  initial release
#
import turtle as t

#
#
#
def dreieck( laenge = 100.0, winkel = 120.0 ):
    for i in range(3):
        t.forward(laenge)
        t.left(winkel)


#
#
#
def quadrat( laenge = 100.0, winkel = 90.0 ):
    for i in range(4):
        t.forward(laenge)
        t.left(winkel)


def main():
    laenge = 100
    for i in range(4):
        dreieck(laenge)
        quadrat(laenge)
        laenge += 10 
    
if __name__ == "__main__":
    main()



