from random import randint

class player():
    def __init_(self,playerName,playerHand):
        self.playerName=playerName
        self.playerHand=playerHand
    
    def __init__(self,playerName):
        self.playerName=playerName
        self.playerHand=[]

    def __str__(self):
        print("{} has a hand of: ".format(self.playerName))
        for card in self.playerHand:
            print(card+" ")
    
    def getPlayerName(self):
        return self.playerName

class players(player):
    def __init__(self, *param):
        if len(param) == 0:
            self.playerList=[]
        
        if len(param) == 1:
            self.playerList=param[0]

    def __str__(self):
        for player in self.playerList:
            print(player)

    def addtoPlayerList(self,player):
        self.playerList.append(player)
    
    def printPlayerOrder(self):
        for i in range(len(self.playerList)):
            if(i==0):
                print("{} goes {}".format(str(self.playerList[i].playerName),"1st"))
            elif(i==1):
                print("{} goes {}".format(str(self.playerList[i].playerName),"2nd"))
            elif(i==2):
                print("{} goes {}".format(str(self.playerList[i].playerName),"3rd"))
            else:
                print("{} goes {}".format(str(self.playerList[i].playerName),str(i+1)+"th"))
    
    def randomizePlayerOrder(self):
        playerArray=[]
        randomNum=randint(1,100)

        ##Gets players picking random numbers and stores it in dictionary
        for i in range(len(self.playerList)):
            while(True):
                try:
                    num=int(input("{} pick a number between 1 and 100: ".format(self.playerList[i])))
                except ValueError:
                    print("Please enter an integer ex: 1,2,3...")
                else:
                    if num<=0 or num>100:
                        print("Number must be between 1 and 100")
                    else:
                        if (num in playerArray):
                            print("Number already chosen please choose again")
                        else:
                            break
            playerArray[i] = [self.playerList[i].getPlayerName, abs(randomNum-num)]
        
        self.playerList=insertionSort(self.playerList)
        self.printPlayerOrder
        print("The random number was: "+str(randomNum))

def insertionSort(array):
    for i in range(1,len(array)):
        key_item = array[i][1]
        j=i-1
        while j >= 0 and array[j][1] > key_item:
            array[j+1][1] = array[j][1]
            j -= 1
        array[j+1][1] = key_item
    return array