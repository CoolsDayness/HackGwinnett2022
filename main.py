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
    def moveForward(self):
        if self.yVal <= len(landScape) - 2:
            self.yVal += 1
            print("moved forward")
        else:
            print("edge of bounds!")
    def moveBackward(self):
        if self.yVal >= 1:
            self.yVal -= 1
            print("moved south")
        else:
            print("edge of bounds!")
    def moveLeft(self):
        if self.xVal >= 1:
            self.xVal -= 1
            print("moved forward")
        else:
            print("edge of bounds!")
    def moveRight(self):
        if self.xVal <= len(landScape[0]) - 2:
            self.xVal += 1
            print("moved east")
        else:
            print("edge of bounds!")
    def printPos(self):
        print(self.xVal)
        print(self.yVal)

roboPosition = cord(2,2)


def move(direction):
    if(direction == "w"):
        roboPosition.moveForward()
    elif(direction == "a"):
        roboPosition.moveLeft()
    elif(direction == "s"):
        roboPosition.moveBackward()
    elif(direction == "d"):
        roboPosition.moveRight()
    else:
        print("Unknown command try again?")


exit = False

giveAttributes(landScapeAtrributes)

while exit == False:
    print("Awaiting Movememnt Command[w,a,s,d]") #asks for direction
    command = input()

    if command == "False":
        exit = True
    else:
        move(command)
        roboPosition.printPos()
        mine = ["fossil", "soil", "rock", "river"]
        rand = random.choice(mine)
        observe = ["metal", "water", "sand storm", "volcano", "canyons", "hills", "river"]
        rand_ob = random.choice(observe)
        question = input("Do you want to Mine/observe: ")
        print(question)
        if question.casefold() == "mine".casefold():
            print("you encountered a " + rand)
        elif question == "observe":
            print("you saw a " + rand_ob)
        print("Awaiting Research Command") #asks for action


