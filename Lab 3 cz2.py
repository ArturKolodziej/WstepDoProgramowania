import random
#Zad 1

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