import json
from random import randint
6688
  
data = {}
with open("MonopolyV2\MonopolyV2.json", "r") as read_file:
    data = json.load(read_file)


class Players:
    
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



####################### FUNCTIONS ###############################


def funct1():
    global Name
    global player1
    subtract = 0
    if Name == 'Mediterranean Avenue' : 
        subtract += 60
    if Name == 'Baltic Avenue' :   
        subtract += 60    
    if Name == 'Reading Railroad' : 
        subtract += 200
    if Name == 'Oriental Avenue' : 
        subtract += 100 
    if Name == 'Vermont Avenue' :      
        subtract += 100
    if Name == 'Connecticut Avenue' :
        subtract += 120
    if Name == 'St. James Place' :  
        subtract += 140
    if Name == 'Electric Company' :   
        subtract += 150
    if Name == 'States Avenue' :    
        subtract += 140
    if Name == 'Virginia Avenue' :     
        subtract += 160
    if Name == 'Pennsylvania Railroad' :
        subtract += 200
    if Name == 'St. Charles Place' :   
        subtract += 180
    if Name == 'Tennessee Avenue' :   
        subtract += 180
    if Name == 'New York Avenue' :
        subtract += 200
    if Name == 'Kentucky Avenue' :
        subtract += 220
    if Name == 'Indiana Avenue' :
        subtract += 220
    if Name == 'Illinois Avenue' :
        subtract += 240
    if Name == 'B. & O. Railroad' :
        subtract += 200
    if Name == 'Atlantic Avenue' :
        subtract += 260
    if Name == 'Ventnor Avenue' :
        subtract += 260
    if Name == 'Water Works' :
        subtract += 150
    if Name == 'Marvin Gardens' :
        subtract += 280
    if Name == 'Pacific Avenue' :
        subtract += 300
    if Name == 'North Carolina Avenue' :
        subtract += 300
    if Name == 'Pennsylvania Avenue' :
        subtract += 320
    if Name == 'Short Line' :
        subtract += 200
    if Name == 'Park Place' :
        subtract += 350
    if Name == 'Boardwalk' :
        subtract += 400

    Name = Name + " = " + str(subtract)

    if player1 == "KEVIN":
        Kevin.SubMoney(subtract)
        Kevin.addProperties(Name)
    if player1 == "ALAN":
        Alan.SubMoney(subtract)
        Alan.addProperties(Name)
    if player1 == "JENNY":
        Jenny.SubMoney(subtract)
        Jenny.addProperties(Name)
    if player1 == "GUO":
        Guo.SubMoney(subtract)
        Guo.addProperties(Name)
    if player1 == "PAM":
        Pam.SubMoney(subtract)
        Pam.addProperties(Name)
    if player1 == "ODI":
        Odi.SubMoney(subtract)
        Odi.addProperties(Name)
    if player1 == "JIMMY":
        Jimmy.SubMoney(subtract)
        Jimmy.addProperties(Name)
    if player1 == "ISIS":
        Isis.SubMoney(subtract)
        Isis.addProperties(Name)

def displayScores():
    Kevin1 = Kevin.getMoney()
    Alan1 = Alan.getMoney()
    Jenny1 = Jenny.getMoney()
    Guo1 = Guo.getMoney()
    Pam1 = Pam.getMoney()
    Odi1 = Odi.getMoney()
    Jimmy1 = Jimmy.getMoney()
    Isis1 = Isis.getMoney()
    list1 = [Kevin1 ,Alan1 ,Guo1 ,Jenny1 ,Pam1 ,Odi1 ,Jimmy1 ,Isis1]
    NamesList = ['Kevin' ,'Alan' ,'Guo' ,'Jenny' ,'Pam' ,'Odi' ,'Jimmy' ,'Isis']
    for i, v in enumerate(list1):
        if not(v == 0):
            print(NamesList[i], ":", list1[i])

