from datetime import datetime

kolokwium = datetime(2024, 2, 11)
laboratorium = datetime(2023, 12, 10)

aktualna_data = datetime.now()

czas_od_laboratoriow = aktualna_data - laboratorium
czas_do_kolokwium = kolokwium - aktualna_data

data_wyswietlona= aktualna_data.strftime("%d %B %Y %H:%M:%S")

print(f"Aktualna data i godzina to: {data_wyswietlona}")
print(f"Od ostatnich laboratoriów minęło: {czas_od_laboratoriow.days} dni i {czas_od_laboratoriow.seconds // 3600} godzin.")
print(f"Do kolokwium pozostało: {czas_do_kolokwium.days} dni i {czas_do_kolokwium.seconds // 3600} godzin.")

