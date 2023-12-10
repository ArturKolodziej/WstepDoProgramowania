def BMI(wzrost,waga):
    if wzrost>0 and waga>0:
        wskaznik=wzrost/waga**2
        if wskaznik<18.5:
            print(f"BMI wynosi:{wskaznik} jesteś w zakresie: Niedowaga")
        elif wskaznik >18.5

wzrost=float(input("Podaj wzrost(w metrach):"))
waga=float(input("Podaj wagę(w kilogramach):"))

BMI(wzrost,waga)