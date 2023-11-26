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