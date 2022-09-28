#!/usr/bin/python3
import math
import sys

def räkna_area(radien):
    resultat = float((float(radien) * float(radien)) * float(math.pi))
    nyRes = "{:.2f}".format(resultat)
    print("Arean är = ", float(nyRes))
    
def räkna_omkrets(radien):
    resultat = float((float(radien) * 2) * float(math.pi))
    nyRes = "{:.2f}".format(resultat)
    print("Omkretsen är  =", float(nyRes))


r = sys.argv
if ((len(r))  == 2):
   radien = int(r[1])
elif (len(r) < 2):
   radien = input("ange radien = ")
   print ("\n")

print("         , - ~ ~ ~ - ,")
print("     , '               ' ,")
print("   ,                       ,")
print("  ,                         ,")
print(f" ,          d= {(int(radien)) * 2}            ,")
print(" ,<------------------------->,")
print(" ,                           ,")
print("  ,                         ,")
print("   ,                       ,")
print("     ,                  , '")
print("       ' - , _ _ _ ,  '")



räkna_area(radien)
räkna_omkrets(radien)

