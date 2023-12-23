rachunki= {"styczeń": 130, "luty": 180, "marzec": 250, "kwiecień": 300, "maj": 250, "czerwiec": 200,
"lipiec": 140, "sierpień": 100, "wrzesień": 190, "październik": 400, "listopad": 210, "grudzień": 210}

#a
wartosci = list(rachunki.values())

maksimum=max(wartosci)
minimum=min(wartosci)
srednia= sum(wartosci)/len(wartosci)

print(f"Maksymalna wartośc rachunku: {maksimum}zł, minimalna wartośc rachunku: {minimum}zł, średnia wartość rachunku: {srednia}zł")

#b
miesiac = list(rachunki.keys())[-1]
rachunek = rachunki[miesiac]

if rachunek <= srednia:
    print("Jesteś bezpieczny")
else:
    print("Zacznij oszczędzać")