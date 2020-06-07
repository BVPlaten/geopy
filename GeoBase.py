# GeoBase.py 
#
# Basisklasse
import turtle as t
import sys
import pathlib



class GeoBase(object):

    def __init__(self, config):
        self.cfg = config
        return super().__init__()

    # openWindow 
    # 
    # �ffnet das Fenster annanhd der Konfigurationsdaten 
    #        
    def openWindow(self):
        t.setup(self.cfg["width"],self.cfg["heigth"])
        t.title(self.cfg["WindowTitel"])
        self.goStart()
        return

    # goStart
    # 
    # Setzt den Cursor an den Startpunkt
    #        
    def goStart(self):
        t.up()
        t.setpos(self.cfg["startX"],self.cfg["startY"])
        t.down()
        return
    

def main():
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))