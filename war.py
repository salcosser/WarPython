# War the card game
# Sam Alcosser
import random
from graphics import *
import time
win = GraphWin("War", 1000, 500)
winnerG = Text(Point(500,300), "")
winnerG.setFace("helvetica")
class Card(object):
    # declaring the variables
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    # turns face cards into a value of 10
    def getVal(self):
        inpVal = self.value
        if inpVal == "ace":
            return 11
        elif inpVal == "jack":
            return 10
        elif inpVal == "queen":
            return 10
        elif inpVal == "king":
            return 10
        else:
            return inpVal


# main part of the whole game
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        self.player1H = []
        self.player2H = []
    # making the deck

    def build(self):
        for s in ["spades", "clubs", "diamonds", "hearts"]:
            for v in ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]:
                self.cards.append(Card(v, s))

    # used for printing
    def show(self):
        for c in self.cards:
            c.show()

    # shuffles the deck how many times the user wants

    def shuffle(self, n):
        print("shuffling {} times".format(n))
        for time in range(0, n):
            random.shuffle(self.cards)
        print("Cards shuffled")

    def split(self):
        for c in range(0, 26):
            self.player1H.append(self.cards.pop(0))
            self.player2H.append(self.cards.pop(0))

    # the whole game is contained within this one main function
    def play(self):
        games = 0
        # the game will go for 2500 rounds or whoever runs out of cards first, whoever has the most at the end wins
        while games <= 100 and len(self.player1H) > 0 and len(self.player2H) > 0:
            winnerG.undraw()
            print("\n")
            print("game: ", games)
            p1card = self.player1H.pop(0)
            p2card = self.player2H.pop(0)
            print("")
            print("player 1 card:")
            p1card.show()
            print("player 2 card:")
            p2card.show()
            # this section checks who has the higher card or if there is a draw
            # if one person wins both cards get added to the winners stack of cards on the bottom
            if p1card.getVal() > p2card.getVal():
                print("player 1 wins")
                time.sleep(.1)
                self.player1H.append(p1card)
                self.player1H.append(p2card)
                print("player 1 has ", len(self.player1H), "cards")
                print("player 2 has ", len(self.player2H), "cards")
                if len(self.player1H) < 1:
                    print("game over, player 2 wins")
                    time.sleep(.1)
                    break
                elif len(self.player2H) < 1:
                    print("game over, player 1 wins")
                    time.sleep(.1)
                    break
                games = games + 1
            elif p1card.getVal() < p2card.getVal():
                print("player 2 wins")
                time.sleep(.1)
                self.player2H.append(p1card)
                self.player2H.append(p2card)
                print("player 1 has ", len(self.player1H), "cards")
                print("player 2 has ", len(self.player2H), "cards")
                if len(self.player1H) < 1:
                    print("game over, player 2 wins")
                    time.sleep(.1)
                    break
                elif len(self.player2H) < 1:
                    print("game over, player 1 wins")
                    time.sleep(.1)
                    break
                games = games + 1

            # what happens if there is a tie?
            else:
                # tie
                print("THIS MEANS WAR!!!")

                # tempstack is the name of a list which contains all cards on the table including both of the tied cards
                # and the other four which are dealt out between the two players
                # check that both players have enough cards to continue
                tempstack = [p1card, p2card]
                if len(self.player2H) < 3:
                    print("player 1 wins as player 2 is out of cards")
                    games = 2501
                elif len(self.player1H) < 3:
                    print("player 2 wins as player 1 is out of cards")
                    games = 2501
                else:
                    # represents both players placing two cards face down
                    tempstack.append(self.player1H.pop(0))
                    tempstack.append(self.player1H.pop(0))
                    tempstack.append(self.player2H.pop(0))
                    tempstack.append(self.player2H.pop(0))
                    # the commented line below is used for debugging purposes
                    # print("tempstack length", len(tempstack))
                    p1card = self.player1H.pop(0)
                    p2card = self.player2H.pop(0)
                    tempstack.append(p1card)
                    tempstack.append(p2card)
                    print("WAR")
                    print("player 1 card:")
                    p1card.show()
                    print("player 2 card:")
                    p2card.show()
                    # checking yet again for a winner or a tie, if there is a winner, empty all of the tempstack
                    # into that players deck
                    if p1card.getVal() > p2card.getVal():
                        print("player 1 wins")
                        time.sleep(.1)
                        for card in tempstack:
                            self.player1H.append(card)
                        tempstack = []
                        print(len(self.player1H))
                        print(len(self.player2H))
                        games = games + 1
                    elif p1card.getVal() < p2card.getVal():
                        print("player 2 wins")
                        time.sleep(.1)
                        for card in tempstack:
                            self.player2H.append(card)
                        tempstack = []
                        print(len(self.player1H))
                        print(len(self.player2H))
                        games = games + 1
                    # in the event of a double war, check again that both players have enough cards to go again

                    else:
                        print("THIS MEANS DOUBLE WAR!!!")
                        # check that both players have enough cards to continue
                        if len(self.player2H) < 3:
                            print("player 1 wins as player 2 is out of cards")
                            games = 2501
                        elif len(self.player1H) < 3:
                            print("player 2 wins as player 1 is out of cards")
                            games = 2501
                        else:
                            # represents both players putting two cards down and one face up
                            tempstack.append(self.player1H.pop(0))
                            tempstack.append(self.player1H.pop(0))
                            tempstack.append(self.player2H.pop(0))
                            tempstack.append(self.player2H.pop(0))
                            # the commented line below is used for debugging purposes
                            # print("tempstack length", len(tempstack))
                            p1card = self.player1H.pop(0)
                            p2card = self.player2H.pop(0)
                            tempstack.append(p1card)
                            tempstack.append(p2card)
                            print("WAR")
                            print("player 1 card:")
                            p1card.show()
                            print("player 2 card:")
                            p2card.show()
                            # checks for winner or a tie
                            # if there is a winner, dump all of the tempstack into the winners stack
                            if p1card.getVal() > p2card.getVal():
                                print("player 1 wins")
                                time.sleep(.1)
                                for card in tempstack:
                                    self.player1H.append(card)
                                tempstack = []
                                print(len(self.player1H))
                                print(len(self.player2H))
                                games = games + 1
                            elif p2card.getVal() > p1card.getVal():
                                print("player 2 wins")
                                time.sleep(.1)
                                for card in tempstack:
                                    self.player2H.append(card)
                                tempstack = []
                                print(len(self.player1H))
                                print(len(self.player2H))
                                games = games + 1
                            # in the event of a draw on double war, just split the tempstack and continue playing
                            else:
                                print("it's a draw")
                                while (len(tempstack) >= 2):
                                    self.player1H.append(tempstack.pop(0))
                                    self.player2H.append(tempstack.pop(0))
                                tempstack = []
                                print(len(self.player1H))
                                print(len(self.player2H))
                                games = games + 1
        # checking the result of the set of games, who has more cards
        if len(self.player2H) > len(self.player1H):
            print("player 2 wins the game")
            
            winnerG.setText( "Player 2 Wins with " + str(len(self.player2H)) + " cards.")
            winnerG.draw(win)
        elif len(self.player1H) > len(self.player2H):
            winnerG.setText( "Player 1 Wins with " + str(len(self.player1H)) + " cards.")
            winnerG.draw(win)
        elif len(self.player2H) == len(self.player1H):
            
            print("the game is a draw")
            winnerG.setText("the game is a draw")
            winnerG.draw(win)

