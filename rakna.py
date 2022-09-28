#!/usr/bin/python3

def rakna_upphojt(nummer, upphojt_till):   
    resultat = int(nummer) ** int(upphojt_till) 
    print(int(nummer),"^",int(upphojt_till),"=",int(resultat))

while True:
    nummer = input("ange nummret du vill lägga upphöjt till på ")
    upphojt_till = input("Ange nummret du vill lägga den i upphöjt till ")
    rakna_upphojt(nummer, upphojt_till)

