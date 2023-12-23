#Zad 1
lista=["Andrzej","Dariusz","Stefan","Karolina"]

#a
posortowana=sorted(lista)

#b
posortowana.append("Krzysztof")
posortowana.append("Zuzanna")

imie=posortowana.pop()
print(imie)

#c
posortowana.insert(3,"Faustyna")

#d
posortowana.reverse()
zdublowana=posortowana*2

for name in zdublowana:
    print(name)