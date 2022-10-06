class Person:

   def __init__(self, age):
      self.age = int(age)

   def birthday(self):
      self.age += 1

   def beBorn(self):
      self.age = 0


gammal = []
name = []

antal = int(input('Hur många personer är ni: \n'))
antal += 1

for i in range(1, antal):
   print(f"\nHej person nummer {i}.")
   namn = input('Vad heter du?')
   name.append(namn)
   i = Person(input(f'Hur gammal är du: '))
   gammal.append(i.age)

print()

for Ra in range(1, antal):
   Ra -= 1
   print (f'{name[Ra]} är: {gammal[Ra]}')

print(f'\nVi har {antal - 1} personer')
print(f'Deras samlade ålder är = {sum(gammal)}')
