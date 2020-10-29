def addition(zahla, zahlb):
    zahlc = zahla + zahlb
    print("In der Funktion: zahla + zahlb = " + str(zahlc))
    return zahlc

def multiplikation(zahla, zahlb):
    print("In der Funktion: zahla * zahlb = " + str(zahla*zahlb))



a = 5
b = 10

c = addition(a, b)
print ("a + b = c :  c = " + str(c))

addition(10,20)
addition(1,1)
addition(3,10)

multiplikation(a,b)
multiplikation(5,3)


