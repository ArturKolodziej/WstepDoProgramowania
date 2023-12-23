def poletrojkata(a,b,c):
    if a<=0 or b<=0 or c<=0:
        print(f"Boki nie mogą być mniejsze bądź równe zero")
    elif a+b<=c or a+c<=b or c+b<=a:
        print(f"Suma długości dwóch dowolnych boków musi być większa od długości trzeciego boku.")
    else:
        p=(a+b+c)/2
        pole=(p*(p-a)*(p-b)*(p-c))**(1/2)
        print(f"Pole trójkąta wynosi: {pole}")

a=float(input("Podaj bok a: "))
b=float(input("Podaj bok b: "))
c=float(input("Podaj bok c: "))

poletrojkata(a,b,c)