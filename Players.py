import json
import copy
import atexit

class Players:
    '''
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Players.__instance == None:
            Players()
        return Players.__instance
    '''
    def __init__(self):
        '''
        """ Virtually private constructor. """
        if Players.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Players.__instance = self
        '''

        self.players = []
        atexit.register(self.__del__)

    def __del__(self):
    #def saveBeforeClose(self):
        print("del program called")
        with open("./SaveBeforeClose/SaveBeforeClosePlayers.json", 'w') as json_file:
            print(self.players)
            print("KEVIN")
            json.dump(self.players, json_file)
        

    def addPlayer(self, playerName):
        with open("./Default/default_player.json") as f:
            newPlayer = json.load(f)
            newPlayer["Name"] = playerName
            newPlayer["Amount"] = 1500
            self.players.append(newPlayer)

    def loadPreviousSaveData(self):
        with open("./SaveBeforeClose/SaveBeforeClosePlayers.json", 'r') as json_file:
            self.players = json.load(json_file)    

    def listCurentPlayers(self):
        print("this.players = ", self.players)

    def setAmount(self, playerName, newAmount):
        for player in self.players:
            if player["Name"] == playerName:
                var1 = player["Amount"]
                player["Amount"] = newAmount

    def getAmount(self, playerName):
        for player in self.players:
            if player["Name"] == playerName:
                return player["Amount"]


    def getPlayerslist(self):
        return self.players

    def addProperty(self, playerName, property):
        for player in self.players:
            if player["Name"] == playerName:
                player["PropertyOwned"].append(property)

    def updateRollDiceOrder(self, playerName, orderNum):
        for player in self.players:
            if player["Name"] == playerName:
                player["RollDiceOrder"] = orderNum

    '''    def PlayerRolling(self, playerList):
            for i,player in enumerate(self.players):
                if player["RollDiceOrder"] == playerList[i]:

                if player["RollDiceOrder"] == playerList[i]:
                    player["JailStatus"] = JailStatus
    '''
    def updateJailStatus(self, playerName, JailStatus):
        for player in self.players:
            if player["Name"] == playerName:
                player["JailStatus"] = JailStatus

    def updateIcon(self, playerName, icon):
        for player in self.players:
            if player["Name"] == playerName:
                player["Icon"] = icon

    def updatePosition(self, playerName, position):
        for player in self.players:
            if player["Name"] == playerName:
                player["CurrentPosition"] = position

    def getPosition(self, playerName):
        for player in self.players:
            if player["Name"] == playerName:
                return player["CurrentPosition"]



    def getRolls(self, playerName):
        for player in self.players:
            if player["Name"] == playerName:
                return player["Rolls"]
    def addRolls(self, playerName, roll):
        for player in self.players:
            if player["Name"] == playerName:
                player["Rolls"].append(roll)

    def setRolls(self, playerName, Lroll):
        for player in self.players:
            if player["Name"] == playerName:
                player["Rolls"] = Lroll

    def updatePosition(self, playerName, position):
        for player in self.players:
            if player["Name"] == playerName:
                player["CurrentPosition"] = position

    def reorderPlayersAsItWasSet(self):
        tmp = copy.deepcopy(self.players)
        totalPlayerCount = len(self.players)
        self.players.clear() 
        while (totalPlayerCount > 0):
            print("AA totalPlayerCount = ", totalPlayerCount)
            print("tmp = ", tmp)
            for elm in tmp:
                print("elm = ", elm)
                if elm["RollDiceOrder"] == totalPlayerCount:
                    self.players.insert(0, elm)
                    totalPlayerCount -= 1
                    print("self.players = ", self.players)
    

def main():

    #player = Players.getInstance()
    player = Players()
    player.addPlayer("kevin")
    player.setAmount("kevin", 1400)
    player = Players()
    player.addPlayer("guo") 
    player.addPlayer("alan")
    player.addPlayer("kevin")
    player.updateRollDiceOrder("kevin", 1)
    player.updateRollDiceOrder("alan", 2)
    player.updateRollDiceOrder("guo", 3)
    player.reorderPlayersAsItWasSet()

    #player.listCurentPlayers()


if __name__ == "__main__":
    print("To run Players class directly")
    main()
else:
    print("To run Players being imported")