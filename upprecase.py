#!/usr/bin/python3
f = open("uppertext.txt")
text = f.read()

def uppercase():
        print("Stor text:\n",text.upper())

def countwords():
    count = len(text.split())
    print("\nAntal ord: ", count)
    return count

def countletters(text):
    delete = "., \n"
    for deletes in delete:
        text = text.replace(deletes, '')
    print("\nAntal bokstäver:", len(text))
    kort_text = len(text)
    return kort_text

def medel():
    print("\nMedel:", (kort_text) / (len(text.split())))

uppercase()
countwords()
kort_text = countletters(text)
medel()
