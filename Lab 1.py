#Laboratorium 1

#Zad1
wiek=int(input("Proszę o podanie wieku:"))

if wiek<4 and wiek>=0:
    print("Wstęp jest bezpłatny")
elif wiek>18 and wiek<120:
    print("Wstęp kosztuje 20zł")
elif wiek>=4 and wiek<=18:
    print("Wstęp kosztuje 10zł")
else:
    print("Podano nieprawidłowy wiek")

#Zad2
litera=str(input("Proszę podać literę"))

if litera.isupper()==True:
    print("Podana litera jest wielką literą")
else:
    print("Podana litera jest małą literą")

#Zad3
print("Numery dostępnych operacji:")
print("1 -dodawanie")
print("2 -odejmowanie")
print("3 -mnożenie")
print("4 -dzielenie")
print("5 -potęgowanie")
operacja=int(input("Proszę podać numer opercji"))

if operacja==1:
    x=float(input("Proszę podać pierwszą cyfrę"))
    y=float(input("Proszę podać drugą cyfrę"))
    print("wartośc działania wynosi: ",x+y)
elif operacja==2:
    x=float(input("Proszę podać pierwszą cyfrę"))
    y=float(input("Proszę podać drugą cyfrę"))
    print("wartośc działania wynosi: ",x-y)
elif operacja==3:
    x=float(input("Proszę podać pierwszą cyfrę"))
    y=float(input("Proszę podać drugą cyfrę"))
    print("wartośc działania wynosi: ",x*y)
elif operacja==4:
    x=float(input("Proszę podać pierwszą cyfrę"))
    y=float(input("Proszę podać drugą cyfrę"))
    print("wartośc działania wynosi: ",x/y)
elif operacja==5:
    x=float(input("Proszę podać pierwszą cyfrę"))
    y=float(input("Proszę podać drugą cyfrę"))
    print("wartośc działania wynosi: ",x**y)
else:
    print("Podano nieprawidłową operację")

#Zad4
print("Program rozwiązujący równanie kwadratowe")
a=float(input("Proszę podać a"))
b=float(input("Proszę podać b"))
c=float(input("Proszę podać c"))
delta=(b**2)-(4*a*c)
if delta>0:
    x1=(-(b)-(delta**(1/2)))/2*a
    x2=(-(b)+(delta**(1/2)))/2*a
    print(f"Rozwiązania równania: x1={x1} x2={x2}")
elif delta==0:
    x=(-(b))/2*a
    print(f"Rozwiązanie równania: x={x}")
else:
    print("Delta mniejsza od zera: brak rozwiązań")

#Zad5
x=float(input("Proszę podać x"))
y=float(input("Proszę podać y"))
z=float(input("Proszę podać z"))

if x>y and x>z:
    if y>z:
        print(f"Cyfry od najwiekszej do najmniejszej: x={x},y={y},z={z}")
    else:
        print(f"Cyfry od najwiekszej do najmniejszej: x={x},z={z},z={y}")
elif y>z and y>x:
    if x>z:
        print(f"Cyfry od najwiekszej do najmniejszej: y={y},x={x},z={z}")
    else:
        print(f"Cyfry od najwiekszej do najmniejszej: y={y},z={z},x={x}")
elif z>y and z>x:
    if x>y:
        print(f"Cyfry od najwiekszej do najmniejszej: z={z},x={x},y={y}")
    else:
        print(f"Cyfry od najwiekszej do najmniejszej: z={z},y={y},x={x}")