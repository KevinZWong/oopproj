import json

class Property:
    def __init__(self, jsonFilePath="./default_properties.json"):
        with open(jsonFilePath) as f:
            self.Properties = json.load(f)

        #print(self.Properties)

    def __del__(self):
        with open("./SaveBeforeCloseProperties.json", 'w') as json_file:
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
        return self.Properties[propertyName]["HouseCost"]
    def MortgageValue(self, propertyName):
        return self.Properties[propertyName]["HouseCost"]
        

        


def main():
    property = Property()
    print(property.getPrice("Boardwalk"))

if __name__ == "__main__":
    print("To run Property class directly")
    main()
else:
    print("To run Property being imported")