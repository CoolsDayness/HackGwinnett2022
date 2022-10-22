import json
from pickle import FALSE, TRUE

import requests

r = requests.get("https://cataas.com/cat?json=true")
data = json.loads(r.text)

print(data["url"])

landScape = [[0,1,2,3,4] , [5,6,7,8,9] , [10,11,12,13,14] , [15,16,17,18,19], [20,21,22,23,24]]
    #initial 5x5 array 

x = 2   # 2,2 is the center of the 5 x 5 array
y = 2

position = [x,y] #Set default posistion to the middle of the array

def move(direction):
    if(direction == "w"):
        print("moved forward")
        y += 1
    if(direction == "a"):
        print("moved west")
        x -= 1
    if(direction == "s"):
        print("moved south")
        y -= 1
    if(direction == "d"):
        print("moved east")
        x += 1
    else:
        print("Unknown command try again?")

exit = FALSE

while exit == FALSE:
    print("Awaiting Command")
    command = input()
    if command == FALSE:
        exit == TRUE
    else:
        exit == FALSE
        move(command)

