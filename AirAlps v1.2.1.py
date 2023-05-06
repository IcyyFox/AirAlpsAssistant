import time
import datetime
from datetime import date, datetime, timedelta
date = date.today()
distance = 0
codeshare = "None"
# Fuelcost is Pounds/kg of fuel
fuelcost = 0.61
passengerPerKm = 0.206
efficiency = 0
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
print("----------Logging Assistant V1.1---------")
print("    ")
print("Hello, And thank you for flying with AirAlps™")
input("Press Enter to begin...")
flight = input("Please enter your flight number(e.g AAP0002, AAP0010)-->")
Takeoff = input("Please enter time of Takeoff, In Zulu time, e.g 2100-->")
if flight == "AAP0001":
    departure = "London Heathrow/LHR"
    arrival = "Zurich/ZRH"
    distance = 789
    EFD = "0110"
if flight == "AAP0002":
    departure = "Zurich/ZRH"
    arrival = "London Heathrow/LHR"
    distance = 789
    EFD = 110
if flight == "AAP0003":
    departure = "Zurich/ZRH"
    arrival = "Geneva/GVA"
    distance = 230
    EFD = 55
if flight == "AAP0004":
    departure = "Geneva/GVA"
    arrival = "Zurich/ZRH"
    distance = 230
    EFD = 55
if flight == "AAP0005":
    departure = "Munich/MUC"
    arrival = "Zurich/ZRH"
    distance = 261
    EFD = 50
if flight == "AAP0006":
    departure = "Munich/MUC"
    arrival = "Zurich/ZRH"
    distance = 261
    EFD = 50
if flight == "AAP0007":
    departure = "Zurich/ZRH"
    arrival = "Gatwick/LGW"
    distance = 755
    EFD = 105
if flight == "AAP0008":
    departure = "Gatwick/LGW"
    arrival = "Zurich/ZRH"
    distance = 755
    EFD = 105
if flight == "AAP0009":
    departure = "Amsterdam/AMS"
    arrival = "Zurich/ZRH"
    distance = 603
    EFD = 100
if flight == "AAP0010":
    departure = "Zurich/ZRH"
    arrival = "Amsterdam/AMS"
    distance = 603
    EFD = 100
if flight == "AAP0011":
    departure = "Zurich/ZRH"
    arrival = "Sion/SIR"
    distance = 167
    EFD = 45
if flight == "AAP0012":
    departure = "Sion/SIR"
    arrival = "Zurich/ZRH"
    distance = 167
    EFD = 45
if flight == "AAP0013":
    departure = "St Gallen/ACH"
    arrival = "Friedrichshafen/FDH"
    distance = 21
    EFD = 8
    codeshare = "ShibaFly SA"
if flight == "AAP0014":
    departure = "Friedrichshafen/FDH"
    arrival = "St Gallen/ACH"
    distance = 21
    EFD = 8
    codeshare = "ShibaFly SA"
if flight == "AAP2001":
    departure = "Zurich/ZRH"
    arrival = "Boston/BOS"
    distance = 6026
    EFD = 510
if flight == "AAP2002":
    departure = "Boston/BOS"
    arrival = "Zurich/ZRH"
    distance = 6026
    EFD = 510
if flight == "AAP2003":
    departure = "Zurich/ZRH"
    arrival = "Dubai/DBX"
    distance = 4773
    EFD = 370
if flight == "AAP2004":
    departure = "Dubai/DBX"
    arrival = "Zurich/ZRH"
    distance = 4773
    EFD = 370
if flight == "AAP1000":
    departure = "Zurich/ZRH"
    arrival = "Reykjavik/RKV"
    distance = 2617
    EFD = 240
if flight == "AAP1001":
    departure = "Reykjavik/RKV"
    arrival = "Zurich/ZRH"
    distance = 2617
    EFD = 240
if flight == "AAP3000":
    departure = "Zurich/ZRH"
    arrival = "Kuala Lumpur/KUL"
    distance = 10024
    EFD = 900
if flight == "AAP3001":
    departure = "Kuala Lumpur/KUL"
    arrival = "Zurich/ZRH"
    distance = 10024
    EFD = 900
if flight == "AAP3002":
    departure = "Zurich/ZRH"
    arrival = "Tokyo/HND"
    distance = 9610  
    EFD = 780
if flight == "AAP3003":
    departure = "Tokyo/HND"
    arrival = "Zurich/ZRH"
    distance = 9610
    EFD = 780
if flight == "AAP3004":
    departure = "Zurich/ZRH"
    arrival = "Los Angeles/LAX"
    distance = 9556
    EFD = 630
if flight == "AAP3005":
    departure = "Los Angeles/LAX"
    arrival = "Zurich/ZRH"
    distance = 9556
    EFD = 630
if flight == "AAP4000":
    departure = "Gatwick/LGW"
    arrival = "Geneva/GVA"
    distance = 716
    EFD = 95
    codeshare = "ShibaFly SA"
if flight == "AAP4001":
    departure = "Geneva/GVA"
    arrival = "Jersey/JER"
    distance = 705
    EFD = 90
    codeshare = "ShibaFly SA"
