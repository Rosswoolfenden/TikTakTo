

board = [[1,2,3],[4,5,6],[7,8,9]]  # the board

#Imports-
import random
from tkinter import *
from tkinter import messagebox

###TKINTER

tk=Tk()# creates new window
tk.title("TIK TAC FUCKING TOE") #Tittles the window

#Creates the buttons.
b1 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b1,1))
b1.grid(row = 0, column = 0) #creates a grid- to sort the buttons into tik tak toe grid order.

b2 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b2,2))
b2.grid(row = 0, column = 1)
b3 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b3,3))
b3.grid(row = 0, column = 2)

b4 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b4,4))
b4.grid(row = 1, column = 0)

b5 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b5,5))
b5.grid(row = 1, column = 1)

b6 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b6,6))
b6.grid(row = 1, column = 2)

b7 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b7,7))
b7.grid(row = 2, column = 0)

b8 = Button(tk, text=" ", height=10, width=20,bg="White", command=lambda:pressedB(b8,8))
b8.grid(row = 2, column = 1)

b9 = Button(tk, text=" " , height=10, width=20,bg="White", command=lambda:pressedB(b9,9))
b9.grid(row = 2, column = 2)
first=0

lab= Label(tk, text=board)  #tester
lab.grid(row=3, column=0)
labW= Label(tk, text=" TTESTING WIN ")
labW.grid(row=3, column=1)


p1=True  #whose turn is it.
def pressedB(b, n):  #function what is called when a button has been pressed
        global p1  #imports p1 variable to see who's turn it is.
        global board   #imports the board 
        if b["text"]== " " and p1==True:   #if button not been pressed AND its player 1's turn
                b["text"]= "X"  #Change button to X
                b["bg"]="Red"    #Changes button colour 
                p1= False       #Changes turn to player 2
                setElem("X", n, board, 3)  #call setelm funtiion to add there go
                lab["text"]=board    #prints board at bottem, for testing porpose
                win = checkWin(board)  #Checks if player 1 has won/
                #labW["text"]=win     
                if win==1:  #if player 1 has won
                        labW["text"]=("PLAYER X WINSSS2")  #adds message at bottem
                        b1["bg"]="Red"
                        b2["bg"]="Red"   #changes whole grid to red
                        b3["bg"]="Red"
                        b4["bg"]="Red"
                        b5["bg"]="Red"
                        b6["bg"]="Red"
                        b7["bg"]="Red"
                        b8["bg"]="Red"
                        b9["bg"]="Red"
                        messagebox.showinfo("PLAYER X", "PLAYER X WINSSSSS") #
                
        elif b["text"]== " " and p1==False:
                b["text"]= "O"
                b["bg"]="Yellow"
                p1= True
                setElem("O", n, board, 3)
                lab["text"]=board
                win = checkWin(board)
                if win==1:  #if player 2 has won
                        labW["text"]=("PLAYER X WINSSS2")  #adds message at bottem
                        b1["bg"]="Yellow"
                        b2["bg"]="Yellow"   #changes whole grid to red
                        b3["bg"]="Yellow"
                        b4["bg"]="Yellow"
                        b5["bg"]="Yellow"
                        b6["bg"]="Yellow"
                        b7["bg"]="Yellow"
                        b8["bg"]="Yellow"
                        b9["bg"]="Yellow"
                        messagebox.showinfo("PLAYER 0", "PLAYER O WINSSSSS") 
                



#Check winning conditons.
def diag(board,direction):   
	won = True    # sets win to true.
	j = 2;          
	for i in range(2):     #loops through the board
		if (direction == 'fd'):      #Check if searching for a forward diagonal
			if (board[i][i] != board[i+1][i+1]):    #Checks if the first iteration is not the same as the previous
				won = False
		elif (direction == 'bd'):
			if (board[i][j] != board[i+1][j-1]):    #Checks if the first iteration is not the same as the previous
				won = False
		j = j -1;
	return (won)
def line(i,board,direction):
	won = True
	j=0
	for j in range(2):  
		if (direction == ("hoz")):   #checks hoz win check
			if (board[i][j] != board[i][j+1]):
				 won = False
			 	
		elif (direction == ("vert")):  # checks vertical win possibilities 
			if (board[j][i] != board[j+1][i]):
				won = False
	return (won)   #Return won boolean
def checkWin(board):  
	win = False
	i=0
	for i in range (2):
		hoz_win = line(i, board, "hoz")   #calls check lines, and checks hoz
		if (hoz_win == True):   #if reutrns true player has won
			win = True	
	# check the verticals 
	for i in range(2):
		vert_win= line (i, board, "vert")  #calls check lines, and checks vertically
		if(vert_win == True):
			win = True	
# check the diagonals
	diag_winf= diag(board, "fd")
	if (diag_winf== True):
		win = True
	diag_winb= diag(board, "bd")
	if(diag_winb==True):
		win = True
	return (win)				
