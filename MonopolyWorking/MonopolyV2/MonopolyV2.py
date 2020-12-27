import json
from random import randint

data = {}
with open("C:/Users/kevin/AC/Monopoly/MonopolyV2.json", "r") as read_file:
    data = json.load(read_file)
###############FUCTIONS################

def players(list1):
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis
    for i in list1:
        if i == "KEVIN":
            Kevin = 1500
        if i == "ALAN":
            Alan = 1500
        if i == "JENNY":
            Jenny = 1500
        if i == "GUO":
            Guo = 1500
        if i == "ODI":
            Odi = 1500
        if i == "PAM":
            Pam = 1500
        if i == "JIMMY":
            Jimmy = 1500
        if i == "ISIS":
            Isis = 1500
    
def display():
    global subtract
    global player1
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis

    if player1 == "KEVIN" and Kevin > 0:
        Kevin = Kevin - subtract
    if player1 == "ALAN" and Alan > 0:
        Alan = Alan - subtract
    if player1 == "GUO" and Guo > 0:
        Guo = Guo - subtract
    if player1 == "JENNY" and Jenny > 0:
        Jenny = Jenny - subtract

    if player1 == "PAM" and Pam > 0:
        Pam = Pam - subtract
    if player1 == "ODI" and Odi > 0:
        Odi = Odi - subtract
    if player1 == "JIMMY" and Jimmy > 0:
        Jimmy = Jimmy - subtract
    if player1 == "ISIS" and Isis > 0:
        Isis = Isis - subtract

def funct1():
    global subtract
    global Name
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

def buy():
    global var10
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

def rent():
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis
    input2 = input("Type in money  ")
    input2 = int(input2)
    input3 = input("From:  ")
    input3 = input3.upper()
    input4 = input("To:  ")
    input4 = input4.upper()
    subtract = input2
    add = input2
    if input4 == "KEVIN":
        Kevin = Kevin + add
    if input4 == "GUO":
        Guo = Guo + add
    if input4 == "PAM":
        Pam = Pam + add
    if input4 == "ODI":
        Odi = Odi + add
    if input3 == "KEVIN":
        Kevin = Kevin - subtract
    if input3 == "GUO":
        Guo = Guo - subtract
    if input3 == "PAM":
        Pam = Pam - subtract
    if input3 == "ODI":
        Odi = Odi - subtract

def giveall(var1, list10):
        if var1 == "Kevin" and Kevin > 0:
            players = players + 1
        if var1 == "Alan" and Alan > 0:
            players = players + 1
        if var1 == "Guo" and Guo > 0:
            players = players + 1
        if var1 == "Jenny" and Jenny > 0:
            players = players + 1

        if var1 == "Pam" and Pam > 0:
            players = players + 1
        if var1 == "Odi" and Odi > 0:
            players = players + 1
        if var1 == "Jimmy" and Jimmy > 0:
            players = players + 1
        if var1 == "Isis" and Isis > 0:
            players = players + 1

def special():
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis
    print("1. Properties List")
    print("2. pass go get 200")
    print("3. Money grab")
    SInput = int(input("Choose a number:   "))
    var1 = ""
    if SInput == 1:
        var1 = input("Who's property list do you want to display?   ")
        var1 = var1.upper()
        if var1 == "KEVIN":
            print("Kevin:  ", LKevin)
        if var1 == "ALAN":
            print("Alan:  ", LAlan)
        if var1 == "GUO":
            print("Guo:  ", LGuo)
        if var1 == "JENNY":
            print("Jenny:  ", LJenny)
        if var1 == "PAM":
            print("Pam:  ", LPam)
        if var1 == "ODI":
            print("Odi:  ", LOdi)
        if var1 == "JIMMY":
            print("Jimmy:  ", LJimmy)
        if var1 == "ISIS":
            print("Isis:  ", LIsis)
         
    if SInput == 2:
        var1 = input("Who passed go?   ")
        var1 = var1.upper()
        if var1 == "KEVIN":
            Kevin = Kevin + 200
        if var1 == "ALAN":
            Alan = Alan +  200
        if var1 == "GUO":
            Guo = Guo + 200
        if var1 == "JENNY":
            Jenny = Jenny + 200
        if var1 == "PAM":
            Pam = Pam + 200
        if var1 == "ODI":
            Odi = Odi + 200
        if var1 == "JIMMY":
            Jimmy = Jimmy + 200
        if var1 == "ISIS":
            Isis += Isis + 200

    if SInput == 3:
        list20 = ["Kevin  = ", "Alan = ", "Guo = ", "Jenny = ", "Pam = ", "Odi = ", "Jimmy = ", "Isis = "]
        for i in range(0, 8, 1):
            var1 = str(randint(1, 8))
            print(list20[i], var1 + "00")

    if SInput == 4:
        print("Hello World")

    print("=======================")