def buy():
    global Name
    global player1
    player1 = input("Whos score are you entering in?")
    player1 = player1.upper()
    input1 = input("Enter a color:  ")
    input1 = input1.upper()
    var10 = input1
    var1 = 0
    Name = ""


    if input1 == "BROWN":
        print("1.", data["Brown"][0], "  ", "2.", data["Brown"][1] )
        var1 = input("Select 1 or 2  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Brown"][0]
        elif var1 == 2:
            Name = data["Brown"][1]



    if input1 == "DARK BLUE":
        print("1.", data["Dark Blue"][0], "  ", "2.", data["Dark Blue"][1] )
        var1 = input("Select 1 or 2  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Dark Blue"][0]
        elif var1 == 2:
            Name = data["Dark Blue"][1]


    if input1 == "UTILITIES":
        print("1.", data["Utilities"][0], "  ", "2.", data["Utilities"][1] )
        var1 = input("Select 1 or 2  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Utilities"][0]
        elif var1 == 2:
            Name = data["Utilities"][1]
    #THREE CARDS
    if input1 == "LIGHT BLUE":
        print("1.", data["Light Blue"][0], "  ", "2.", data["Light Blue"][1], "  ", "3.", data["Light Blue"][2] )
        var1 = input("Select 1, 2, or 3  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Light Blue"][0]
        elif var1 == 2:
            Name = data["Light Blue"][1]
        elif var1 == 3:
            Name = data["Light Blue"][2] 

    if input1 == "PINK":
        print("1.", data["Pink"][0], "  ", "2.", data["Pink"][1], "  ", "3.", data["Pink"][2] )
        var1 = input("Select 1, 2, or 3  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Pink"][0]
        elif var1 == 2:
            Name = data["Pink"][1]
        elif var1 == 3:
            Name = data["Pink"][2] 

    if input1 == "ORANGE":
        print("1.", data["Orange"][0], "  ", "2.", data["Orange"][1], "  ", "3.", data["Orange"][2] )
        var1 = input("Select 1, 2, or 3  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Orange"][0]
        elif var1 == 2:
            Name = data["Orange"][1]
        elif var1 == 3:
            Name = data["Orange"][2] 

    if input1 == "YELLOW":
        print("1.", data["Yellow"][0], "  ", "2.", data["Yellow"][1], "  ", "3.", data["Yellow"][2] )
        var1 = input("Select 1, 2, or 3  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Yellow"][0]
        elif var1 == 2:
            Name = data["Yellow"][1]
        elif var1 == 3:
            Name = data["Yellow"][2] 

    if input1 == "GREEN":
        print("1.", data["Green"][0], "  ", "2.", data["Green"][1], "  ", "3.", data["Green"][2] )
        var1 = input("Select 1, 2, or 3  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Green"][0]
        elif var1 == 2:
            Name = data["Green"][1]
        elif var1 == 3:
            Name = data["Green"][2] 

    if input1 == "RED":
        print("1.", data["Red"][0], "  ", "2.", data["Red"][1], "  ", "3.", data["Red"][2] )
        var1 = input("Select 1, 2, or 3  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Red"][0]
        elif 2 == 2:
            Name = data["Red"][1]
        elif var1 == 3:
            Name = data["Red"][2] 



    #FOUR CARDS
    if input1 == "STATIONS":
        print("1.", data["Stations"][0], "  ", "2.", data["Stations"][1], "  ", "2.", data["Stations"][2], "  ", "2.", data["Stations"][3] )
        var1 = input("Select 1, 2, 3, or 4  ")
        var1 = int(var1)
        if var1 == 1:
            Name = data["Stations"][0]
        elif var1 == 2:
            Name = data["Stations"][1]
        elif var1 == 3:
            Name = data["Stations"][2] 
        elif var1 == 4:
            Name = data["Stations"][3] 

def string_list_byChar(str1):
    TYPE = type(str1)
    if TYPE == str:
        return list(str1)
    else:
        return "Input is not a string"

