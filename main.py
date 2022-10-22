landScape = [[0,1,2,3,4] , [5,6,7,8,9] , [10,11,12,13,14] , [15,16,17,18,19], [20,21,22,23,24]]
    #initial 5x5 array 

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

while exit == False:
    print("Awaiting Movememnt Command[w,a,s,d]") #asks for direction
    command = input()
    command = (command) #resolve later find how to make a string all lower case
    if command == False:
        exit == True
    else:
        exit == False
        move(command)
        print("Awaiting Research Command") #asks for action

