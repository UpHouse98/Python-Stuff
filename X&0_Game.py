#First player chooses X or 0 to play
def xorzero():
    x = input("Please choose X or O for the first player: ")
    while True:
        if (x == "X") or (x == "O"):
            return x
        else:
           x = input("Please choose X or O: ")


def inNum():
    x = int(input("Give me the position for the first player: "))
    while 1 < x and x > 9:
        print("Please input a number beetween 1 and 9!")
        x = int(input("Give me the position for the first player: "))
    return x

def ShowGame():
    print("\n")
    print(" {0} | {1} | {2} ".format(mydict["1"],mydict["2"],mydict["3"]))
    print("-----------")
    print(" {0} | {1} | {2} ".format(mydict["4"],mydict["5"],mydict["6"]))
    print("-----------")
    print(" {0} | {1} | {2} ".format(mydict["7"],mydict["8"],mydict["9"]))
    print("\n")


mydict = {
  "1": " ",
  "2": " ",
  "3": " ",
  "4": " ",
  "5": " ",
  "6": " ",
  "7": " ",
  "8": " ",
  "9": " "
}

print("=============================================================")
print("Welcome to the X/O game!\nThis is the layout of the game board: ")
print("\n")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")
print("\n")
print("To place an X or O you need too input the position you chose!")
print("=============================================================")
player1 = xorzero()
numberIn = str(inNum())

mydict[numberIn] = player1

ShowGame()