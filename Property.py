import json
from Players import Players
import atexit
class Property:
    def __init__(self, jsonFilePath="./Default/default_properties.json"):
        with open(jsonFilePath) as f:
            self.Properties = json.load(f)
        self.player = Players()
        self.player.loadPreviousSaveData()
        atexit.register(self.saveBeforeClose)
    def saveBeforeClose(self):
        with open("./SaveBeforeClose/SaveBeforeCloseProperties.json", 'w') as json_file:
            json.dump(self.Properties, json_file)


    def getPrice(self, propertyName):
        return self.Properties[propertyName]["Price"]

    def setOwner(self, propertyName, owner):
        self.Properties[propertyName]["Owner"] = owner

    def getOwner(self, propertyName):
        return self.Properties[propertyName]["Owner"]

    def saveCurStateInJson(self, filePathName):
        with open(filePathName, 'w') as json_file:
            json.dump(self.Properties, json_file)

    def getStatus(self, propertyName):
        return self.Properties[propertyName]["Status"]
    def setStatus(self, propertyName, newStatus):
        self.Properties[propertyName]["Status"] = newStatus
    def setHouses(self, propertyName, newHouses):
        self.Properties[propertyName]["Houses"] = newHouses
    def getHouses(self, propertyName):
        return self.Properties[propertyName]["Houses"]
    def getHouseCost(self, propertyName):
        return self.Properties[propertyName]["HouseCost"]
    def MortgageValue(self, propertyName):
        return self.Properties[propertyName]["MortgageValue"]
    def UnmortgageValue(self, propertyName):
        return self.Properties[propertyName]["UnmortgageValue"]

    def BuyProperty(self, propertyName, FutureOwner):
        FutureOwnerMoney = self.player.getAmount(FutureOwner)
        PropPrice = self.getPrice(propertyName)
        if FutureOwnerMoney >= PropPrice:
            newAmount = FutureOwnerMoney - PropPrice
            self.player.setAmount(FutureOwner,newAmount)
            self.player.addProperty(FutureOwner,propertyName)
        else:
            print("Not enough money, L. git more monay")
            return

    
        


def main():
    property = Property() 

    #print(property.MortgageValue("Boardwalk"))
    property.BuyProperty("Boardwalk","kevin")
    print(property.getPrice("Boardwalk"))
if __name__ == "__main__":
    print("To run Property class directly")
    main()
else:
    print("To run Property being imported")