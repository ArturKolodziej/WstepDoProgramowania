c1=int(input("Podaj pierwszą cyfrę:"))
c2=int(input("Podaj drugą cyfrę:"))

if c1>c2:
    x=c2
    while x<=c1:
        print(x)
        x+=1
elif c2>c1:
    x=c1
    while x <= c2:
        print(x)
        x += 1
else:
    print(f"Cyfry są równe {c1}={c2}")