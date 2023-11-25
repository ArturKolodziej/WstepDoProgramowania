#Laboratorium 2 while

#Zad1
c1=int(input("Podaj pierwszą cyfrę:"))
c2=int(input("Podaj drugą cyfrę:"))

if c1>c2:
    x=c2
    while x<=c1:
        print(x)
        x+=1
elif c2>c1:
    x=c1
    while x <= c2:
        print(x)
        x += 1
else:
    print(f"Cyfry są równe {c1}={c2}")

#Zad2


#Zad3
x=0
while x>=0:
    x=float(input("Podaj cyfrę:"))
else:
    print("Koniec pętli")

#Zad4
c1=int(input("Podaj pierwszą cyfrę:"))
c2=int(input("Podaj drugą cyfrę:"))

if c1>c2:
    x=c2
    while x<=c1:
        if x%2==1:
            x += 1
            continue
        else:
            print(x)
            x+=1
elif c2>c1:
    x=c1
    while x <= c2:
        if x % 2 == 1:
            x += 1
            continue
        else:
            print(x)
            x += 1
else:
    print(f"Cyfry są równe {c1}={c2}")