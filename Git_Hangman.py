class hangman :
    wrong = 0
    picture =["",
              "_______      ",
              "|      |     ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            ",
              ]
    def __init__(self,w) :
        self.w_list = list(w)
        self.w_board = ["_"] * len(w)
        print("Welcome to hangman!")

    def compare(self) :
        while self.wrong < len(self.picture) :
            print("\n")
            c = input("Type one word : ")
            if c in self.w_list :
                index = self.w_list.index(c)
                self.w_list[index] = "$"
                self.w_board[index] = c
                print("Are you genius?")
                print(" ".join(self.w_board))
            else :
                self.wrong += 1
                print("Oh... It\'s a bummer.")
            print("\n".join(self.picture[0:self.wrong+1]))

            if "_" not in self.w_board :
                print("You win!")
                break
        if self.wrong == len(self.picture) :
            print("You lose!")

a = hangman("red")
a.compare()
