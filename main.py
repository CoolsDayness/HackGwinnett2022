import random

landScape = [[0,1,2,3,4] , [5,6,7,8,9] , [10,11,12,13,14] , [15,16,17,18,19], [20,21,22,23,24]]
    #initial 5x5 array
attributes = ["rocky", "wet", "muddy"]
landScapeAtrributes = [[],[],[],[],[]]
def giveAttributes(map):
    for array in map:
        for i in range(0,5):
            array.insert(i, attributes[random.randint(0,len(attributes) - 1)])

class cord:
    def __init__(self, xVal, yVal):
        self.xVal = xVal
        self.yVal = yVal

roboPosition = cord(2,2)


def move(direction):
    if(direction == "w"):
        print("moved forward")
        roboPosition.yVal += 1
    elif(direction == "a"):
        print("moved west")
        roboPosition.xVal -= 1
    elif(direction == "s"):
        print("moved south")
        roboPosition.yVal -= 1
    elif(direction == "d"):
        print("moved east")
        roboPosition.xVal += 1
    else:
        print("Unknown command try again?")


exit = False

giveAttributes(landScapeAtrributes)
print(landScapeAtrributes)
while exit == False:
    print("Awaiting Movememnt Command[w,a,s,d]") #asks for direction
    command = input()

    if command == "False":
        exit = True
    else:
        move(command)
        print("Awaiting Research Command") #asks for action


