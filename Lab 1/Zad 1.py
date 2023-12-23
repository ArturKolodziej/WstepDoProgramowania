wiek=int(input("Proszę o podanie wieku:"))

if wiek<4 and wiek>=0:
    print("Wstęp jest bezpłatny")
elif wiek>18 and wiek<120:
    print("Wstęp kosztuje 20zł")
elif wiek>=4 and wiek<=18:
    print("Wstęp kosztuje 10zł")
else:
    print("Podano nieprawidłowy wiek")