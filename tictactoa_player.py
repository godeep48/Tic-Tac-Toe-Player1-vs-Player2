def print_output():
    print(" ","|"," ","|"," ")
    print(player1.num[0],"|",player1.num[1],"|",player1.num[2])
    print(" ","|"," ","|"," ")
    print("---------")
    print(" ","|"," ","|"," ")
    print(player1.num[3],"|",player1.num[4],"|",player1.num[5])
    print(" ","|"," ","|"," ")
    print("---------")
    print(" ","|"," ","|"," ")
    print(player1.num[6],"|",player1.num[7],"|",player1.num[8])
    print(" ","|"," ","|"," ")
    
def player1_break_func():
    for i in range(len(player1.player_pattern)):
        player1.player_pattern.pop(0)

player1_score = []
player2_score = []
def check():
    if player1.num[0]==player1.num[1]==player1.num[2]=="X" or \
    player1.num[3]==player1.num[4]==player1.num[5]=="X" or \
    player1.num[6]==player1.num[7]==player1.num[8]=="X" or \
    player1.num[0]==player1.num[3]==player1.num[6]=="X" or \
    player1.num[1]==player1.num[4]==player1.num[7]=="X" or \
    player1.num[2]==player1.num[5]==player1.num[8]=="X" or \
    player1.num[0]==player1.num[4]==player1.num[8]=="X" or \
    player1.num[2]==player1.num[4]==player1.num[6]=="X":
        player1_break_func()
        player1_score.append("1")
        print("Player1(X) won the match")
    elif player1.num[0]==player1.num[1]==player1.num[2]=="O" or \
    player1.num[3]==player1.num[4]==player1.num[5]=="O" or \
    player1.num[6]==player1.num[7]==player1.num[8]=="O" or \
    player1.num[0]==player1.num[3]==player1.num[6]=="O" or \
    player1.num[1]==player1.num[4]==player1.num[7]=="O" or \
    player1.num[2]==player1.num[5]==player1.num[8]=="O" or \
    player1.num[0]==player1.num[4]==player1.num[8]=="O" or \
    player1.num[2]==player1.num[4]==player1.num[6]=="O":
        player1_break_func()
        player2_score.append("1")
        print("Player2(O) won the match")

from IPython.display import clear_output
class Player1():
    def __init__(self,num,player_pattern):
        self.num = num
        self.player_pattern=player_pattern
    def player1_turn(self):
        while True:
            if len(self.player_pattern) != 0:
                player1_input = int(input("Enter the player1 input value"))
                self.num[player1_input-1] = self.player_pattern.pop(0)
                clear_output()
                print_output()
                check()
                if len(self.player_pattern) != 0:
                    player2_input = int(input("Enter the player2 input value"))
                    self.num[player2_input-1] = self.player_pattern.pop(0)
                    clear_output()
                    print_output()
                    check()
                elif len(self.player_pattern) == 0:
                    break
            elif len(self.player_pattern) == 0:
                break
    def player2_turn(self):
        while True:
            if len(self.player_pattern) != 0:
                player2_input = int(input("Enter the player2 input value"))
                self.num[player2_input-1] = self.player_pattern.pop(0)
                clear_output()
                print_output()
                check()
                if len(self.player_pattern) != 0:
                    player1_input = int(input("Enter the player1 input value"))
                    self.num[player1_input-1] = self.player_pattern.pop(0)
                    clear_output()
                    print_output()
                    check()
                elif len(self.player_pattern) == 0:
                    break
            elif len(self.player_pattern) == 0:
                break

game_play = 0
while True:
    if game_play < 5:
        game_play += 1
        numbers1 = [" "]*9
        pattern1 = ["X","O","X","O","X","O","X","O","X"]
        #pattern1 = ["O","X","O","X","O","X","O","X","O"]
        player1 = Player1(numbers1,pattern1)
        player1.player1_turn()
        if game_play < 5:
            game_play += 1
            numbers2 = [" "]*9
            #pattern1 = ["X","O","X","O","X","O","X","O","X"]
            pattern2 = ["O","X","O","X","O","X","O","X","O"]
            player1 = Player1(numbers2,pattern2)
            player1.player2_turn()
        elif game_play == 5:
            break
    elif game_play == 5:
        break
        
if len(player1_score) > len(player2_score):
    print(f"Player 1 (X) won the tournament with score {len(player1_score)}:{len(player2_score)}")
elif len(player2_score) > len(player1_score):
    print(f"Player 2 (O) won the tournamant with score {len(player2_score)}:{len(player1_score)}")
elif len(player1_score) == len(player2_score):
    print(f"This tournament is a tie with score {len(player1_score)}:{len(player2_score)}")