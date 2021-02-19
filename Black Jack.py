from random import randint
from deckOfCards import deckOfCards
from player import player,players

class gameInstance:
    def __init__(self,numOfPlayers,playerList,numOfDecks,deck):
        self.numOfPlayers=numOfPlayers
        self.playerList=playerList
        self.numOfDecks=numOfDecks
        self.deck=deck
        
    def __str__(self):
        print("Number of players: {}\nNumber of decks: {}".format(self.numOfPlayers,self.numOfDecks))
              

def setUpGame():
    
    print("Welcome to Black Jack")
    
    ##Gets number of players 
    while(True):
        try:
            numOfPlayers=int(input("Enter number of players: "))
        except ValueError:
            print("Please enter an integer ex: 1,2,3...")
        else:
            if numOfPlayers<=0:
                print("Number of players must be greater than 0")
            else:
                break
    
    playersObj=players()
    #Gets player names
    for i in range(int(numOfPlayers)):
        playerName=input("Enter player {}'s name: ".format(str(i+1)))
        playersObj.playerList.append(player(playerName))
    
    ##Determins what player will go first, second, etc.
    if(int(numOfPlayers)>1):
        validResponse=False
        response=input("Would you like for the computer who decides first,second,etc? ")
        response=response.upper()
        while(validResponse==False):
            if((response=="YES") | (response=="NO")):
                validResponse=True
            else:
                response=input("Response not valid, answer with yes or no: ")
                response=response.upper()
        if (response=="YES"):
            playersObj.randomizePlayerOrder()

       
    ##Gets number of decks
    while(True):
        try:
            numOfDecks=int(input("Enter the number of decks you would like to use: "))
        except ValueError:
            print("Please enter an integer ex: 1,2,3...")
        else:
            if numOfDecks<=0:
                print("Number of decks must be greater than 0")
            else:
                break
    
    deck = deckOfCards(numOfDecks)
    game = gameInstance(numOfPlayers,playersObj.playerList,numOfDecks,deck)
    return game

def main():
    print("Setting Up Game")
    game=setUpGame()
    print("Game Set Up")
main()        