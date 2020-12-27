import json
from Property import Property as Props
# from Players import Players


#=================================

props = Props()
print(props.getPrice("Park_Place"))

props.setOwner("Park_Place", "Alan")
print(props.curOwner("Park_Place"))



print(props.getRent("Park_Place"))
# props.saveCurStateInJson("./guo.json")


#=================================
'''
player = Players()
player.addPlayer("guo")
player.addPlayer("alan")
player.addPlayer("kevin")

player.listCurentPlayers()

player.updateRollDiceOrder("kevin", 1)
player.updateRollDiceOrder("alan", 2)
player.updateRollDiceOrder("guo", 3)

player.listCurentPlayers()

player.reorderPlayersAsItWasSet()

player.listCurentPlayers()

'''