def listNames():
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis
    if player1 == "KEVIN":
        LKevin.append(Name)
    if player1 == "ALAN":
        LAlan.append(Name)
    if player1 == "GUO":
        LGuo.append(Name)
    if player1 == "JENNY":
        LJenny.append(Name)

    if player1 == "PAM":
        LPam.append(Name)
    if player1 == "ODI":
        LOdi.append(Name)
    if player1 == "JIMMY":
        LJimmy.append(Name)
    if player1 == "ISIS":
        LIsis.append(Name)

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
    global Kevin
    global Alan
    global Guo
    global Jenny
    global Pam
    global Odi
    global Jimmy
    global Isis
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
            Alan = eval(str(Alan) + sign + nums)
            Alan = int(Alan)
        if person == "Kevin":
            Kevin = eval(str(Kevin) + sign + nums)
            Kevin = int(Kevin)
        if person == 'Guo':
            Guo = eval(str(Guo) + sign + nums)
            Guo = int(Guo)
        if person == 'Jenny':
            Jenny = eval(str(Jenny) + sign + nums)
            Jenny = int(Jenny)
        if person == 'Pam':
            Pam = eval(str(Pam) + sign + nums)
            Pam = int(Pam)
        if person == 'Odi':
            Odi = eval(str(Odi) + sign + nums)
            Odi = int(Odi)
        if person == 'Jimmy':
            Jimmy = eval(str(Jimmy) + sign + nums)
            Jimmy = int(Jimmy)
        if person == 'Isis':
            Isis = eval(str(Isis) + sign + nums)
            Isis = int(Isis)
                 

#######################################


#var1 = input("Select 1, 2, or 3")
#TWO CARDS
list1 = []
list2 = []
Kevin = 0
Alan = 0
Guo = 0
Jenny = 0
Pam = 0
Odi = 0
Jimmy = 0
Isis = 0

LKevin = []
LAlan = []
LGuo = []
LJenny = []
LPam = []
LOdi = []
LJimmy = []
LIsis = []


people = ""
print("Type in the players and 0 to exit")
while people != "0":
    people = input("Who is playing:  ")
    people = people.upper()
    list1.append(people)
    players(list1)

while(1):
    option1 = input("Rent, Buy, or Special: ")
    option1 = option1.upper()
    if option1 == "R":
        option1 = "RENT"
    if option1 == "B":
        option1 = "BUY"
    if option1 == "S":
        option1 = "SPECIAL"

    logic(option1)



    if option1 == "BUY":
        buy()
        funct1()
        display()

    if option1 == "RENT":
        rent()
    if option1 == "SPECIAL":
        special()






    if Kevin > 0:
        print("Kevin = ", Kevin)
    if Alan > 0:
        print("Alan = ", Alan)
    if Guo > 0:
        print("Guo = ", Guo)
    if Jenny > 0:
        print("Jenny = ", Jenny)
    if Pam > 0:
        print("Pam = ", Pam)
    if Odi > 0:
        print("Odi = ", Odi)
    if Jimmy > 0:
        print("Jimmy = ", Jimmy)
    if Isis > 0:
        print("Isis = ", Isis)