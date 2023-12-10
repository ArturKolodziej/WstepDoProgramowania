# Laboratorium 3

#Zad 1
lista=["Andrzej","Dariusz","Stefan","Karolina"]

#a
posortowana=sorted(lista)

#b
posortowana.append("Krzysztof")
posortowana.append("Zuzanna")

imie=posortowana.pop()
print(imie)

#c
posortowana.insert(3,"Faustyna")

#d
posortowana.reverse()
zdublowana=posortowana*2

for name in zdublowana:
    print(name)

#Zad 2
haslo="Rzeszów jest piękny"

#a
print(haslo[0])

#b
print(haslo[6])
print(haslo[9])
print(haslo[12])
print(haslo[1])

#Zad 3

tekst="Python jest super"

#a
print(tekst[0])
print(tekst[-1])

#b
for i in range(0,len(tekst),2):
    print(tekst[i])

#c
for i in range(1,len(tekst),3):
    print(tekst[i])

#d

for i in range(10,len(tekst)):
    print(tekst[i])

#wer2
print(tekst[10:])

#e
print(tekst[::-1])

#Zad 4

imie=input("Podaj imie: ")
nazwisko=input("Podaj nazwisko: ")
wiek=input("Podaj wiek: ")

#a
print(f"Witaj: {imie}")

#b
print(f"Twój wiek to: {wiek}")

#c
print(f"Twoje inicjały to: {imie[0]}{nazwisko[0]}")

#d
lancuch=input("Podaj tekst: ")

for i in range(0,5):
    print(f"{lancuch}")

#e

tekst1=input("Podaj tekst nr 1: ")
tekst2=input("Podaj tekst nr 2: ")

polaczone=tekst1+tekst2

print(f"{polaczone}")

#f

zlaczone=""

for i in range(0,int(len(tekst1)/2)):
    zlaczone=zlaczone+tekst1[i]
for i in range(int(len(tekst2)/2),len(tekst1)):
    zlaczone=zlaczone+tekst2[i]

print(f"{zlaczone}")