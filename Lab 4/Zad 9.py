def fibonacci(n):
    if n<=1:
        print(f"{n} wyraz ciągu wynosi: {n}")
    else:
        a=0
        b=1
        for i in range(2,n+1):
            a,b = b,a+b
    print(f"{n} wyraz ciągu wynosi: {b}")


n=int(input("Podaj wyraz ciągu n:"))

fibonacci(n)