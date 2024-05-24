#Draws a chessboard made of zeros and ones based on user input

def chessboard(length):
    height = 1
    odds = ""
    evens = ""
    while height <= length:
        if height % 2 == 0:
            evens = "01" * length
            print(evens[0:length])
        else:
            odds = "10" * length
            print(odds[0:length])
        height += 1

chessboard(int(input("Please enter the dimension of the chessboard (a single integer above 0):")))