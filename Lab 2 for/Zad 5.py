silnia=int(input("Podaj liczbę do wyliczenia silni: "))
iloczyn = 1
for i in range(1,silnia+1):
    iloczyn=iloczyn*i
    i=i+1
print(iloczyn)