def BMI(wzrost,waga):
    if wzrost>0 and waga>0:
        wskaznik=waga/(wzrost*wzrost)
        if wskaznik<18.5:
            print(f"BMI wynosi:{wskaznik} jesteś w zakresie: Niedowaga")
        elif wskaznik >= 18.5 and wskaznik < 25:
            print(f"BMI wynosi:{wskaznik} jesteś w zakresie: Waga prawidłowa")
        elif wskaznik >= 25 and wskaznik < 35:
            print(f"BMI wynosi:{wskaznik} jesteś w zakresie: Nadwaga I stopnia")
        elif wskaznik >= 35 and wskaznik < 40:
            print(f"BMI wynosi:{wskaznik} jesteś w zakresie: Nadwaga II stopnia")
        else:
            print(f"BMI wynosi:{wskaznik} jesteś w zakresie: Nadwaga III stopnia")
    else:
        print("Podano nieprawidłowe wartości.")

wzrost=float(input("Podaj wzrost(w metrach):"))
waga=float(input("Podaj wagę(w kilogramach):"))

BMI(wzrost,waga)