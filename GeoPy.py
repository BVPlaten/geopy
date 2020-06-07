# GeoPy.py 
# Scripte um mit python-turtle Grafik etwas geometrie zu 
# betreiben.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 31.05.2019  bvp  initial release
#
import turtle as t
import sys
import CoordSys as cs

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - Konfiguration des gesamten Moduls
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
confg = {"startX" : -300,
         "startY" : -300,
         "width"  :  1500,
         "heigth" :  1000,
         "WindowTitel" : "GeoPy" }


# main() 
#
# die Startfunktion
def main():
    s = cs.CoordSys(confg)        # Koordinatensystem
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))


