from card import Card

#
class Hand:

    def __init__(self):
        self.__hand = []

    def add(self, card):
        self.__hand.insert(0, card)

    def suitsRemove(self):
        self.__hand.pop(3)
        self.__hand.pop(0)

    def matchRemove(self):
        del self.__hand[0:5]

    def view(self, index):
        return self.__hand[index]


    def __len__(self):
        return len(self.__hand)
