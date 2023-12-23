import random

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
maksimumx = max(X)
maksimumy = max(Y)
print(f"Maksymalna wartość zbioru X: {maksimumx}, maksymalna wartość zbioru Y: {maksimumy}")

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