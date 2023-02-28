#! python3

class Tile():
    columns = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
    rows = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8'}
    def __init__(self,column,row):
        self.column = column
        self.row = row
    
    def __repr__(self):
        return str(self.columns.get(self.column) + self.rows.get(self.row))
    
class Board():
    def __init__(self):
        self.board = {}
        for i in range (1,9):
            for j in range(1,9):
                self.board.update({str(Tile(i,j)):' '})

    def Show_board(self):
            self.num = 0
            slova = ['A','B','C','D','E','F','G','H']
            print('    1    2    3    4    5    6    7    8  ')
            for i in slova:
                print('   ___  ___  ___  ___  ___  ___  ___  ___ ')
                print('  |   ||   ||   ||   ||   ||   ||   ||   |')
                print('{} | {} || {} || {} || {} || {} || {} || {} || {} |'.format(i,list(self.board.values())[self.num],list(self.board.values())[self.num+1],list(self.board.values())[self.num+2],list(self.board.values())[self.num+3],list(self.board.values())[self.num+4],list(self.board.values())[self.num+5],list(self.board.values())[self.num+6],list(self.board.values())[self.num+7]))
                print('  |___||___||___||___||___||___||___||___|')
                self.num +=8
            self.num=0
    
class Player():
    def __init__(self,name):
        self.name = name
        self.turn = None
        self.brodovi = {}
        self.player_bord = Board()
        self.guesses = []
        self.guess = '$'

class Game():
    def __init__(self):
        print('Dobrodošli u potapanje brodova :)')
        print()
        name1 = input ('Player 1 name : ')
        print()
        name2 = input ('Player 2 name : ')
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.players = [self.player1,self.player2]
        for player in self.players:
            print()
            print('{} smjesti 2 broda duljine 2 polja na ploču npr.(A1,A2 i C6,D6)'.format(player.name))
            for j in range(4):
                brod = input()
                while True:
                    if brod not in list(player.player_bord.board.keys()):
                        brod = input('Unesi pravilno polje : ')
                    elif brod in player.brodovi.keys():
                        brod = input('Već imaš brod na tom polju, molim te unesi drugo polje : ')
                    else:
                        player.brodovi.update({brod:0})
                        break
            print('{} smjesti 2 broda duljine 3 polja na ploču npr.(A1,A2,A3 i C6,D6,E6)'.format(player.name))
            for j in range(6):
                brod = input()
                while True:
                    if brod not in list(player.player_bord.board.keys()):
                        brod = input('Unesi pravilno polje : ')
                    elif brod in player.brodovi.keys():
                        brod = input('Već imaš brod na tom polju, molim te unesi drugo polje : ')
                    else:
                        player.brodovi.update({brod:0})
                        break
            print('{} smjesti 1 brod duljine 4 polja na ploču npr.(A1,A2,A3,A4)'.format(player.name))
            for j in range(4):
                brod = input()
                while True:
                    if brod not in list(player.player_bord.board.keys()):
                        brod = input('Unesi pravilno polje : ')
                    elif brod in player.brodovi.keys():
                        brod = input('Već imaš brod na tom polju, molim te unesi drugo polje : ')
                    else:
                        player.brodovi.update({brod:0})
                        break
            for i in range(10):
                print()
                     
        first = input('Unesi ime igrača koji će započeti igru : ')
        while True:
            if first == name1:
                self.player1.turn = True
                break
            elif first == name2:
                self.player2.turn = True
                break
            else:
                first = input('Ponovno unesi ime igrača koji će započeti igru : ')
        print()

    def Play_game(self):
        while self.player1.brodovi != {} and self.player2.brodovi != {}:

            while self.player1.turn == True and (self.player1.brodovi != {} and self.player2.brodovi != {}):
                print("{}'s turn!".format(self.player1.name))
                print()
                print()
                self.player1.player_bord.Show_board()
                print()
                self.player1.guess = input('Upiši polje npr.(A1,B3,G7) : ')
                while True:
                    if self.player1.guess not in list(self.player2.player_bord.board.keys()):
                        self.player1.guess = input('Unesi pravilno polje : ')
                    elif self.player1.guess in self.player1.guesses:
                        self.player1.guess = input('Već si pogađao to polje : ')
                    else:
                        self.player1.guesses.append(self.player1.guess)
                        self.player1.turn = False
                        self.player2.turn = True
                        if self.player1.guess in list(self.player2.brodovi.keys()):
                            self.player2.brodovi.pop(self.player1.guess)
                            self.player1.player_bord.board.update({self.player1.guess:'X'})
                        else:
                            self.player1.player_bord.board.update({self.player1.guess:'O'})
                        break
                print()
            
            while self.player2.turn == True and (self.player1.brodovi != {} and self.player2.brodovi != {}):
                print("{}'s turn!".format(self.player2.name))
                print()
                print()
                self.player2.player_bord.Show_board()
                print()
                self.player2.guess = input('Upiši polje npr.(A1,B3,G7) : ')
                while True:
                    if self.player2.guess not in list(self.player1.player_bord.board.keys()):
                        self.player2.guess = input('Unesi pravilno polje : ')
                    elif self.player2.guess in self.player2.guesses:
                        self.player2.guess = input('Već si pogađao to polje : ')
                    else:
                        self.player2.guesses.append(self.player2.guess)
                        self.player2.turn = False
                        self.player1.turn = True
                        if self.player2.guess in list(self.player1.brodovi.keys()):
                            self.player1.brodovi.pop(self.player2.guess)
                            self.player2.player_bord.board.update({self.player2.guess:'X'})
                        else:
                            self.player2.player_bord.board.update({self.player2.guess:'O'})
                        break
                print()

        self.win()

    def win(self):
        if self.player1.brodovi == {}:
            print('{} wins the game !!!'.format(self.player2.name))
        else:
            print('{} wins the game !!!'.format(self.player1.name))

game = Game()
game.Play_game()
