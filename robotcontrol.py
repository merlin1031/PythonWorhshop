# Import
import sys, os

def printStatus():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("PiCrawler - Status")
    print ("Betriebssytem: " + os.name)

printStatus()