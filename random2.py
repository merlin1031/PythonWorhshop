import random

anz1 = 0
anz2 = 0
for i in range(1, 100000, 1):
    zufall = random.randint(1,49)
    if zufall == 1:
        anz1 = anz1 +1
    elif zufall == 2:
        anz2 = anz2 +1

print ("Anzahl 1 = " + str(anz1))
print ("Anzahl 2 = " + str(anz2))
