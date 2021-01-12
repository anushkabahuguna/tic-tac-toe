
#A TWO PLAYER GAME
brd = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in brd:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def gameOver(turn):
    print ("\nGame Over\n")
    print(" **** " +turn + " won. ****")
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(brd)
        print("It's your turn, " + turn + ".  Move to which place?")

        move = input()        

        if brd[move] == ' ':
            brd[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
 
        if count >= 5:
            if brd['7'] == brd['8'] == brd['9'] != ' ': # across the top
                printBoard(brd)
                gameOver(turn);                
                break
            elif brd['4'] == brd['5'] == brd['6'] != ' ': # across the middle
                printBoard(brd)
                gameOver(turn);
                break
            elif brd['1'] == brd['2'] == brd['3'] != ' ': # across the bottom
                printBoard(brd)
                gameOver(turn);
                break
            elif brd['1'] == brd['4'] == brd['7'] != ' ': # down the left side
                printBoard(brd)
                gameOver(turn);
                break
            elif brd['2'] == brd['5'] == brd['8'] != ' ': # down the middle
                printBoard(brd)
                gameOver(turn);
                break
            elif brd['3'] == brd['6'] == brd['9'] != ' ': # down the right side
                printBoard(brd)
                gameOver(turn);
                break 
            elif brd['7'] == brd['5'] == brd['3'] != ' ': # diagonal
                printBoard(brd)
                gameOver(turn);
                break
            elif brd['1'] == brd['5'] == brd['9'] != ' ': # diagonal
                printBoard(brd)
                gameOver(turn);
                break 

        
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            brd[key] = " "

        game()

if __name__ == "__main__":
    game()