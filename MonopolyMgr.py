import json
from Property import Property as Props
from Players import Players


player = Players()
print("\n A")
player.addPlayer("alan")
player.setAmount("alan", 1400)
print(player.getPlayerslist())




















'''
class MonopolyMgr:
    def __init__(self):
        self.players = []
        self.properties = []

    def checkIfWeStartANewGameOrResumePrevousGame(self):
        pass

    def preparationEnterPlayerName(self):
        pass

    def preparationEnterPlayerIcon(self):
        pass

    def preparationEnterPlayerRollingOrder(self):
        pass
    
    def startTheGame(self):
        pass
'''