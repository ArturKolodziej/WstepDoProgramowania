#Laboratorium 2 for

#Zad 1
#a
for i in range (1,101):
    print(i, end=", ")

#b
for i in range(100,-1,-1):
    print(i, end=", ")

#c
for i in range(7,78,7):
    print(i, end=", ")

#d
for i in range(20,-1,-2):
    print(i, end=", ")

#Zad 2
x=int(input("Podaj liczbe gwaizdek: "))
for i in range(x):
    for i in range(x):
        print("*", end=" ")
    print()

#Zad3
x=int(input("Podaj liczbe gwaizdek: "))
for i in range(x):
    for i in range(i+1):
        print("*", end=" ")
    print()

#Zad4
n=int(input("Który wyraz ciągu policzyć: "))
a=int(input("Podaj pierwsz wyraz ciągu: "))
r=int(input("Podaj róznicę ciągu: "))
for i in range(1,n+1):
    an=a+(i-1)*r
    print(an)

#Zad5
silnia=int(input("Podaj liczbę do wyliczenia silni: "))
iloczyn = 1
for i in range(1,silnia+1):
    iloczyn=iloczyn*i
    i=i+1
print(iloczyn)