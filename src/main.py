# Project Name: 
#   TBD
#
# Project Description: 
#   Program meant to automate the process of downloading 
#   videos from twitch after a stream has ended and uploading them to youtube.
#
# Project Python Version:
#   3.11.4
# 
# Authors: 
#   Rasmus Tanggaard, Malthe Sørensen, Jonas Søgaard Frederiksen

import random

bread = ["Sandpaper", "Cardboard", "Sponge", "Plywood", "Concrete Slab", "Astroturf"]
spread = ["Glue", "Motor Oil", "Paint", "Shaving Cream", "Lotion", "Cement"]
meat_protein = ["Rubber Bands", "Shoelaces", "Plastic Straws", "Electrical Wires", "Hoses", "Screws"]
cheese = ["Wax", "Soap", "Chalk", "Playdough", "Styrofoam", "Slime"]
vegetables = ["Leaves", "Grass", "Plastic Plants", "Pine Cones", "Feathers", "Aluminum Foil"]
condiments = ["Ink", "Bleach", "Nail Polish", "Antifreeze", "Adhesive", "Coolant"]
extras = ["Batteries", "Thumbtacks", "Paper Clips", "Nails", "Tape", "Washers"]

sandwich_parts = {
    "bread": bread,
    "spread": spread,
    "meat_protein": meat_protein,
    "cheese": cheese,
    "vegetables": vegetables,
    "condiments": condiments,
    "extras": extras
}

def generate_sandwich() -> list:
    sandwich = []
    sandwich.append(bread[random.randint(0, len(bread) - 1)])
    sandwich.append(spread[random.randint(0, len(spread) - 1)])
    sandwich.append(extras[random.randint(0, len(extras) - 1)])
    sandwich.append(vegetables[random.randint(0, len(vegetables) - 1)])
    sandwich.append(cheese[random.randint(0, len(cheese) - 1)])
    sandwich.append(meat_protein[random.randint(0, len(meat_protein) - 1)])
    sandwich.append(condiments[random.randint(0, len(condiments) - 1)])
    sandwich.append(bread[random.randint(0, len(bread) - 1)])
    return sandwich

def main():
    print("Welcome to the Sandwich Generator!")
    print("Here is your sandwich:")
    for part in generate_sandwich():
        print(part)
    
    
        


if __name__ == "__main__":
    main()