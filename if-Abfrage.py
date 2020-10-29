# IF-Abfragen Grundlagen

# Variablen deklarieren
zahl = 5

# IF-Abfrage
if zahl == 5:
    print("Zahl ist gleich 5")
if zahl == 4:
    print("Zahl ist gleich 4")
if zahl <= 5:
    print("Zahl ist kleiner oder gleich 5")

print("Ende")

# IF-Abfrage mit else
print("---- IF-Abfrage mit ELSE ----")
if zahl == 4:
    print("Zahl ist gleich 4")
else:
    print("Zahl ist ungleich 4")
    print("Zahl ist " + str(zahl))
