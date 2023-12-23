def potega(a,n):
    wynik=1
    for i in range(n):
        wynik=wynik*a
    print(f"Wynik potegowania wynosi: {wynik}")

a=int(input("Podaj podstawę a:"))
n=int(input("Podaj wykładnik n:"))

potega(a,n)