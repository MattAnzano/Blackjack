from indCard import Card
from random import randint
import random



class Deck:
    #Initilaizes the Deck
    def __init__ (self):
        self.fullDeck = []

    #Creates the Deck 
    def createDeck(self):
        for i in range(1,5):
            if i == 1:
                suit = "Spade" 
            if i == 2:
                suit = "Diamond"
            if i == 3:
                suit = "Clubs"
            if i == 4:
                suit = "Hearts"
            for j in range(1, 14):
                self.fullDeck.append(Card(j,suit))
    
    #Pulls a card out of the full deck 
    def pullCard(self):
        self.x = random.randint(0, len(self.fullDeck))
        card = self.fullDeck[self.x]
        self.fullDeck.pop(self.x)
        return card
    
    #Allows me to look at the entire deck 
    def lookAtDeck (self):
        for card in self.fullDeck:
            card.showCard()
        