def main():
#making the UI
    win.setBackground("green")
    winnerG = Text(Point(500,300), "")
    titleText = Text(Point(500, 50), "WAR").draw(win)
    titleText.setFace("helvetica")
    playBox = Rectangle(Point(545, 30), Point(600,70)).draw(win)
    playBox.setFill("lightgray")
    playText = Text(Point(572, 50), "PLAY").draw(win)
    playText.setFace("helvetica")
    p1tag = Text(Point(250, 85), "Player 1").draw(win)
    p2tag = Text(Point(750, 85), "Player 2").draw(win)
    shuffT = Entry(Point(625,50), 3).draw(win)
    shuffLab = Text(Point(625, 25), "shuffle #").draw(win)
    crossLine = Line(Point(0,100), Point(1000,100)).draw(win)
    rectClose = Rectangle(Point(150, 30), Point(200, 60)).draw(win)
    rectClose.setFill("lightgray")
    rtxtClose = Text(Point(175, 45), "Close").draw(win)
    rtxtClose.setFace("helvetica")
    clickT = True
    while clickT:
        click = win.getMouse() # pause for click in window
        x = click.getX()
        y = click.getY()
        if ((545 <= x <= 600) & (30 <= y <= 70)) & (shuffT.getText() != ""):
##---
            deck = Deck()
            winnerG.setText("")
    # showing the cards
            deck.show()
    # checking to make sure that when someone tries to give an amount of times to shuffle that its a number
    # shuffling the deck
            isnum = False
            while isnum == False:
                shuffle = shuffT.getText()
                if (shuffle.isalpha()  == False) & (shuffle != ""):
                    deck.shuffle(int(shuffle))
                    isnum = True
                else:
                   print("please input a number.")
                   break

    # splitting the deck and showing the two players starting stacks
            deck.split()
            print("\nplayer 1 stack\n")
            print(len(deck.player1H))
            for c in deck.player1H:
                c.show()
            print("\nplayer 2 stack\n")
            print(len(deck.player2H))
            for c in deck.player2H:
                c.show()
            deck.play()
    ##--
        elif (150 <= x < 200) & (30 <= y <= 60):
            win.close()
            break





main()
