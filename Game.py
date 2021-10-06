from indCard import Card
from DeckofCards import Deck
from theplayers import Player




class Game:
    def __init__(self):
        self.theDeck = Deck()
        self.Dealer = Player()
        self.player = Player()

    def hitOrStay (self, player):
        self.choice = ' '
        self.stay = False
        while self.stay == False:
            self.choice = input("Hit (h) or Stay(s): ")
            if self.choice == 'h':
                aCard = self.theDeck.pullCard()
                player.enterCard(aCard)
            if player.checkTotal() > 21:
                print("Bust! You lose!")
                break
            else:
                self.stay = True
        print("Players Card:")
        print("--------------")
        player.showCards()
        print("--------------")



    def dealerHitOrStay(self):
        self.stay = False
        if self.player.checkTotal() > 21:
            print("Dealer Wins")
            return
        while self.stay == False:
            if self.Dealer.checkTotal() < 17:
               aCard = self.theDeck.pullCard() 
               self.Dealer.enterCard(aCard)
            elif self.Dealer.checkTotal() > 21:
                print("Dealer Busts!")
                break
            else:
                self.stay = True
        print("Dealers Card:")
        print("--------------")
        self.Dealer.showCards()
        print("--------------")



    def gameProcedure(self):
        self.theDeck.createDeck()
       
        aCard = self.theDeck.pullCard()
        self.Dealer.enterCard(aCard)
        aCard = self.theDeck.pullCard()
        self.Dealer.enterCard(aCard)

        aCard = self.theDeck.pullCard()
        self.player.enterCard(aCard)
        aCard = self.theDeck.pullCard()
        self.player.enterCard(aCard)
        print("Dealers Cards:")
        print("--------------")
        self.Dealer.showCards()
        print("--------------")
        print()
        print()
        print("players Cards:")
        print("---------------")
        self.player.showCards()
        print("---------------")
        self.hitOrStay(self.player)
        print ("Players Total: ", self.player.checkTotal())
        print()
        print()
        self.dealerHitOrStay()
        print("Dealers Score: ", self.Dealer.checkTotal())



      
            







game = Game()
game.gameProcedure()





