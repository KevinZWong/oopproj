import threading 

time = int(input("How long do you want to set a timer for? (mins)  "))
time = time  
extend = 3
def Extend(): 
    timer = threading.Timer(1, Done2)
    timer.start() 
    main()
def Done(): 
    global time
    global extend
    print(time ,"min has passed ")
    if extend > 0:
        text = "Would you like to extend the game by 10 minutes, you can only do this " + str(extend) + " more times "
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
    print("10 min has passed ")
    if extend > 0:
        text = "Would you like to extend the game by 10 minutes, you can only do this " + str(extend) + " more times "
        var1 = input(text)
        var1 = var1.upper()
        if var1 == "YES" or var1 == "Y":
            Extend()
            extend -= 1
        if var1 == "NO" or var1 == "N":
            exit()

timer = threading.Timer(time, Done)
timer.start() 
def main(): 
    print("The main code has sucessfully ran \n") 

main()