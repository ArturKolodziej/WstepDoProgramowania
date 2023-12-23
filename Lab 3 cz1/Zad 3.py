tekst="Python jest super"

#a
print(tekst[0])
print(tekst[-1])

#b
for i in range(0,len(tekst),2):
    print(tekst[i])

#c
for i in range(1,len(tekst),3):
    print(tekst[i])

#d

for i in range(10,len(tekst)):
    print(tekst[i])

#wer2
print(tekst[10:])

#e
print(tekst[::-1])