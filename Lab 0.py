#Laboratorium 0
import random

#Zad1
type(1+2) #int - dodawanie
type(1+4.5) #float - dodawanie
type(3/2) #float - dzielenie
type(4/2) #int - dzielenie
type(3//2) #int - dzielenie całkowite
type(-3//2) #int - dzielenie całkowite
type(11%2) #int - reszta z dzielenia
type(2**10) #int - potęgowanie
type(8**(1/3)) #float - potęgowanie

#Zad2
int(3.0) #zmiana liczby na int
float(3) #zmiana liczby na float
float("3") #zmiana tekstu na liczbę float
str(12.4) #zmiana liczby float na string
bool(0) #zmina liczby na wartość logiczną

#Zad3
bok1=int(input("podaj długość boku 1:"))
bok2=int(input("podaj długość boku 2:"))
obwod=(bok1*2)+(bok2*2)
pole=bok1*bok2
print(f"pole wynosi: {pole}")
print(f"obwód wynosi: {obwod}")

#Zad4
droga=float(input("Podaj przejechaną drogę:"))
spalanie=float(input("Podaj średnie spalanie:"))
paliwo=6.5

zuzycie=droga*spalanie/100
koszty=zuzycie*paliwo

print(f"przewidywane zużycie paliwa:{zuzycie}")
print(f"przewidywane koszty paliwa:{koszty}")


#Zad4.1
droga=random.randint(1,1000)
spalanie=float(input("Podaj średnie spalanie:"))
paliwo=6.5

zuzycie=droga*spalanie/100
koszty=zuzycie*paliwo

print(f"przewidywane zużycie paliwa:{zuzycie}")
print(f"przewidywane koszty paliwa:{koszty}")