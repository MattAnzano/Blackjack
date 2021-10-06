from indCard import Card
from DeckofCards import Deck


class Player:
    def __init__(self):
        self.theHand = []
        self.playerName = ' '
    
    def aboutPlayer (self):
        self.playerName = input("player Name:")

    
    def specialPlayer(self):
        self.playerName = "Dealer"

    def enterCard(self, card):
        self.theHand.append(card)

    def checkTotal (self):
        total = 0
        for card in self.theHand:
            total += card.GetValue()
        return total
        

    def showCards (self):
        for card in self.theHand:
            card.showCard()
            



