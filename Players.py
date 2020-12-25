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

    def updateRollDiceOrder(self, playerName, orderNum):
        for player in self.players:
            if player["Name"] == playerName:
                player["RollDiceOrder"] = orderNum


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
    player.addPlayer("guo")
    player.addPlayer("alan")
    player.addPlayer("kevin")

    player.listCurentPlayers()  
    print("\n A")

    player.updateRollDiceOrder("kevin", 1)
    player.updateRollDiceOrder("alan", 2)
    player.updateRollDiceOrder("guo", 3)

    player.listCurentPlayers()
    print("\n B")
    player.reorderPlayersAsItWasSet()
    print("\n C")
    player.listCurentPlayers()


if __name__ == "__main__":
    print("To run Players class directly")
    main()
else:
    print("To run Players being imported")