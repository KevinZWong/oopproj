
import json
import random as r
import copy
from Players import Players
from Rent import Rent
from Property import Property
import time

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
    inputStr = "What is " + PlayerNames[i] + "'s Icon: "
    icon = str(input(inputStr))
    player.updateIcon(PlayerNames[i], icon)



class runningLoop:
    def __init__(self):
        self.count = 0

    def startLooping(self, loopingList):
        
        testCount = 0
        while (self.count < len(loopingList)):
            time.sleep(1) 
            print("self.count =", self.count)

            print("It is", loopingList[self.count], "'s turn")

            PlayerRolling = loopingList[self.count]
            mainInput = input("Enter your roll:")
            player.addRolls(PlayerRolling,mainInput)
            PlayerRolls = getRolls(PlayerRolling)
            total = 0
            for i in PlayerRolls:
                total = total + i


            '''
            if testCount == 3: 
                self.goBackCount(2)


            if testCount == 9:
                self.goForwardCount(1)
            

            if testCount == 12:
                self.exitRunningLoop()
            else:
                testCount += 1            
            
            if self.count == len(loopingList) - 1:
                self.count = 0
            else:
                self.count += 1
            '''
    def exitRunningLoop(self):
        self.count = 999

    def goBackCount(self, backCount):
        self.count = self.count - backCount

    def goForwardCount(self, forwardCount):
        self.count = self.count + forwardCount


def main():
    PlayerNames = ["kevin", "Alan", "Odi", "Pam"]
    obj = runningLoop()
    obj.startLooping(PlayerNames)






if __name__ == "__main__":
    print("To run Players class directly")
    main()
else:
    print("To run Players being imported")





















    '''

PlayerRolling = "kevin"
mainInput = input("Enter your roll:")
player.addRolls(PlayerRolling,mainInput)
PlayerRolls = getRolls(PlayerRolling)
total = 0
for i in PlayerRolls:
    total = total + i


'''