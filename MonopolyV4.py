
import json
import random as r
import copy
from Players import Players
from Rent import Rent
from Property import Property
import time

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


player = Players()
rent = Rent()
property = Property()


for i in range(0, len(PlayerNames),1):
    player.addPlayer(PlayerNames[i])
    player.updateRollDiceOrder(PlayerNames[i], i)
    #inputStr = "What is " + PlayerNames[i] + "'s Icon: "
    #icon = str(input(inputStr))
    #player.updateIcon(PlayerNames[i], icon)



class runningLoop:
    def __init__(self):
        self.count = 0
        self.PositionList = ["GO","Mediterranean_Avenue","Community_Chest","Baltic_Avenue","Income_Tax","Reading_Railroad","Oriental_Avenue","Chance",
                             "Vermont_Avenue","Connecticut_Avenue","Jail","St._Charles_Place","Eletric_Company","States_Avenue","Virginia_Avenue","Pennsylvania_Railroad",
                             "St._James_Place","Community_Chest","Tennessee_Avenue","New_York_Avenue","Free_Parking","Kentucky_Avenue","Chance","Indiana_Avenue",
                             "Illinois_Avenue","B._&_O._Railroad","Atlantic_Avenue","Ventnor_Avenue","Water_Works","Marvin_Gardens","Go_To_Jail","Pacific_Avenue",
                             "North_Carolina_Avenue","Community_Chest","Pennsylvania_Avenue", "Short_Line","Chance","Park_Place", "Luxury_Tax","Boardwalk"]
        self.Hotelslist = ["Mediterranean_Avenue","Baltic_Avenue","Reading_Railroad","Oriental_Avenue",
                             "Vermont_Avenue","Connecticut_Avenue","St._Charles_Place","Eletric_Company","States_Avenue","Virginia_Avenue","Pennsylvania_Railroad",
                             "St._James_Place","Tennessee_Avenue","New_York_Avenue","Kentucky_Avenue","Indiana_Avenue",
                             "Illinois_Avenue","B._&_O._Railroad","Atlantic_Avenue","Ventnor_Avenue","Water_Works","Marvin_Gardens","Pacific_Avenue",
                             "North_Carolina_Avenue","Pennsylvania_Avenue", "Short_Line","Park_Place","Boardwalk"]

    def startLooping(self, loopingList):


        triplelD= 0
        while (self.count < len(loopingList)):
            if triplelD == 3:
                player.updatePosition(loopingList[self.count], "Jail")
                player.updateJailStatus(loopingList[self.count], "True")
                totalJ = 0
                for i in PlayerRolls:
                    totalJ = totalJ + i
                if totalJ >= 40:
                    totalJ = totalJ % 40
                print("Total: ",total)
                steptojail = 10 - totalJ
                player.addRolls(loopingList[self.count],steptojail)
                self.goForwardCount(1)
                triplelD = 0


            player.listCurentPlayers()



            doubleStatus = 0
            #time.sleep(1) 
            loopinglen = len(loopingList) -1
            if self.count == len(loopingList):
                self.count = 0
            print("self.count =", self.count)

            print("It is", loopingList[self.count], "'s turn")

            PlayerRolling = loopingList[self.count]


            mainInput1= int(input("Enter your first roll:"))
            mainInput2 = int(input("Enter your Second roll:"))
            
            if mainInput1 > 6 or mainInput2 > 6:
                print("You rolled is greater than 6, geez what dice are you using.")
                print("Try again.")
                mainInput1= int(input("Enter your first roll:"))
                mainInput2 = int(input("Enter your Second roll:"))

            mainInput = mainInput1 + mainInput2

            player.addRolls(PlayerRolling,mainInput)
            PlayerRolls = player.getRolls(PlayerRolling)
            total = 0
            for i in PlayerRolls:
                total = total + i
            if total >= 40:
                amount1 = player.getAmount(loopingList[self.count])
                passGo = amount1 + 200
                player.setAmount(loopingList[self.count],passGo)
                total = total % 40
            player.updatePosition(loopingList[self.count], self.PositionList[total])

            
            '''
            position = player.getPosition(loopingList[self.count])
            for i in self.Hotelslist:
                #check it its a hotel and not a chance or a chest
                if position == i:
                    status = property.getStatus(position)
                    if status == 0:
                        print("Do you want to buy", player.getPosition(loopingList[self.count]) ,"? : ")
                        inputbuy = input("Yes, No: ")
                        inputbuy = inputbuy.upper()
                        if inputbuy == "Y":
                            inputbuy = "YES"
                        if inputbuy == "N": 
                            inputbuy = "NO"
                        if inputbuy == "YES":
                            propertyBuying = player.getPosition(loopingList[self.count])
                            propPrice = property.getPrice(propertyBuying)
                            amountP = player.getAmount(loopingList[self.count])
                            print(amountP)
                            if amountP >= propPrice:
                                amountP = amountP - propPrice
                                print(amountP)
                                player.setAmount(loopingList[self.count], amountP)
                    if status == 1:
                        pass
                            
            '''

            





            ### Double or no
            if mainInput1 == mainInput2:
                doubleStatus += 1
            if not(doubleStatus == 0):
                self.goBackCount(2)
                triplelD += 1
            else:
                self.goBackCount(1)
                triplelD = 0


            self.count += 1

            if self.count == len(loopingList) - 1:
                self.count = 0
            else:
                self.count += 1

            '''
            if testCount == 3: 
                self.goBackCount(2)


            if testCount == 9:
                self.goForwardCount(1)

                
            if testCount == 12:
                self.exitRunningLoop()
            else:
                testCount += 1            
            '''






            ######Reset varibles############
            
            
            
    def exitRunningLoop(self):
        self.count = 999

    def goBackCount(self, backCount):
        self.count = self.count - backCount

    def goForwardCount(self, forwardCount):
        self.count = self.count + forwardCount


def main():
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