def list_string(list1):
    TYPE = type(list1)
    if TYPE == list:
        str1 = "".join(list1)
        return str1
    else:
        return "Input is not a list"

def logic(option1):
    list1 = string_list_byChar(option1)
    #/K+10
    sign = ""
    person = ""
    if list1[0] == "/":
        list1.remove("/")
        #K+10
        Jproblem = list1[0] + list1[1]
        if Jproblem == "JE":
            person = Jenny
            list1.pop(0)
            list1.pop(0)
        if Jproblem == "JI":
            person = "Jimmy"
            list1.pop(0)
            list1.pop(0)
        if list1[0] == "K":
            person = "Kevin"
            list1.pop(0)
        if list1[0] == "A":
            person = "Alan"
            list1.pop(0)
        if list1[0] == "G":
            person = "Guo"
            list1.pop(0)
        if list1[0] == "P":
            person = "Pam"
            list1.pop(0)
        if list1[0] == "O":
            person = "Odi"
            list1.pop(0)
        if list1[0] == "I":
            person = "Isis"
            list1.pop(0)

        if list1[0] == "+":
            sign = "+"
            list1.pop(0)
        if list1[0] == "-":
            sign = "-"
            list1.pop(0)
        result = list_string(list1)
        nums = result
        
        if person == "Alan":
            Alan2 = eval(sign + nums)
            Alan = Alan.addMoney(Alan2)
        if person == "Kevin":
            Kevin2 = eval(sign + nums)
            Kevin.addMoney(Kevin2)
        if person == 'Guo':
            Guo2 = eval(sign + nums)
            Guo.addMoney(Guo2)
        if person == 'Jenny':
            Jenny2 = eval(sign + nums)
            Jenny.addMoney(Jenny2)
        if person == 'Pam':
            Pam2 = eval(sign + nums)
            Pam.addMoney(Pam2)
        if person == 'Odi':
            Odi2 = eval(sign + nums)
            Odi.addMoney(Odi2)
        if person == 'Jimmy':
            Jimmy2 = eval(sign + nums)
            Jimmy.addMoney(Jimmy2)
        if person == 'Isis':
            Isis2 = eval(sign + nums)
            Isis.addMoney(Isis2)

def rent():
    input2 = input("Type in money  ")
    typeinput2 = type(input2)
    input2 = int(input2)
    input3 = input("From:  ")
    input3 = input3.upper()
    input4 = input("To:  ")
    input4 = input4.upper()
    subtract = input2
    add = input2
    if input4 == "KEVIN":
        Kevin.addMoney(add)
    if input4 == "ALAN":
        Alan.addMoney(add)
    if input4 == "JENNY":
        Jenny.addMoney(add)
    if input4 == "GUO":
        Guo.addMoney(add)
    if input4 == "PAM":
        Pam.addMoney(add)
    if input4 == "ODI":
        Odi.addMoney(add)
    if input4 == "JIMMY":
        Jimmy.addMoney(add)
    if input4 == "ISIS":
        Isis.addMoney(add)


    if input3 == "KEVIN":
        Kevin.SubMoney(subtract)
    if input3 == "ALAN":
        Alan.SubMoney(subtract)
    if input3 == "GUO":
        Guo.SubMoney(subtract)
    if input3 == "JENNY":
        Jenny.SubMoney(subtract)
    if input3 == "PAM":
        Pam.SubMoney(subtract)
    if input3 == "ODI":
        Odi.SubMoney(subtract)
    if input3 == "JIMMY":
        Jimmy.SubMoney(subtract)
    if input3 == "ISIS":
        Isis.SubMoney(subtract)

