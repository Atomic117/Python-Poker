# Thomas Tran 300290320

import random


class PokerGame:
    def __init__(self, n = 2):
        self.deck = []
        for i in ("D", "C", "S", "H"):
            for j in range(1, 14):
                if j == 1:
                    z = "A"
                elif j == 10:
                    z = "T"
                elif j == 11:
                    z = "J"
                elif j == 12:
                    z = "Q"
                elif j == 13:
                    z = "K"
                else:
                    z = str(j)
                z += i
                self.deck.append(z)
        self.hand = []
        self.table = []
        for i in range(n):
            self.hand.append([])

    def add_card(self, x, y):
        self.hand[x].append(y)

    def add_to_table(self, x):
        self.table.append(x)

    def get_card(self):
        while True:
            x = random.randint(1, 13)
            y = random.randint(0, 4)
            if x == 1:
                z = "A"
            elif x == 10:
                z = "T"
            elif x == 11:
                z = "J"
            elif x == 12:
                z = "Q"
            elif x == 13:
                z = "K"
            else:
                z = str(x)
            if y == 0:
                z += "D"
            elif y == 1:
                z += "C"
            elif y == 2:
                z += "S"
            else:
                z += "H"
            if z in self.deck:
                v = self.deck.index(z)
                self.deck[v] = "##"
                break

        return z

    def is_straight_flush(self, x):
        y = []
        b = []
        for i in x:
            b.append(i[1])
        for i in x:
            y.append(i[0])
        for i in b:
            if b.count(i) >= 5:
                break
        else:
            return False

        for i in range(len(y)):
            if y[i] == "A":
                y[i] = 1
                y.append(14)
            elif y[i] == "T":
                y[i] = 10
            elif y[i] == "J":
                y[i] = 11
            elif y[i] == "Q":
                y[i] = 12
            elif y[i] == "K":
                y[i] = 13
            else:
                y[i] = int(y[i])
        for i in range(len(y)):
            for j in range(len(y)-i-1):
                if y[j] > y[j+1]:
                    d, e = y[j], b[j]
                    y[j], b[j] = y[j+1], b[j+1]
                    y[j+1], b[j+1] = d, e
        s = len(y) - 4
        for i in range(s):
            for j in range(5):
                if y[i] + j != y[i+j]:
                    break
            else:
                for k in range(5):
                    if b[i] != b[i+k]:
                        return False
                else:
                    return True
        else:
            return False

    def is_four(self, x):
        y = []
        for i in x:
            y.append(i[0])
        for i in y:
            if y.count(i) == 4:
                return True
        else:
            return False

    def is_flush(self, x):
        y = []
        for i in x:
            y.append(i[1])
        for i in y:
            if y.count(i) >= 5:
                return True
        else:
            return False

    def is_full(self, x):
        y = []
        for i in x:
            y.append(i[0])
        for i in y:
            if y.count(i) == 3:
                z = i
                break
        else:
            return False
        for i in range(3):
            y.remove(z)
        for i in y:
            if y.count(i) == 2:
                return True
        else:
            return False


    def is_straight(self, x):
        y = []
        for i in x:
            y.append(i[0])
        for i in range(len(y)):
            if y[i] == "A":
                y[i] = 1
                y.append(14)
            elif y[i] == "T":
                y[i] = 10
            elif y[i] == "J":
                y[i] = 11
            elif y[i] == "Q":
                y[i] = 12
            elif y[i] == "K":
                y[i] = 13
            else:
                y[i] = int(y[i])
        for i in range(len(y)):
            for j in range(len(y)-i-1):
                if y[j] > y[j+1]:
                    d = y[j]
                    y[j] = y[j+1]
                    y[j+1] = d
        s = len(y) - 4
        for i in range(s):
            for j in range(5):
                if y[i] + j != y[i+j]:
                    return False
            else:
                return True

    def is_three(self, x):
        y = []
        for i in x:
            y.append(i[0])
        for i in y:
            if y.count(i) == 3:
                return True
        else:
            return False

    def is_two_pair(self, x):
        y = []
        for i in x:
            y.append(i[0])
        for i in y:
            if y.count(i) == 2:
                z = i
                break
        else:
            return False
        for i in range(2):
            y.remove(z)
        for i in y:
            if y.count(i) == 2:
                return True
        else:
            return False

    def is_pair(self, x):
        y = []
        for i in x:
            y.append(i[0])
        for i in y:
            if y.count(i) == 2:
                return True
        else:
            return False


class TexasHodem(PokerGame):
    def __init__(self, x=2):
        super().__init__(x)

    def deal(self):
        for i in range(len(self.hand)):
            for j in range(2):
                self.add_card(i, self.get_card())
        for i in range(5):
            self.add_to_table(self.get_card())

    def hands(self):
        x = []
        for i in range(len(self.hand)):
            print("Player " + str(i+1) + " hand: " + str(self.hand[i]))
        print("Table: " + str(self.table))

        for i in range(len(self.hand)):
            a = []
            for j in self.hand[i]:
                a.append(j)
            for j in self.table:
                a.append(j)

            if self.is_straight_flush(a):
                x.append("Straight Flush")
            elif self.is_four(a):
                x.append("Four of a kind")
            elif self.is_full(a):
                x.append("Full House")
            elif self.is_flush(a):
                x.append("Flush")
            elif self.is_straight(a):
                x.append("Straight")
            elif self.is_three(a):
                x.append("Three of a kind")
            elif self.is_two_pair(a):
                x.append("Two pair")
            elif self.is_pair(a):
                x.append("Pair")
            else:
                x.append("High card")

        print(x)
        return x

Game = TexasHodem()
Game.deal()
v = Game.hands()