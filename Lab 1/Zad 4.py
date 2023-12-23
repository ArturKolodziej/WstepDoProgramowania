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