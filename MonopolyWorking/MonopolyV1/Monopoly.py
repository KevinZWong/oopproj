Kevin = 1500
Guo = 1500
Pam = 1500
Odi = 1500
list1 = ["Mediterranean Avenue","Baltic Avenue","Reading Railroad","Oriental Avenue","Vermont Avenue",
         "Connecticut Avenue","St. James Place","Electric Company","States Avenue","Virginia Avenue",
         "Pennsylvania Railroad","St. Charles Place","Tennessee Avenue","New York Avenue","Kentucky Avenue",
         "Indiana Avenue","Illinois Avenue","B. & O. Railroad","Atlantic Avenue","Ventnor Avenue","Water Works",
         "Marvin Gardens","Pacific Avenue","North Carolina Avenue","Pennsylvania Avenue","Pennsylvania Avenue","Short Line",
         "Park Place","Boardwalk",]

def funct1():
    global subtract
    global input1
    subtract = 0

    if input1 == 'Mediterranean Avenue' : 
        subtract += 60
    if input1 == 'Baltic Avenue' :   
        subtract += 60    
    if input1 == 'Reading Railroad' : 
        subtract += 200
    if input1 == 'Oriental Avenue' : 
        subtract += 100 
    if input1 == 'Vermont Avenue' :      
        subtract += 100
    if input1 == 'Connecticut Avenue' :
        subtract += 120
    if input1 == 'St. James Place' :  
        subtract += 140
    if input1 == 'Electric Company' :   
        subtract += 150
    if input1 == 'States Avenue' :    
        subtract += 140
    if input1 == 'Virginia Avenue' :     
        subtract += 160
    if input1 == 'Pennsylvania Railroad' :
        subtract += 200
    if input1 == 'St. Charles Place' :   
        subtract += 180
    if input1 == 'Tennessee Avenue' :   
        subtract += 180
    if input1 == 'New York Avenue' :
        subtract += 200
    if input1 == 'Kentucky Avenue' :
        subtract += 220
    if input1 == 'Indiana Avenue' :
        subtract += 220
    if input1 == 'Illinois Avenue' :
        subtract += 240
    if input1 == 'B. & O. Railroad' :
        subtract += 200
    if input1 == 'Atlantic Avenue' :
        subtract += 260
    if input1 == 'Ventnor Avenue' :
        subtract += 260
    if input1 == 'Water Works' :
        subtract += 150
    if input1 == 'Marvin Gardens' :
        subtract += 280
    if input1 == 'Pacific Avenue' :
        subtract += 300
    if input1 == 'North Carolina Avenue' :
        subtract += 300
    if input1 == 'Pennsylvania Avenue' :
        subtract += 320
    if input1 == 'Short Line' :
        subtract += 200
    if input1 == 'Park Place' :
        subtract += 350
    if input1 == 'Boardwalk' :
        subtract += 400

while(1):
    player1 = input("Whos score are you entering in? Kevin, Guo, Pam, or Odi, or mchange  ")
    if player1 == "mchange":
        input2 = input("Type in money  ")
        input2 = int(input2)
        input3 = input("Enter the person who the money is being taken away")
        input4 = input("Enter the person who is getting the money")
        player1 = input3
        player2 = input4
        subtract = input2
        add = input2
        if player2== "Kevin":
            Kevin = Kevin + add
        if player2== "Guo":
            Guo = Guo + add
        if player2== "Pam":
            Pam = Pam + add
        if player2== "Odi":
            Odi = Odi + add
        if player1 == "Kevin":
            Kevin = Kevin - subtract
        if player1 == "Guo":
            Guo = Guo - subtract
        if player1 == "Pam":
            Pam = Pam - subtract
        if player1 == "Odi":
            Odi = Odi - subtract
            #RentOrBuy = input("Have you landed on someone's property or have you landed on an open property? Buy, Rent   ")

    '''    if RentOrBuy == "Rent" or RentOrBuy == "rent":
        houses = input("How many houses?   ")'''

    input1 = input("Enter the propertly landed on:  ")
    var1 = 0
    if input1 == "Kchange":
        var1 = input("What to change to:")
        Kevin = int(var1)
    if input1 == "Ochange":
        var1 = input("What to change to:")
        Odi = int(var1)
    if input1 == "Pchange":
        var1 = input("What to change to:")
        Pam = int(var1)
    if input1 == "Gchange":
        var1 = input("What to change to:")
        Guo = int(var1)

    funct1()

    if player1 == "Kevin":
        Kevin = Kevin - subtract
    if player1 == "Guo":
        Guo = Guo - subtract
    if player1 == "Pam":
        Pam = Pam - subtract
    if player1 == "Odi":
        Odi = Odi - subtract

    print("kevin=", Kevin)
    print("Guo=", Guo)
    print("pam=", Pam)
    print("odi=", Odi)

