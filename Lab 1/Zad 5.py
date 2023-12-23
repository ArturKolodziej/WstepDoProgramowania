x=float(input("Proszę podać x"))
y=float(input("Proszę podać y"))
z=float(input("Proszę podać z"))

if x>y and x>z:
    if y>z:
        print(f"Cyfry od najwiekszej do najmniejszej: x={x},y={y},z={z}")
    else:
        print(f"Cyfry od najwiekszej do najmniejszej: x={x},z={z},z={y}")
elif y>z and y>x:
    if x>z:
        print(f"Cyfry od najwiekszej do najmniejszej: y={y},x={x},z={z}")
    else:
        print(f"Cyfry od najwiekszej do najmniejszej: y={y},z={z},x={x}")
elif z>y and z>x:
    if x>y:
        print(f"Cyfry od najwiekszej do najmniejszej: z={z},x={x},y={y}")
    else:
        print(f"Cyfry od najwiekszej do najmniejszej: z={z},y={y},x={x}")