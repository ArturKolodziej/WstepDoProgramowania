import random

#Zad3
bok1=int(input("podaj długość boku 1:"))
bok2=int(input("podaj długość boku 2:"))
obwod=(bok1*2)+(bok2*2)
pole=bok1*bok2
print("pole wynosi: ",pole)
print("obwód wynosi: ",obwod)

#Zad4
droga=float(input("Podaj przejechaną drogę:"))
spalanie=float(input("Podaj średnie spalanie:"))
paliwo=6.5

zuzycie=droga*spalanie/100
koszty=zuzycie*paliwo

print("przewidywane zużycie paliwa:",zuzycie)
print("przewidywane koszty paliwa:",koszty)


#Zad4.1
droga=random.randint(1,1000)
spalanie=float(input("Podaj średnie spalanie:"))
paliwo=6.5

zuzycie=droga*spalanie/100
koszty=zuzycie*paliwo

print("przewidywane zużycie paliwa:",zuzycie)
print("przewidywane koszty paliwa:",koszty)