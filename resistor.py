import sys

#print(resistans)

def ErsattningsResistansSeriell(intLista):
 print("Ersättningsresistansen för seriella resistanser är:" , sum(intLista))

def ErsattningsResistansPararell(intLista):
 nyLista = [1/i for i in intLista]
 res = 1/sum(nyLista)
 nyRes = "{:.2f}".format(res)
 print("Ersättningsresistansem för pararella resistanser är: ", nyRes)

#while True:

resistans = sys.argv[1:]
# resistanser = input("ange värderna på resistanser ")
# resistansLista = resistans.split(", ")
intLista = [eval(i) for i in resistans]
# print(intLista)
# print(len(intLista))
ErsattningsResistansSeriell(intLista)
ErsattningsResistansPararell(intLista)
