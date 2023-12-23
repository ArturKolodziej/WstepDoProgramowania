droga=float(input("Podaj przejechaną drogę:"))
spalanie=float(input("Podaj średnie spalanie:"))
paliwo=6.5

zuzycie=droga*spalanie/100
koszty=zuzycie*paliwo

print(f"przewidywane zużycie paliwa:{zuzycie}")
print(f"przewidywane koszty paliwa:{koszty}")