def special():
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis
    print("1. Properties Lists")
    print("2. pass go get 200")
    print("3. Money grab")
    print("4. Give Everyone X")
    print("5. Recover data")
    print("6. Collect X from everybody")
    print("7. Timer :(")
    SInput = input("Choose a number:   ")
    if SInput == "1":
        var1 = input("Who's properties do you want to display?")
        var1 = var1.upper()
        if var1 == "KEVIN":
            print("Kevin's Properties:", Kevin.getProperties())
        if var1 == "ALAN":
            var2 = Alan.getProperties()
            print("Alan's Properties:", var2)
        if var1 == "JENNY":
            var2 = Jenny.getProperties()
            print("Jenny's Properties:", var2)
        if var1 == "GUO":
            var2 = Guo.getProperties()
            print("Guo's Properties:", var2)
        if var1 == "PAM":
            var2 = Pam.getProperties()
            print("Pam's Properties:", var2)
        if var1 == "ODI":
            var2 = Odi.getProperties()
            print("Odi's Properties:", var2)
        if var1 == "JIMMY":
            var2 = Jimmy.getProperties()
            print("Jimmy's Properties:", var2)
        if var1 == "ISIS":
            var2 = Isis.getProperties()
            print("Isis's Properties:", var2)

    if SInput == '2':
        var1 = input("Who Passed Go?  ")
        var1 = var1.upper()
        if var1 == "KEVIN":
            Kevin.addMoney(200)
        if var1 == "ALAN":
            Alan.addMoney(200)     
        if var1 == "JENNY":
            Jenny.addMoney(200)
        if var1 == "GUO":
            Guo.addMoney(200)
        if var1 == "PAM":
            Pam.addMoney(200)
        if var1 == "ODI":
            Odi.addMoney(200)
        if var1 == "JIMMY":
            Jimmy.addMoney(200)
        if var1 == "ISIS":
            Isis.addMoney(200)

    if SInput == '3':
        list20 = ["Kevin  = ", "Alan = ", "Jenny = ", "Guo = ", "Pam = ", "Odi = ", "Jimmy = ", "Isis = "]
        list2 = []
        for i in range(0, 8, 1):
            var1 = str(randint(1, 8))
            var1 = int(var1+"00")
            list2.append(var1)
            print(list20[i], list2[i])
        var2 = input("Would you like to automatically input the score to the people currently playing?")
        var2 = var2.upper()
        if var2 == "YES" or var2 == "Y":
            list1 = [Kevin.getMoney() ,Alan.getMoney() , Jenny.getMoney() ,Guo.getMoney() ,Pam.getMoney() ,Odi.getMoney() ,Jimmy.getMoney() ,Isis.getMoney()]
            for i in range(0,8,1):
                if list1[i] != 0:
                    list1[i] = list1[i] + list2[i]

            Kevin.setMoney(list1[0])
            Alan.setMoney(list1[1])
            Jenny.setMoney(list1[2])
            Guo.setMoney(list1[3])
            Pam.setMoney(list1[4])
            Odi.setMoney(list1[5])
            Jimmy.setMoney(list1[6])
            Isis.setMoney(list1[7])

    if SInput == "4":
        loser = input("Who is losing Money:  ")
        loser = loser.upper()
        money = int(input("How much are they giving per person."))
        list1 = [Kevin.getMoney() ,Alan.getMoney() , Jenny.getMoney() ,Guo.getMoney() ,Pam.getMoney() ,Odi.getMoney() ,Jimmy.getMoney() ,Isis.getMoney()] 
        NumPlayers = 0
        for i in range(0,8,1):
            if list1[i] != 0:
                NumPlayers += 1
        list2 = ["KEVIN", "ALAN", "JENNY", "GUO", "PAM", "ODI", "JIMMY", "ISIS"]
        if loser == "KEVIN":
            Kevin.SubMoney(money*NumPlayers)
        if loser == "ALAN":
            Alan.SubMoney(money*NumPlayers)
        if loser == "JENNY":
            Jenny.SubMoney(money*NumPlayers)
        if loser == "GUO":
            Guo.SubMoney(money*NumPlayers)
        if loser == "PAM":
            Pam.SubMoney(money*NumPlayers)
        if loser == "ODI":
            Odi.SubMoney(money*NumPlayers)
        if loser == "JIMMY":
            Jimmy.SubMoney(money*NumPlayers)
        if loser == "ISIS":
            Isis.SubMoney(money*NumPlayers)
        list1 = [Kevin.getMoney() ,Alan.getMoney() , Jenny.getMoney() ,Guo.getMoney() ,Pam.getMoney() ,Odi.getMoney() ,Jimmy.getMoney() ,Isis.getMoney()] 
        for i in range(0,8,1):
            if i != 0:
                list1[i] = list1[i] + money
        Kevin.setMoney(list1[0])
        Alan.setMoney(list1[1])
        Jenny.setMoney(list1[2])
        Guo.setMoney(list1[3])
        Pam.setMoney(list1[4])
        Odi.setMoney(list1[5])
        Jimmy.setMoney(list1[6])
        Isis.setMoney(list1[7])

    if SInput == "5":
        with open('RecovMoney.json') as RecovMoney:
            LRecovMoney = json.load(RecovMoney)

            print("data= ", LRecovMoney)
        with open('RecovProperty.json') as RecovProperty:
            LRecovProperty = json.load(RecovProperty)

        Kevin = Players("Kevin", LRecovMoney[0], LRecovProperty[0])
        Alan = Players("Alan", LRecovMoney[1], LRecovProperty[1])
        Guo = Players("Guo", LRecovMoney[2], LRecovProperty[2])
        Jenny = Players("Jenny", LRecovMoney[3], LRecovProperty[3])
        Pam = Players("Pam", LRecovMoney[4], LRecovProperty[4])
        Odi = Players("Odi", LRecovMoney[5], LRecovProperty[5])
        Jimmy = Players("Jimmy", LRecovMoney[6], LRecovProperty[6])
        Isis = Players("Isis", LRecovMoney[7], LRecovProperty[7])

    if SInput == "6":
        winner = input("Who is getting all the money?")
        winner = winner.upper()
        money = int(input("How much are they getting per person."))
        list1 = [Kevin.getMoney() ,Alan.getMoney() , Jenny.getMoney() ,Guo.getMoney() ,Pam.getMoney() ,Odi.getMoney() ,Jimmy.getMoney() ,Isis.getMoney()] 
        NumPlayers = 0
        for i in range(0,8,1):
            if list1[i] != 0:
                NumPlayers += 1
        list2 = ["KEVIN", "ALAN", "JENNY", "GUO", "PAM", "ODI", "JIMMY", "ISIS"]
        if winner == "KEVIN":
            Kevin.addMoney(money*NumPlayers)
        if winner == "ALAN":
            Alan.addMoney(money*NumPlayers)
        if winner == "JENNY":
            Jenny.addMoney(money*NumPlayers)
        if winner == "GUO":
            Guo.addMoney(money*NumPlayers)
        if winner == "PAM":
            Pam.addMoney(money*NumPlayers)
        if winner == "ODI":
            Odi.addMoney(money*NumPlayers)
        if winner == "JIMMY":
            Jimmy.addMoney(money*NumPlayers)
        if winner == "ISIS":
            Isis.addMoney(money*NumPlayers)
        list1 = [Kevin.getMoney() ,Alan.getMoney() , Jenny.getMoney() ,Guo.getMoney() ,Pam.getMoney() ,Odi.getMoney() ,Jimmy.getMoney() ,Isis.getMoney()] 
        for i in range(0,8,1):
            if i != 0:
                list1[i] = list1[i] - money
        Kevin.setMoney(list1[0])
        Alan.setMoney(list1[1])
        Jenny.setMoney(list1[2])
        Guo.setMoney(list1[3])
        Pam.setMoney(list1[4])
        Odi.setMoney(list1[5])
        Jimmy.setMoney(list1[6])
        Isis.setMoney(list1[7])
    
    if SInput == "7":
        global time
        global extend
        time = int(input("\nHow long do you want to set a timer for? (mins)  \n"))
        time = time * 60  
        extend = 3
        def Extend(): 
            timer = threading.Timer(600, Done2)
            timer.start() 
            main()
        def Done(): 
            global time
            global extend
            print(time ,"min has passed ")
            if extend > 0:
                text = "\n Would you like to extend the game by 10 minutes, you can only do this " + str(extend) + " more times \n"
                var1 = input(text)
                var1 = var1.upper()
                if var1 == "YES" or var1 == "Y":
                    Extend()
                    extend -= 1
                if var1 == "NO" or var1 == "N":
                    exit()
        def Done2(): 
            global time
            global extend
            print("\n 10 min has passed \n")
            if extend > 0:
                text = "\n Would you like to extend the game by 10 minutes, you can only do this " + str(extend) + " more times \n"
                var1 = input(text)
                var1 = var1.upper()
                if var1 == "YES" or var1 == "Y":
                    Extend()
                    extend -= 1
                if var1 == "NO" or var1 == "N":
                    exit()

        timer = threading.Timer(time, Done)
        timer.start() 

