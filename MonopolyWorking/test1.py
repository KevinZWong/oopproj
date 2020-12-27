
import json
from random import randint


with open("default_properties.json", "r") as read_file:
    data = json.load(read_file)

LProperty = ["Mediterranean_Avenue","Baltic_Avenue","Reading_Railroad","Oriental_Avenue","Vermont_Avenue",
             "Connecticut_Avenue","St._James_Place","Electric_Company","States_Avenue","Virginia_Avenue",
             "Pennsylvania_Railroad","St._Charles_Place","Tennessee_Avenue","New_York_Avenue","Kentucky_Avenue",
             "Indiana_Avenue","Illinois_Avenue","B._&_O._Railroad","Atlantic_Avenue","Ventnor_Avenue","Water_Works",
             "Marvin_Gardens","Pacific_Avenue","North_Carolina_Avenue","Pennsylvania_Avenue","Pennsylvania_Avenue","Short_Line",
             "Park_Place","Boardwalk",]
for i in LProperty:
    var1 = data[i]["Type"]
    print(var1)
