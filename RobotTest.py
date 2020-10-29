# Demo Robotersteuerung

# Funktion zur Steuerung der Motoren
# dir = Drehrichtung des Motors (1 = links / -1 = rechts)
# power = Dehzahl in % (1 - 100%)
def motor(dir, power):
    print ("Motor 1 - " + str(dir) + " - " + str(power))
    print ("-----")
    return dir * power

print(motor(1, 10))
print(motor(-1,20))
print(motor(1,30))