#################################################################
Kevin = None
Alan = None
Guo = None
Jenny = None
Pam = None
Odi = None
Jimmy = None
Isis = None

##################INPUT CODE######################

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

for i, v in enumerate(list1):
    if v == "Y" or v =="YES":
        list2.append(1500)
    if v == "N" or v =="NO":
        list2.append(0)

#####################################################

#Kevin Alan Guo Jenny Pam Odi Jimmy Isis
list1 = list2

LKevin = []
LAlan = []
LGuo = []
LJenny = []
LPam = []
LOdi = []
LJimmy = []
LIsis = []

Kevin = Players("Kevin", list1[0], LKevin)
Alan = Players("Alan", list1[1], LAlan)
Guo = Players("Guo", list1[2], LGuo)
Jenny = Players("Jenny", list1[3], LJenny)
Pam = Players("Pam", list1[4], LPam)
Odi = Players("Odi", list1[5], LOdi)
Jimmy = Players("Jimmy", list1[6], LJimmy)
Isis = Players("Isis", list1[7], LIsis)

def main():
    option1 = str(input("Rent, Buy, or Special: "))
    option1 = option1.upper()
    if option1 == "R":
        option1 = "RENT"
    if option1 == "B":
        option1 = "BUY"
    if option1 == "S":
        option1 = "SPECIAL"
    try:
        logic(option1)
    except:
        pass
    if option1 != "BUY" and option1 != "RENT" and option1 != "SPECIAL":
        displayScores()

    try:
        if option1 == "BUY":
            buy()
            funct1()
            displayScores()
    except:
        print("Error")
        print("I'd bet ur glad that u coded this fail safe")
    try:
        if option1 == "RENT":
            rent()
            displayScores()
    except:
        print("Error")
        print("You typed a string idiot, you wrote this code how the hell do u not know")
        print("I'd bet ur glad that u coded this fail safe")
    try:
        if option1 == "SPECIAL":
            special()
            displayScores()
    except:
        print("Error")
        print("I'd bet ur glad that u coded this fail safe")
    try:
        RecovMoney = [Kevin.getMoney(), Alan.getMoney(), Guo.getMoney(),
                    Jenny.getMoney(), Pam.getMoney(), Odi.getMoney(),
                    Jimmy.getMoney(), Isis.getMoney()]
        RecovProperty = [Kevin.getProperties(), Alan.getProperties(), Guo.getProperties(),
                        Jenny.getProperties(), Pam.getProperties(), Odi.getProperties(),
                        Jimmy.getProperties(), Isis.getProperties()]
        with open('RecovMoney.json','w') as f:
            json.dump(RecovMoney, f)
        with open('RecovProperty.json','w') as f:
            json.dump(RecovProperty, f)
    except:
        print("Error")
        print("Uhhh, kevin I dont think you have the recovery file in the same folder")

while(1):
    main()