def defineBoard(boardsize):
	board = [[""] * boardsize for i in range(boardsize)]		#make the basic (non-drawable) version of theboard
	return board
def inputBoardSize():			#futer improvements might allow user to chose differnt boardsize
	boardsize = 3			
	return boardsize
def player1Move(board):
	nextMove= int(input("Player 1, Where will your next move be?  "))
	while any(nextMove in sublist for sublist in board)==False: 
		nextMove = int(input("Player 1, enter a a square thats not been taken you stupid person... "))

	return(nextMove)
def player2Move(board):
	nextMove= int(input("Player 2, Where will your next move be?  "))
	while any(nextMove in sublist for sublist in board)==False: 
		nextMove = int(input("Player 2, enter a a square thats not been taken you stupid person... "))
		
	return(nextMove)

#Draws the board.
def createBoardLabels(board, boardsize):						
	counter = 0
	for i in range(boardsize):
		for j in range(boardsize):
			counter +=1
			board[i][j] = counter
	return (board)
def print_divider (boardsize):								  
	print ('|'.join(['____' for x in range(boardsize)])) 

def print_blank (boardsize):
	print ('|'.join(['    ' for x in range(boardsize)]))		

def print_labels(counter, board, boardsize):					
	row = ' | '.join(['%2s' % board[counter][x] for x in range(boardsize)])
	row = ' ' + row
	print(row)
def drawBoard(board, boardsize):							
	for i in range(boardsize):
		print_blank(boardsize)
		print_labels(i,board, boardsize)
		if (i == boardsize-1):
			print_blank(boardsize)
		else:
			print_divider(boardsize)

		
def setElem(elem, position, board, boardsize):  #Function to change list values with new value
	if position==1:
		board[0][0]=(elem)   #if user choses square 1, change the number 1 is the list ... and so on..
	elif position==2:
		board[0][1]=(elem)
	elif position==3:
		board[0][2]=(elem)
	elif position==4:
		board[1][0]=(elem)
	elif position==5:
		board[1][1]=(elem)
	elif position==6:
		board[1][2]=(elem)
	elif position==7:
		board[2][0]=(elem)
	elif position==8:
		board[2][1]=(elem)	
	elif position==9:
		board[2][2]=(elem)
	return (board)			
#MAIN FUNCTION
def main():
	win = 0 
	#tk.tk.mainloop()
	boardsize = inputBoardSize()  #gets board size.
	board = defineBoard(boardsize)  #creates board
	howManyPlayer=int(input("How many players are there, 1, or 2?  "))  #how many players?
	createBoardLabels(board, boardsize)  #Draws board
	drawBoard(board, boardsize)   #Draws board
	Player_1(board, boardsize, howManyPlayer)  #Calls player 1 function

def guilaunch():
        gui=input("Do yo want a GUI (AI DONT WORK WITH GUI) Y or N? ")   #if the user wants to use the GUI
        if gui==("N"):
                main()   #if they dont, call the main funtion
        else:
                tk.tk.mainloop()  #if they do, calls tk window to open 
def Player_1 (board,boardsize, howManyPlayer):
	elem = 'X'    #players 1 gets X
	position = player1Move(board)    #allows the use to choose wheere they go
	board = setElem(elem, position, board, boardsize)  #sets there mpove to the list
	drawBoard(board,boardsize)    #Re-draws board after players move
	win = checkWin(board)  #checks if the player has won
	if (win==False):
		if howManyPlayer==1:  #Checks if the use is playing on is own or with someone.
			ai (board,boardsize, howManyPlayer)   # if there is only one player, calls ai funtion
		else:
			Player_2(board, boardsize, howManyPlayer)  # if 2 players calls teh player 2 funtion 
	else:
		print('Congratulations Player 1! You win!')  # if the player wins, prinnt it
def Player_2(board, boardsize, howManyPlayer):   ##player 2 function
	elem = "O"
	position = player2Move(board)
	board = setElem(elem, position, board, boardsize)
	drawBoard(board,boardsize)
	win = checkWin(board)
	if (win==False):
		Player_1 (board,boardsize, howManyPlayer)
	else:
		print('Congratulations Player 2! You win!')
		
def ai(board, boardsize, howManyPlayer):   #AI Function
	elem = "O"
	AIpos=random.randint(1,9)     #generates a random number, between 1 and 9 (the board.)
	while any(AIpos in sublist for sublist in board)==False:   #to check if that number is in the board list, it wont be if that square has already been taken
		AIpos=random.randint(1,9)  #if it has already been taken, choose a new number.
	position=AIpos    
	board = setElem(elem, position, board, boardsize)  #sets there move to the list
	drawBoard(board,boardsize)	
	win = checkWin(board)
	if (win==False):
		Player_1 (board,boardsize, howManyPlayer) 
	else:
		print('unlucky you lost to the bot... HAHAHA ')
		
	
		

	                                                                              
guilaunch()	#launches gui launch to see if they want to gui or not.
#main()
