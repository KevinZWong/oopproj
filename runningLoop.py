import time

class runningLoop:
    def __init__(self):
        self.count = 0

    def startLooping(self, loopingList):
        
        testCount = 0
        while (self.count < len(loopingList)):
            time.sleep(1) 
            print("self.count =", self.count)

            print("Now, start roll the dice ", loopingList[self.count])
            '''
            if testCount == 3: 
                self.goBackCount(2)


            if testCount == 9:
                self.goForwardCount(1)
            '''

            if testCount == 12:
                self.exitRunningLoop()
            else:
                testCount += 1            
            
            if self.count == len(loopingList) - 1:
                self.count = 0
            else:
                self.count += 1
            
    def exitRunningLoop(self):
        self.count = 999

    def goBackCount(self, backCount):
        self.count = self.count - backCount

    def goForwardCount(self, forwardCount):
        self.count = self.count + forwardCount


def main():
    list1 = ["Kevin", "Alan", "Guo"]
    obj = runningLoop()
    obj.startLooping(list1)






if __name__ == "__main__":
    print("To run Players class directly")
    main()
else:
    print("To run Players being imported")