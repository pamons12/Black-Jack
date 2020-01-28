# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:19:45 2019

@author: patma
"""
from random import randint
from deckOfCards import deckOfCards


class gameInstance:
    def __init__(self,numOfPlayers,playerList,numOfDecks,deck):
        self.numOfPlayers=numOfPlayers
        self.playerList=playerList
        self.numOfDecks=numOfDecks
        self.deck=deck
        
    def __str__(self):
        print("Number of players: {}\nNumber of decks: {}".format(self.numOfPlayers,self.numOfDecks))
        
def whoGoesFirst(playerList):
    playerDict={}
    randomNum=randint(1,100)
    
    for i in range(len(playerList)):
        while(True):
            try:
                num=int(input("{} pick a number between 1 and 100: ".format(str(playerList[i]))))
            except ValueError:
                print("Please enter an integer ex: 1,2,3...")
            else:
                if num<=0 or num>100:
                    print("Number must be between 1 and 100")
                else:
                    break
        playerDict[playerList[i]]= abs(randomNum-num)

        
    orderedPlayers=[]
    while(len(playerList)!=1):
        smallestGuessIndex=0 
        for i in range(len(playerList)-1):
            playerName1=playerList[i]
            playerName2=playerList[i+1]
            if playerDict[playerName1]>playerDict[playerName2]:
                smallestGuessIndex=i+1
            else:
                smallestGuessIndex=i
        orderedPlayers.append(playerList[smallestGuessIndex])
        del playerList[smallestGuessIndex]
    
    orderedPlayers.append(playerList[0])
    del playerList[0]    
    for i in range(len(orderedPlayers)):
        if(i==0):
            print("{} goes {}".format(str(orderedPlayers[i]),"1st"))
        elif(i==1):
            print("{} goes {}".format(str(orderedPlayers[i]),"2nd"))
        elif(i==2):
            print("{} goes {}".format(str(orderedPlayers[i]),"3rd"))
        else:
            print("{} goes {}".format(str(orderedPlayers[i]),str(i+1)+"th"))
        
    print("The random number was: "+str(randomNum))
    return(orderedPlayers)
                

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
            
    playerList=[]
    #Gets player names
    for i in range(int(numOfPlayers)):
        playerName=input("Enter player {}'s name: ".format(str(i+1)))
        playerList.append(playerName)
    
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
            playerList=whoGoesFirst(playerList)
            
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
    game = gameInstance(numOfPlayers,playerList,numOfDecks,deck)
    return game
    
def main():
    game=setUpGame()
    print(game.playerList)
main()        