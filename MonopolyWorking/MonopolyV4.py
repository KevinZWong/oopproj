
import json
from random import randint
with open("KevinOOP\default_properties.json", "r") as read_file:
    data = json.load(read_file)



class MoneyProperty:
    def __init__(self, name, money, properties):
      self.name = name
      self.money = money
      self.properties = properties
   
    def getMoney(self):
        #print(self.name,":",self.money)
        return int(self.money)

    def getProperties(self):
        #print(self.name,":",self.properties)
        return self.properties

    def setMoney(self, var1):
        self.money = var1

    def addProperties(self, var1):
        self.properties.append(str(var1))

    def ClearProperties(self, var1):
        for i in (0, len(self.properties), 1):
            self.properties.pop[0]

    def addMoney(self, var1):
        self.money = var1 + self.money

    def SubMoney(self, var1):
        self.money = self.money - var1 

class properties():
    def __init__(self, owner, property, status):
        self.owner = owner
        self.property = property
        self.status = status
    def buyProperty(self, color, number):
        LProperty = ["Mediterranean_Avenue","Baltic_Avenue","Reading_Railroad","Oriental_Avenue","Vermont_Avenue",
                     "Connecticut_Avenue","St._James_Place","Electric_Company","States_Avenue","Virginia_Avenue",
                     "Pennsylvania_Railroad","St._Charles_Place","Tennessee_Avenue","New_York_Avenue","Kentucky_Avenue",
                     "Indiana_Avenue","Illinois_Avenue","B._&_O._Railroad","Atlantic_Avenue","Ventnor_Avenue","Water_Works",
                     "Marvin_Gardens","Pacific_Avenue","North_Carolina_Avenue","Pennsylvania_Avenue","Pennsylvania_Avenue","Short_Line",
                     "Park_Place","Boardwalk",]
        for i in LProperty:
            var1 = data[i]["Type"]
            print(var1)

player1 = properties("kevin", "red",LProperty)


'''
NumPlayers = int(input("How many people are playing?, max set to 10:  "))
PlayerNames = []
print("Decide the order?, or let the program do it")
print("1. I'll do it the old fasion way.")
print("2. let the program do it")
decide = int(input())
if decide == 1:
    for i in range(1,NumPlayers+1,1):
        name = input("Name of player in order", i,": ")
        PlayerNames.append(name)

if decide == 2:
    for i in range(1,NumPlayers+1,1):
        display = "Names of player"+ str(i) + ":    "
        name = input(display)
        PlayerNames.append(name)
    random.shuffle(PlayerNames)
    print("The order:")


print(PlayerNames)
counter1 = 0
if counter1 < NumPlayers:
    player1 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player2 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player3 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player4 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player5 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player6 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player7 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player8 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player9 = Players(i, LMoney,LProperty)
    counter1 += 1
if counter1 < NumPlayers:
    player10 = Players(i, LMoney,LProperty)
    counter1 += 1




'''

##### KINDA USELESS CODE ################

'''

#Kevin Alan Guo Jenny Pam Odi Jimmy Isis
NamesList = ['Kevin' ,'Alan' ,'Guo' ,'Jenny' ,'Pam' ,'Odi' ,'Jimmy' ,'Isis']
list1 = []
people = ""
for i in NamesList:
    can1 = "Is " + i + " playing?"
    people = input(can1)
    people = people.upper()
    list1.append(people)
list2 = []
counter = 0
for i, v in enumerate(list1):
    if v == "Y" or v =="YES":
        list2.append(1500)
    
    if v == "N" or v =="NO":
        list2.append(0)
if counter >= 6:
    print("There are a lot of people playing this game, \nI would suggest rolling around the map first \nbefore actually purchasing any properties so \nthat way its more far of a starting point.")

'''