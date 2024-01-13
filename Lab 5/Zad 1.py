import random

print(f"Szczęśliwy numerek w grupie to: {random.randint(1,11)}")

roczniki=[1994,1998,2001,2002,2003]

print(f"Wylosowany rocznik to: {random.choice(roczniki)}")

lotek=[]

for i in range(0,49,1):
    lotek.append(i+1)

print(f"Wylosowane liczby to: {random.sample(lotek,6)}")