if flight == "AAP4002":
    departure = "Jersey/JER"
    arrival = "Gatwick/LGW"
    distance = 259
    EFD = 50
    codeshare = "ShibaFly SA"
print("Be sure to post a screenshot when you post your flight log!")
input("Press Enter to Acknowledge and continue...")
if codeshare == "None":
    print("")
else:
    print("You've flown a Codeshare flight with " + codeshare + "!\nThis means you'll need to log your flight in the AirAlps discord AND " + codeshare + "'s discord server.\n Check the routes channel for an invite.")
if distance == 0:
    print("Sorry, it appears that " + flight + " isn't on our\nroute list or has yet to be added.\nIf you believe this is a mistake, please contact us.\nhttps://discord.gg/GBF7sxxGUw")
    time.sleep(0.5)
    input("Press Enter to exit...")
    exit()
else:
    time.sleep(0.2)
    print("Success! Route found.")
    print("Please type the aircraft you flew. A list of aircraft is provided below.")
    print("Boeing 747-400: Type 744")
    time.sleep(0.08)
    print("Boeing 777-300: Type 773")
    time.sleep(0.08)
    print("Boeing 787-9 Dreamliner: Type 789")
    time.sleep(0.08)
    print("Boeing 767-400ER: Type 764")
    time.sleep(0.08)
    print("Boeing 737 Max 9: Type 739")
    time.sleep(0.08)
    print("Boeing 737 Max 8: Type 738")
    time.sleep (0.08)
    print("REGIONAL FLEET")
    time.sleep (0.08)
    print("BAe 146-300: Type 143")
    time.sleep (0.08)
    print("Embraer ERJ-170: Type 170")
    time.sleep (0.08)
    print("Embraer ERJ-190: Type 190")
    time.sleep (0.08)
    print("Embraer 195-E2: Type 195")
    time.sleep(0.08)
    print("CODESHARE EXCLUSIVE AIRCRAFT:")
    time.sleep (0.08)
    print("Shiba&Co Airbus A320: Type 320")
    aircraftType = input("Type here...")
    if aircraftType == "744":
        efficiency = 9.6
        capacity = 600
        aircraft = "Boeing 747-400"
    if aircraftType == "773":
        efficiency = 8.5
        capacity = 388
        aircraft = "Boeing 777-300ER"
    if aircraftType == "789":
        efficiency = 5.63
        capacity = 290
        aircraft = "Boeing 787-9 Dreamliner"
    if aircraftType == "764":
        efficiency = 5.8
        capacity = 245
        aircraft = "Boeing 767-400ER"
    if aircraftType == "739":
        efficiency = 3.3
        capacity = 178
        aircraft = "Boeing 737 Max 9"
    if aircraftType == "738":
        efficiency = 3.04
        capacity = 170
        aircraft = "Boeing 737 Max"
    if aircraftType == "143":
        efficiency = 2.8
        capacity = 122
        aircraft = "BAe 146-300"
    if aircraftType == "170":
        efficiency = 2.6
        capacity = 72
        aircraft = "Embraer ERJ-170"
    if aircraftType == "190":
        efficiency = 2.8
        capacity = 106
        aircraft = "Embraer ERJ-190"
    if aircraftType == "195":
        efficiency = 3.1
        capacity = 130
        aircraft = "Embraer ERJ-195 E2"
    if aircraftType == "320":
        if codeshare == "None":
            print("The Airbus A320 is only Available for certain Codeshare flights such as AAP4000.\nSee https://discord.com/channels/1093758393505828955/1093786168463720498 for more information.")
        efficiency = 2.79
        capacity = 170
        aircraft = "Shiba&Co Airbus A320"
    X = passengerPerKm * capacity
    Y = X * distance
    A = efficiency * fuelcost
    B = A * distance
    profit = Y - B
    if not codeshare == ("None"):
        profit = profit / 2
    profit = round(profit)
    note = input("Any extra notes? -->")
    def zuluadd(time_str, minutes):
        return (datetime.strptime(time_str, "%H%M") + timedelta(minutes=minutes)).strftime("%H%M")
    Landing = zuluadd(Takeoff, EFD)
    blockIn = zuluadd(Takeoff, -7)
    blockOut = zuluadd(str(Landing), 7)
    blockTime = EFD + 14
    print("--------" + flight + "--------")
    print(">|" + str(date))
    print(">|" + departure + " - " + arrival + "(" + str(distance) + "km)")
    print(">|Aircraft: " + aircraft)
    print("-----")
    print(">|" + flight)
    print(">|Estimated Block Times: " + str(blockIn) + "z" + " - " + str(blockOut) + "z (" + str(blockTime) + "m)")
    print(">|Flight Times: " + str(Takeoff) + "z" + " - " + str(Landing) + "z (" + str(EFD) + "m)")
    print("-----")
    print(">|Profit: " + str(profit))
    print(">|Notes: " + note)
    print("------------------------------------------------------------")
    print("Success! Thank you for flying with us, we hope to see you again!")
    time.sleep(2)
    input("Press enter to finish...")
    exit()


