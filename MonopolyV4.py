
import json
import random as r
import copy
from Players import Players
from Rent import Rent
from Property import Property
'''
print("Decide the order?, or let the program do it")
print("1. I'll do it the old fasion way. (roll dice)")
print("2. let the program do it")
decide = int(input())

if decide == 1:
    PlayerNames = input("Type the name of each player seperated by a comma.")
    PlayerNames = PlayerNames.split(",")

if decide == 2:
    PlayerNames = input("Type the name of each player seperated by a space.")
    PlayerNames = PlayerNames.split()
    print("Randomizing order...")
    r.shuffle(PlayerNames)
    print("Order Randomized")
print("Playernames", PlayerNames)
'''
PlayerNames = ["kevin", "Alan", "Odi", "Pam"]

player = Players()
rent = Rent()
property = Property()

PositionList = ["GO","Mediterranean_Avenue","Community_Chest","Baltic_Avenue","Income_Tax","Reading_Railroad","Oriental_Avenue","Chance",
                "Vermont_Avenue","Connecticut_Avenue","Jail","St._Charles_Place","Eletric_Company","States_Avenue","Virginia_Avenue","Pennsylvania_Railroad",
                "St._James_Place","Community_Chest","Tennessee_Avenue","New_York_Avenue","Free_Parking","Kentucky_Avenue","Chance","Indiana_Avenue",
                "Illinois_Avenue","B._&_O._Railroad","Atlantic_Avenue","Ventnor_Avenue","Water_Works","Marvin_Gardens","Go_To_Jail","Pacific_Avenue",
                "North_Carolina_Avenue","Community_Chest","Pennsylvania_Avenue", "Short_Line","Chance","Park_Place", "Luxury_Tax","Boardwalk"]


for i in range(0, len(PlayerNames),1):
    player.addPlayer(PlayerNames[i])
    player.updateRollDiceOrder(PlayerNames[i], i)
    inputStr = "What is " + PlayerNames[i] + "'s Icon"
    icon = str(input(inputStr))
    player.updateIcon(PlayerNames[i], icon)



for i in PlayerNames:
    player.

Rolling = 0
for i in range(0, len(PlayerNames),1):



    Rolling += 1


