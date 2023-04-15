import time
from datetime import date
date = date.today()
distance = 0
print("    ___    _         ___    __          ")
time.sleep(0.05)
print("   /   |  (_)____   /   |  / /___  _____")
time.sleep(0.05)
print("  / /| | / / ___/  / /| | / / __ \/ ___/")
time.sleep(0.05)
print(" / ___ |/ / /     / ___ |/ / /_/ (__  ) ")
time.sleep(0.05)
print("/_/  |_/_/_/     /_/  |_/_/ .___/____/  ")
time.sleep(0.05)
print("                         /_/            ")
time.sleep(0.1)
print("------------Logging Assistant-----------")
print("    ")
print("Hello, And thank you for flying with AirAlps™")
input("Press Enter to begin...")
flight = input("Please enter your flight number(e.g AAP0002, AAP0010)-->")
if flight == "AAP0001":
    departure = "London Heathrow/LHR"
    arrival = "Zurich/ZRH"
    distance = "789"
    profit = "33138"
if flight == "AAP0002":
    departure = "Zurich/ZRH"
    arrival = "London Heathrow/LHR"
    distance = "789"
    profit = "33138"
if flight == "AAP0003":
    departure = "Zurich/ZRH"
    arrival = "Geneva/GVA"
    distance = "230"
    profit = "9660"
if flight == "AAP0004":
    departure = "Geneva/GVA"
    arrival = "Zurich/ZRH"
    distance = "230"
    profit = "9660"
if flight == "AAP0005":
    departure = "Munich/MUC"
    arrival = "Zurich/ZRH"
    distance = "261"
    profit = "10962"
if flight == "AAP0006":
    departure = "Munich/MUC"
    arrival = "Zurich/ZRH"
    distance = "261"
    profit = "10962"
if flight == "AAP0007":
    departure = "Zurich/ZRH"
    arrival = "Gatwick/LGW"
    distance = "755"
    profit = "31710"
if flight == "AAP0008":
    departure = "Gatwick/LGW"
    arrival = "Zurich/ZRH"
    distance = "755"
    profit = "10962"
if flight == "AAP0009":
    departure = "Amsterdam/AMS"
    arrival = "Zurich/ZRH"
    distance = "603"
    profit = "25326"
if flight == "AAP0010":
    departure = "Zurich/ZRH"
    arrival = "Amsterdam/AMS"
    distance = "603"
    profit = "25326"
if flight == "AAP0011":
    departure = "Zurich/ZRH"
    arrival = "Sion/SIR"
    distance = "167"
    profit = "7014"
if flight == "AAP0012":
    departure = "Sion/SIR"
    arrival = "Zurich/ZRH"
    distance = "167"
    profit = "7014"
if flight == "AAP2001":
    departure = "Zurich/ZRH"
    arrival = "Boston/BOS"
    distance = "6026"
    profit = "253092"
if flight == "AAP2002":
    departure = "Boston/BOS"
    arrival = "Zurich/ZRH"
    distance = "6026"
    profit = "253092"
if flight == "AAP2003":
    departure = "Zurich/ZRH"
    arrival = "Dubai/DBX"
    distance = "4773"
    profit = "200466"
if flight == "AAP2004":
    departure = "Dubai/DBX"
    arrival = "Zurich/ZRH"
    distance = "4773"
    profit = "200466"
print("Be sure to post a screenshot when you post your flight log!")
input("Press Enter to Acknowledge and continue...")
if distance == 0:
    print("Sorry, it appears that " + flight + " isn't on our\nroute list or has yet to be added.\nIf you believe this is a mistake, please contact us.\nhttps://discord.gg/GBF7sxxGUw")
    time.sleep(0.5)
    input("Press Enter to exit...")
    exit()
else:
    time.sleep(0.2)
    print("Success! Route found.")
    aircraft = input("Please state the aircraft you flew -->")
    note = input("Any extra notes? -->")
    log = "--------" + flight + "--------\n|Aircraft: " + aircraft + "\n|Departure: " + departure + "\n|Arrival: " + arrival + "\n|Distance: " + distance + "km\n|Profit: " + profit + "£\n|Notes: " + note + "\n----------END----------"
    print(log)
    print("------------------------------------------------------------")
    print("Success! Thank you for flying with us, we hope to see you again!")
    time.sleep(2)
    input("Press enter to finish...")
    exit()


