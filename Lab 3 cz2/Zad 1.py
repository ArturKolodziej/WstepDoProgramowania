import random

n=int(input("Ile elementów  ma lista?"))
x=int(input("Ile Maksymalna liczba znaków w łańcuchu?"))

#ASCII

koniec=0
slowo=""
lista=[]

for i in range(n):
    for i in range(x):
        if koniec>=0.7:
            break
        else:
            slowo+=(chr(random.randint(65,90)))
            #print(slowo)

        koniec=random.random()
        #print(koniec)
    lista.append(slowo)
    koniec=0
    slowo=""
print(lista)

krotka=tuple(lista)

#a
print(len(lista))
znaki=0

for i in range(len(krotka)):
    znaki+=len(krotka[i-1])
print(znaki)

#b
K=0
for i in range(len(lista)):
    K+=lista[i].count("K")
print(lista.count("K"))

#c
KT=0
for i in range(len(lista)):
    K+=lista[i].count("KT")
print(lista.count("KT"))

#d
s=int(input("Podaj długośc ciągu s: "))
ilosc=0

for i in krotka:
    if len(i)>s:
        ilosc=ilosc+1
print(f"Ilosc ciągów znaków dłuższych od s: {ilosc}")