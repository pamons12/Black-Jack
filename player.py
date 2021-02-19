class player:
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