def poletrapez(a,b,h):
    if a>0 and b>0 and h>0:
        print("Pole trapezu wynosi:",((a+b)*h)/2)
    else:
        print("Podano niewłaściwe wartości")

poletrapez(3,4,0)