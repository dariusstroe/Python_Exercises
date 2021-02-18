import random

feetInMile=5280
metersInKilometer=1000
beatlesMembers=["Vasile","Ion","Marinela","Horatiu"]

def getFileExtension(filename):
    return filename[filename.index(".")+1]

def rollDice(number):
    return random.randint(1,number)