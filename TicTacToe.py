import enum
import itertools
from colorama import Fore, Back, Style, init
init()

def game_board(game_map, player=0, row=0, column=0, just_display=False): # ileride fonksiyonu girdi olmadan çağırabilmek için  =0 şeklinde varsayılan değerler atandı
    try:
        if game_map[row][column] != 0:
            print("This place has been occupied! Choose another.")
            return game_map, False
        if not just_display:
            game_map[row][column] = player
        print(" ")
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                else:
                    colored_row += colored(item)
            print(count, colored_row)
        print(" ")
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2 :", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

def all_same(list):
    won = False
    if list.count(list[0]) == len(list) and list[0] != 0:
        won = True
    return won

def colored(player):
    colored_player = ""
    if player == 1:
        colored_player += Back.GREEN + ' X ' + Style.RESET_ALL
    elif player == 2:
        colored_player += Back.MAGENTA + ' O ' + Style.RESET_ALL
    return colored_player

def win(current_game):

# horizontally checks if game winned
    for row in current_game:
        if all_same(row):
            print(f"Player {colored(row[0])} is the winner horizontally (-) !")
            return True

# vertically checks if game winned
    for col in range(len(current_game)):
        column = []
    
        for row in current_game:
            column.append(row[col])
    
        if all_same(column):
            print(f"Player {colored(column[0])} is the winner vertically (|) !")
            return True

# diagonally \ checks if game winned
    diagonals = []

    for lr in range(len(current_game)):
        diagonals.append(current_game[lr][lr])

    if all_same(diagonals):
        print(f"Player {colored(diagonals[0])} is the winner diagonally (\\) !")
        return True
    
# diagonally / checks if game winned
    diagonals = []

    rows = range(len(current_game))

    for rl in rows:
        diagonals.append(current_game[len(rows)-rl-1][rl])

    if all_same(diagonals):
        print(f"Player {colored(diagonals[0])} is the winner diagonally (/) !")
        return True

    return False

play = True
players = [1, 2]

while play:
    game_size = int(input("What is the size of the game of Tic Tac Toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
       # [] kullanıldığında tuple değil list oluyor ve değiştirilebiliyormuş
    
    game_won = False
    game, _ = game_board(game, just_display=True) # değişkene birden fazla tip atanabilmesi için -bu örnekte hem matris hem boolean operatörü- "_" alttan tire işareti ekliyoruz "," virgülden sonra
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {colored(current_player)}")

        played = False
        while not played:
            column_choice = int(input("What column do you want to play? " + str(list(range(game_size))) + " : "))
            row_choice = int(input("What row do you want to play? " + str(list(range(game_size))) + " : "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting...")
            elif again.lower() == "n":
                print("Selam!")
                play = False
            else:
                print("Not a valid answer, so... c u l8r alligator")
                play = False