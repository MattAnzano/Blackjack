class Card:

    def __init__(self,val,suit):
        self.suit = suit
        self.value = val
        self.type = 0
        self.face = self.faceCards()


    def faceCards(self):
        if self.value == 11:
            face = 'Jack'
            self.type = 1
            self.value = 10
        elif self.value == 12:
            face = 'Queen'
            self.type = 1
            self.value = 10
        elif self.value == 13:
            face = 'King'
            self.type = 1
            self.value = 10
        elif self.value == 1:
            self.type = 2
            face = 'Ace' 
        
        else:
            face = ' '
        return face
            

    def GetValue(self):
        return self.value
    def GetSuit(self):
        return self.suit
    def GetFace(self):
        return self.face

    def showCard(self):
        if self.type == 0:
            print(self.value, self.suit)
        elif self.type == 1:
            print(self.face, "of",  self.suit)
        else:
            print(self.face, "of", self.suit)
