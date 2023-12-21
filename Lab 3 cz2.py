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

#Zad 2

zakupy = {"Masło": 3.50, "Chleb": 4.50, "Mleko": 3, "Ser": 12, "Ketchup": 8}

for artykul, kwota in zakupy.items():
    print(f"{artykul}: {kwota} zł")

wydatki=sum(zakupy.values())
print(f"Zakupy wynoszą: {wydatki}zł")

#Zad 4

a = random.randint(3, 7)
b = random.randint(3, 7)

X=set()
Y=set()

for i in range(a):
    X.add(random.randint(0, 10))
for i in range(b):
    Y.add(random.randint(0, 10))
print(f"Zbiór X: {X}")
print(f"Zbiór Y: {Y}")

#a
czy5= 5 in X
print(f"Czy zbiór zawiera liczbę 5? {czy5}")

#b
czy_x_podzbior_y= X<=Y
print(f"Czy X jest podzbiorem Y? {czy_x_podzbior_y}")

#c
czy_y_podzbior_x = Y<=X
print(f"Czy X jest podzbiorem Y? {czy_y_podzbior_x}")

#d
czy_x_nadzbior_y = X>=Y
print(f"Czy X jest nadzbiorem Y? {czy_x_nadzbior_y}")

#e
czy_y_nadzbior_x = Y>=X
print(f"Czy Y jest nadzbiorem X? {czy_y_nadzbior_x}")

#f
suma_zbiorow = X | Y
print(f"Suma zbiorów X i Y: {suma_zbiorow}")

#g
roznica_X_Y = X - Y
print(f"Różnica zbiorów X i Y: {roznica_X_Y}")

#h
roznica_Y_X = Y - X
print(f"Różnica zbiorów Y i X: {roznica_Y_X}")

#i
iloczyn = X & Y
print(f"Iloczyn zbiorów wynosi: {iloczyn}")

#j
symetryczna = X ^ Y
print(f"Różnica symetryczna wynosi: {symetryczna}")

#k
maxX=max(X)
maxY=max(Y)
print(f"Maksymalna wartość zbioru X: {maxX}, maksymalna wartość zbioru Y: {maxY}")

#l
elementx=X.pop()
Y.add(elementx)
print(f"Zbiór Y po dodaniu elementu zbioru X: {Y}")

#m
Y.update(X)
print(f"Wartości zbioru X w zbiorze Y: {Y}")

#n
X.clear()
Y.clear()
print(f"Zbiory X i Y zostały wyczyszczone: X:{X}, Y:{Y}")