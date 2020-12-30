import json
import atexit

# See:  https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class SingletonPlayers:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if SingletonPlayers.__instance == None:
            SingletonPlayers()
        return SingletonPlayers.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SingletonPlayers.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SingletonPlayers.__instance = self
        self.players = []
        self.START_FUND = 1500
        atexit.register(self.saveBeforeClose)

    def saveBeforeClose(self):
        with open("./SaveBeforeClose/SaveBeforeClosePlayers.json", 'w') as json_file:
            json.dump(self.players, json_file)

    def addPlayer(self, playerName):
        with open("./Default/default_player.json") as f:
            newPlayer = json.load(f)
            newPlayer["Name"] = playerName
            newPlayer["Amount"] = self.START_FUND
            self.players.append(newPlayer)

    def listCurentPlayers(self):
        print("this.players = ", self.players)


def main():
    playerObj1 = SingletonPlayers.getInstance()
    playerObj1.addPlayer("guo")
    playerObj1.addPlayer("kevin")
    playerObj1.addPlayer("alan")
    playerObj1.listCurentPlayers()

    playerObj2 = SingletonPlayers.getInstance()
    print("\n\nFollowing is playerObj2 print Out:")
    playerObj2.listCurentPlayers()
    playerObj2.addPlayer("odi")

    print("\n\nFollowing is playerObj2 print Out:")
    playerObj2.listCurentPlayers()

    print("\n\nFollowing is playerObj1 print Out:")
    playerObj1.listCurentPlayers()


if __name__ == "__main__":
    print("To run Players class directly")
    main()
else:
    print("To run Players being imported")