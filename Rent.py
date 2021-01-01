import json
from Property import Property as Property
from Players import Players 
import atexit
class Rent:
    def __init__(self, jsonFilePath="./Default/default_properties.json"):
        with open(jsonFilePath) as f:
            self.Properties = json.load(f)
        self.player = Players()
        self.player.loadPreviousSaveData()
        atexit.register(self.saveBeforeClose)

    def saveBeforeClose(self):
        with open("./SaveBeforeClose/SaveBeforeCloseRent.json", 'w') as json_file:
            json.dump(self.Properties, json_file)


    def getRent(self, propertyName):
        return self.Properties[propertyName]["Rent"]
    def getRentWithColorSet(self, propertyName):
        return self.Properties[propertyName]["RentWithColorSet"]
    def getRentWith1House(self, propertyName):
        return self.Properties[propertyName]["RentWith1House"]
    def getRentWith2House(self, propertyName):
        return self.Properties[propertyName]["RentWith2House"]
    def getRentWith3House(self, propertyName):
        return self.Properties[propertyName]["RentWith3House"]
    def getRentWith4House(self, propertyName):
        return self.Properties[propertyName]["RentWith4House"]
    def getRentWithHotel(self, propertyName):
        return self.Properties[propertyName]["RentWithHotel"]

    def PayRent(self, Rentor, Rentee, price): # rentor is the person geting the money, rentee is the tenant
        RentorAmount = self.player.getAmount(Rentor) 
        RenteeAmount = self.player.getAmount(Rentee)
        if RenteeAmount >= price:
            RenteeAmount = RenteeAmount - price
            self.player.setAmount(Rentee,RenteeAmount)
            RentorAmount = RentorAmount + price
            self.player.setAmount(Rentor, RentorAmount)
        else:
            print("Rentee Doesn't have enough money.")
            return
        


def main():
    property = Property()
    rent = Rent()
    rent.PayRent("kevin", "guo", 200)

if __name__ == "__main__":
    print("To run Property class directly")
    main()
else:
    print("To run Property being imported")