counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

    if "Arapahoe" in counties and "El Paso" not in counties:
        print("Only Arapahoe is in the list of counties.")
    else:
        print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {}  
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)   

for county, voters in counties_dict.items():
    print(county, voters)

