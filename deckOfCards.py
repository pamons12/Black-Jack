# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:41:59 2019

@author: patma
"""
class card:
    def __init__(self,suit,cardNum):
        self.cardNum=cardNum
        self.suit=suit
        
    def __str__(self):
        if(self.cardNum==11):
            return("\nSuit: Jack Card Num: "+ str(self.cardNum))
        elif(self.cardNum==12):
            return("\nSuit: Queen Card Num: "+ str(self.cardNum))
        elif(self.cardNum==13):
            return("\nSuit: King Card Num: "+ str(self.cardNum))
        elif(self.cardNum==1):
            return("\nSuit: Ace Card Num: "+ str(self.cardNum))
        else:
            return("\nSuit: "+str(self.suit)+" Card Num: "+ str(self.cardNum))
       
class deckOfCards(card):
    def __init__(self,numOfDecks):
        self.deck=[]
        suits=["clubs","diamonds","hearts","spades"]
        count=0
        while(count<numOfDecks):
            for i in range(len(suits)):
                for j in range(13):
                    self.deck.append(card(suits[i],j+1))
            count+=1
    def __repr__(self):
        tempStr=""
        for i in range(len(self.deck)):
            tempStr= tempStr+"\nCard: "+str(self.deck[i])
        return tempStr
    
    def __str__(self):
        tempStr=""
        for card in self.deck:
            if(card.cardNum==11):
                tempStr+="\nJack of "+str(card.suit)
            elif(card.cardNum==12):
                tempStr+="\nQueen of "+ str(card.suit)
            elif(card.cardNum==13):
                tempStr+="\nKing of "+ str(card.suit)
            elif(card.cardNum==1):
                tempStr+="\nAce of "+ str(card.suit)
            else:
                tempStr+="\n"+str(card.cardNum)+" of "+str(card.suit)
        return tempStr
    
    def numberOfCards(self):
        numOfCards=0
        for card in self.deck:
            numOfCards+=1
        return numOfCards