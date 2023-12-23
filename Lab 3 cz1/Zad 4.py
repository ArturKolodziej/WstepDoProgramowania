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