import random

# Function to display a welcome message
def welcome():
    wel = '''
    +--------------------------------------+
    |      WELCOME TO TIC-TAC-TOE GAME     |
    +--------------------------------------+
'''
    print(wel)


# Function to display the option to play single or multiplayer
def s_or_m():
    p = """
+-----------------+           +-----------------+
|  SINGLE PLAYER  |           |  MULTI PLAYER   |
+-----------------+    OR     +-----------------+
|    ENTER S      |           |     ENTER M     |
+-----------------+           +-----------------+
"""
    print(p)


# Initialize an empty list to represent the game board
sign_dictionary = []
for i in range(9):
    sign_dictionary.append(' ')


# Function to display the current state of the game board
def print_board():
    board = f"""
+-----------------------------+
|    CURRENT BOARD STATUS     |
|                             |
|          {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}          |
|         ---|---|---         |
|          {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}          |
|         ---|---|---         |
|          {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]}          |
|                             |
+-----------------------------+
"""
    print(board)


# Function to take input from the player and update the game board
index_list = []
def take_input(player_name):
    while True:
        x = int(input(f"{player_name}'s Turn: "))
        x -= 1
        if 0<= x < 9:
            if x in index_list:
                print("This spot is blocked.\n")
                continue
            index_list.append(x)
            return x
        print("Please enter number between 1-9")


# Function to take input from the computer and update the game board
def take_input_COM():
    while True:
        x = random.randint(1,9)
        print(f"COMPUTER Choosen: {x} ")
        x -= 1
        if 0<= x < 9:
            if x in index_list:
                print("This spot is blocked.\n")
                continue
            index_list.append(x)
            return x
        print("Please enter number between 1-9")

#Function to display user won in fancy text
def winner_img_user(name):
    u = f'''
╔═.✵.═════JUDGEMENT═══TIME════╗
             ____
           _(____)_
_______ooO_(_o__o_)_Ooo________
           
           {name} WON!!

╚══OF══THE══GAME═══.✵.════════╝
'''
    print(u)

#Function to display computer won in fancy text
def winner_img_com(name):
    c = f'''
╔═.✵.═════JUDGEMENT═══TIME════╗
            ____
           ||""||
           ||__||
___________[ -=.]`0____________
          
          {name} WON!!

╚══OF══THE══GAME═══.✵.════════╝
'''
    print(c)

#Function to display the match is tie
def tie_img():
    tie ='''
╔═.✵.═════JUDGEMENT═══TIME════╗
            _     _
           ( \---/ )
            ) . . (
______,--._(___-___)_,--.______
      `--'           `--'    
           MATCH DRAW

╚══OF══THE══GAME═══.✵.════════╝
'''
    print(tie)

#Function to display user input is invalid
def invalid_img():
    invalid ='''
+-----------------------------+
|    ___   ! INVALID INPUT !  |
|   (._.)         ✘ ⤵         |
|    <|>     PLEASE ENTER     |
|   _/\_      CORRECTLY !     |
+-----------------------------+
'''
    print(invalid)


