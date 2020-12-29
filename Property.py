import json
from Players import Players

class Property:
    def __init__(self, jsonFilePath="./Default/default_properties.json"):
        with open(jsonFilePath) as f:
            self.Properties = json.load(f)

        print(self.Properties)

        self.player = Players()
        self.player.loadPreviousSaveData()

    def __del__(self):
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

    def getHouseCost(self, propertyName):
        return self.Properties[propertyName]["HouseCost"]
    def MortgageValue(self, propertyName):
        return self.Properties[propertyName]["MortgageValue"]
    def UnmortgageValue(self, propertyName):
        return self.Properties[propertyName]["UnmortgageValue"]

    def BuyProperty(self, propertyName, FutureOwner):
        propertyPrice = self.player.getAmount(propertyName)
        print("guo")
        print(propertyPrice)
        print("wong")

        


def main():
    property = Property() 
    
    print(property.MortgageValue("Boardwalk"))
    property.BuyProperty("Boardwalk","kevin")

if __name__ == "__main__":
    print("To run Property class directly")
    main()
else:
    print("To run Property being imported")