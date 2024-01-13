import datetime

kolokwium = datetime.datetime(2024, 2, 11)
laboratorium = datetime.datetime(2023, 12, 10)

pozostalo = kolokwium - datetime.datetime.today()
uplynelo = datetime.datetime.today() - laboratorium
print(pozostalo)
print(uplynelo)