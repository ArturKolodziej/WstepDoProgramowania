zakupy = {"Masło": 3.50, "Chleb": 4.50, "Mleko": 3, "Ser": 12, "Ketchup": 8}

for artykul, kwota in zakupy.items():
    print(f"{artykul}: {kwota} zł")

wydatki=sum(zakupy.values())
print(f"Zakupy wynoszą: {wydatki}zł")