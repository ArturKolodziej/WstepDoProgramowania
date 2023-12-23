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