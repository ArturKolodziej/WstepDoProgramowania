n=int(input("Który wyraz ciągu policzyć: "))
a=int(input("Podaj pierwsz wyraz ciągu: "))
r=int(input("Podaj róznicę ciągu: "))
for i in range(1,n+1):
    an=a+(i-1)*r
    print(an)