# Function to calculate the result of the game for single player mode      
def calculate_result_s(player_one,player_two):
    thank = """
+--------------------------------+
|   THANK YOU BOTH FOR JOINING   |
+--------------------------------+
"""

    if (sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or
    sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X'  or
    sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X'  or
    sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X'  or
    sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X'  or
    sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X'  or
    sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X'  or
    sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X') :
        winner_img_user(player_one)
        quit(thank)
    elif (sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or
    sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O'  or
    sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O'  or
    sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O'  or
    sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O'  or
    sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O'  or
    sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O'  or
    sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O') :
        winner_img_com(player_two)
        quit(thank)

# Function to calculate the result of the game for multi player mode 
def calculate_result_m(player_one,player_two):
     thank = """
+--------------------------------+
|   THANK YOU BOTH FOR JOINING   |
+--------------------------------+
"""
     if (sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or
    sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X'  or
    sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X'  or
    sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X'  or
    sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X'  or
    sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X'  or
    sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X'  or
    sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X') :
           winner_img_user(player_one)
           quit(thank)
     elif (sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or
    sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O'  or
    sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O'  or
    sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O'  or
    sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O'  or
    sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O'  or
    sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O'  or
    sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O') :
        winner_img_user(player_two)
        quit(thank)

# Main function for Single Player Mode
def Single_main():
    instructions = """
+------------------------------------------------------------------------+
|                   THIS WILL BE OUR TIC TAC TOE GAME                    |
|                                                                        |
|                            1 | 2 | 3                                   |
|                           ---|---|---                                  |
|                            4 | 5 | 6                                   |
|                           ---|---|---                                  |
|                            7 | 8 | 9                                   |
|------------------------------------------------------------------------|
|                                                                        |
|   -*INSTRUCTIONS OF THE GAME ARE AS FOLLOWS*-                          |
|                                                                        |
|     1.Insert the spot number (1-9) to put your sign                    |
|     2.You must first all 9 spots to get the result                     |
|     3.Player will go first                                             |
|                                                                        |
+------------------------------------------------------------------------+"""
        
    player = input("Enter Your Username: ")
    player_one = player.upper()
    player_two = "COMPUTER"
    print(f"\n✧ Thank you for joining {player_one} and {player_two} ✧")

    print(instructions)
    print((f"\t\t\t {player_one.upper()}'s Sign is - X").upper())
    print((f"\t\t\t {player_two.upper()}'s Sign is - O").upper())
    input("\nEnter any key to start the game: ")

    print_board()

    #input part where player will input the sign
    for i in range(9):
        if i%2==0:
            index = take_input(player_one)
            print(index)
            sign_dictionary[index] = 'X'
        else:
            index = take_input_COM()
            sign_dictionary[index] = 'O'
    
        print_board()
        calculate_result_s(player_one,player_two)
    tie_img()


# Main function for Multi Player Mode
def Multi_main():

    player1 = input("Enter First Player Username: ")
    player_one = player1.upper()
    player2 = input("Enter Second Player Username: ")
    player_two = player2.upper()
    print(f"\n✧ Thank you for joining {player_one} and {player_two} ✧")

    instructions1 = """
+------------------------------------------------------------------------+
|                   THIS WILL BE OUR TIC TAC TOE GAME                    |
|                                                                        |
|                            1 | 2 | 3                                   |
|                           ---|---|---                                  |
|                            4 | 5 | 6                                   |
|                           ---|---|---                                  |
|                            7 | 8 | 9                                   |
|------------------------------------------------------------------------|
|                                                                        |
|   -*INSTRUCTIONS OF THE GAME ARE AS FOLLOWS*-                          |
|                                                                        |
|     1.Insert the spot number (1-9) to put your sign                    |
|     2.You must first all 9 spots to get the result                     |
|     3.Player one will go first                                         |
|                                                                        |
+------------------------------------------------------------------------+"""
    print(instructions1)
    print((f"\t\t\t {player_one.upper()}'s Sign is - X").upper())
    print((f"\t\t\t {player_two.upper()}'s Sign is - O").upper())
    input("\nEnter any key to start the game: ")

    print_board()

    #input part where player will input the sign
    for i in range(9):
        if i%2==0:
            index = take_input(player_one)
            sign_dictionary[index] = 'X'
        else:
            index = take_input(player_two)
            sign_dictionary[index] = 'O'
    
        print_board()
        calculate_result_m(player_one,player_two)
    tie_img()


#Implemtation and Combining Both the Main Function into One Main Function
def main():
    welcome()
    s_or_m()
    single_or_multi=input("YOUR CHOICE : ")
    if single_or_multi.upper()=="S":
           Single_main()
    elif single_or_multi.upper()=="M":
            Multi_main()
    else:
            invalid_img()
            
   
         
#Running the main function     
main()