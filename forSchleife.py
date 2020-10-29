# Variablen deklarieren
superhelden = ["Spiderman", "Superman", "Bat Man", "Iron Man"]
i = 0   # Zähler auf 0 setzen

# Demo der For-Schleife
for held in superhelden:
    i = i + 1
    print (str(i) + " = " + held)
print ("so das waren jetzt alle Superhelden")


# Demo der For-Schleife mit enumerate
for nr, held in enumerate(superhelden):
    print (nr, held)
print ("so das waren jetzt alle Superhelden gezählt mit enumerate")