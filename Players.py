import json
import copy

START_FUND = 1500

class Players:
    def __init__(self):
        self.players = []

    def __del__(self):
        with open("./SaveBeforeClosePlayers.json", 'w') as json_file:
            json.dump(self.players, json_file)

    def addPlayer(self, playerName):
        with open("./default_player.json") as f:
            newPlayer = json.load(f)
            newPlayer["Name"] = playerName
            newPlayer["Amount"] = START_FUND
            self.players.append(newPlayer)

    def listCurentPlayers(self):
        print("this.players = ", self.players)

    def addProperty(self, playerName, property):
        for player in self.players:
            if player["Name"] == playerName:
                player["PropertyOwned"].append(property)

    def updateRollDiceOrder(self, playerName, orderNum):
        for player in self.players:
            if player["Name"] == playerName:
                player["RollDiceOrder"] = orderNum

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
    player = Players()
    print("\n A")
    player.addPlayer("kevin")
    player.listCurentPlayers()
    player.updateJailStatus("kevin",1)
    player.updateRollDiceOrder("kevin", 2)
    player.addProperty("kevin","Park Place")
    player.addProperty("kevin","Boardwalk")
    player.listCurentPlayers()

    '''
    player = Players()
    player.addPlayer("guo")
    player.listCurentPlayers()  
    print("\n A")
    player.addPlayer("alan")
    player.listCurentPlayers() 

    print("\n A")
    player.addPlayer("kevin")
    player.listCurentPlayers()


    print("\n B")
    player.updateRollDiceOrder("kevin", 1)
    player.listCurentPlayers()
    print("\n B")

    player.updateRollDiceOrder("alan", 2)
    player.listCurentPlayers()
    print("\n B")

    player.updateRollDiceOrder("guo", 3)
    player.listCurentPlayers()
    print("\n B")


    print("\n C")
    player.reorderPlayersAsItWasSet()
    print("\n C")
    player.listCurentPlayers()
    '''

if __name__ == "__main__":
    print("To run Players class directly")
    main()
else:
    print("To run Players being imported")