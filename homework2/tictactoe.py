import random
import tkinter as tk
from abc import ABC, abstractmethod


WIN_LINES = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [11, 12, 13, 14, 15],
    [12, 13, 14, 15, 16],
    [13, 14, 15, 16, 17],
    [14, 15, 16, 17, 18],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [21, 22, 23, 24, 25],
    [22, 23, 24, 25, 26],
    [23, 24, 25, 26, 27],
    [24, 25, 26, 27, 28],
    [25, 26, 27, 28, 29],
    [30, 31, 32, 33, 34],
    [31, 32, 33, 34, 35],
    [32, 33, 34, 35, 36],
    [33, 34, 35, 36, 37],
    [34, 35, 36, 37, 38],
    [35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44],
    [41, 42, 43, 44, 45],
    [42, 43, 44, 45, 46],
    [43, 44, 45, 46, 47],
    [44, 45, 46, 47, 48],
    [45, 46, 47, 48, 49],
    [50, 51, 52, 53, 54],
    [51, 52, 53, 54, 55],
    [52, 53, 54, 55, 56],
    [53, 54, 55, 56, 57],
    [54, 55, 56, 57, 58],
    [55, 56, 57, 58, 59],
    [60, 61, 62, 63, 64],
    [61, 62, 63, 64, 65],
    [62, 63, 64, 65, 66],
    [63, 64, 65, 66, 67],
    [64, 65, 66, 67, 68],
    [65, 66, 67, 68, 69],
    [70, 71, 72, 73, 74],
    [71, 72, 73, 74, 75],
    [72, 73, 74, 75, 76],
    [73, 74, 75, 76, 77],
    [74, 75, 76, 77, 78],
    [75, 76, 77, 78, 79],
    [80, 81, 82, 83, 84],
    [81, 82, 83, 84, 85],
    [82, 83, 84, 85, 86],
    [83, 84, 85, 86, 87],
    [84, 85, 86, 87, 88],
    [85, 86, 87, 88, 89],
    [90, 91, 92, 93, 94],
    [91, 92, 93, 94, 95],
    [92, 93, 94, 95, 96],
    [93, 94, 95, 96, 97],
    [94, 95, 96, 97, 98],
    [95, 96, 97, 98, 99],
    [0, 10, 20, 30, 40],
    [1, 11, 21, 31, 41],
    [2, 12, 22, 32, 42],
    [3, 13, 23, 33, 43],
    [4, 14, 24, 34, 44],
    [5, 15, 25, 35, 45],
    [6, 16, 26, 36, 46],
    [7, 17, 27, 37, 47],
    [8, 18, 28, 38, 48],
    [9, 19, 29, 39, 49],
    [10, 20, 30, 40, 50],
    [11, 21, 31, 41, 51],
    [12, 22, 32, 42, 52],
    [13, 23, 33, 43, 53],
    [14, 24, 34, 44, 54],
    [15, 25, 35, 45, 55],
    [16, 26, 36, 46, 56],
    [17, 27, 37, 47, 57],
    [18, 28, 38, 48, 58],
    [19, 29, 39, 49, 59],
    [20, 30, 40, 50, 60],
    [21, 31, 41, 51, 61],
    [22, 32, 42, 52, 62],
    [23, 33, 43, 53, 63],
    [24, 34, 44, 54, 64],
    [25, 35, 45, 55, 65],
    [26, 36, 46, 56, 66],
    [27, 37, 47, 57, 67],
    [28, 38, 48, 58, 68],
    [29, 39, 49, 59, 69],
    [30, 40, 50, 60, 70],
    [31, 41, 51, 61, 71],
    [32, 42, 52, 62, 72],
    [33, 43, 53, 63, 73],
    [34, 44, 54, 64, 74],
    [35, 45, 55, 65, 75],
    [36, 46, 56, 66, 76],
    [37, 47, 57, 67, 77],
    [38, 48, 58, 68, 78],
    [39, 49, 59, 69, 79],
    [40, 50, 60, 70, 80],
    [41, 51, 61, 71, 81],
    [42, 52, 62, 72, 82],
    [43, 53, 63, 73, 83],
    [44, 54, 64, 74, 84],
    [45, 55, 65, 75, 85],
    [46, 56, 66, 76, 86],
    [47, 57, 67, 77, 87],
    [48, 58, 68, 78, 88],
    [49, 59, 69, 79, 89],
    [50, 60, 70, 80, 90],
    [51, 61, 71, 81, 91],
    [52, 62, 72, 82, 92],
    [53, 63, 73, 83, 93],
    [54, 64, 74, 84, 94],
    [55, 65, 75, 85, 95],
    [56, 66, 76, 86, 96],
    [57, 67, 77, 87, 97],
    [58, 68, 78, 88, 98],
    [59, 69, 79, 89, 99],
    [4, 13, 22, 31, 40],
    [5, 14, 23, 32, 41],
    [14, 23, 32, 41, 50],
    [6, 15, 24, 33, 42],
    [15, 24, 33, 42, 51],
    [24, 33, 42, 51, 60],
    [7, 16, 25, 34, 43],
    [16, 25, 34, 43, 52],
    [25, 34, 43, 52, 61],
    [34, 43, 52, 61, 70],
    [8, 17, 26, 35, 44],
    [17, 26, 35, 44, 53],
    [26, 35, 44, 53, 62],
    [35, 44, 53, 62, 71],
    [44, 53, 62, 71, 80],
    [9, 18, 27, 36, 45],
    [18, 27, 36, 45, 54],
    [27, 36, 45, 54, 63],
    [36, 45, 54, 63, 72],
    [45, 54, 63, 72, 81],
    [54, 63, 72, 81, 90],
    [19, 28, 37, 46, 55],
    [28, 37, 46, 55, 64],
    [37, 46, 55, 64, 73],
    [46, 55, 64, 73, 82],
    [55, 64, 73, 82, 91],
    [29, 38, 47, 56, 65],
    [38, 47, 56, 65, 74],
    [47, 56, 65, 74, 83],
    [56, 65, 74, 83, 92],
    [39, 48, 57, 66, 75],
    [48, 57, 66, 75, 84],
    [57, 66, 75, 84, 93],
    [49, 58, 67, 76, 85],
    [58, 67, 76, 85, 94],
    [59, 68, 77, 86, 95],
    [5, 16, 27, 38, 49],
    [4, 15, 26, 37, 48],
    [15, 26, 37, 48, 59],
    [3, 14, 25, 36, 47],
    [14, 25, 36, 47, 58],
    [25, 36, 47, 58, 69],
    [2, 13, 24, 35, 46],
    [13, 24, 35, 46, 57],
    [24, 35, 46, 57, 68],
    [35, 46, 57, 68, 79],
    [1, 12, 23, 34, 45],
    [12, 23, 34, 45, 56],
    [23, 34, 45, 56, 67],
    [34, 45, 56, 67, 78],
    [45, 56, 67, 78, 89],
    [0, 11, 22, 33, 44],
    [11, 22, 33, 44, 55],
    [22, 33, 44, 55, 66],
    [33, 44, 55, 66, 77],
    [44, 55, 66, 77, 88],
    [55, 66, 77, 88, 99],
    [10, 21, 32, 43, 54],
    [21, 32, 43, 54, 65],
    [32, 43, 54, 65, 76],
    [43, 54, 65, 76, 87],
    [54, 65, 76, 87, 98],
    [20, 31, 42, 53, 64],
    [31, 42, 53, 64, 75],
    [42, 53, 64, 75, 86],
    [53, 64, 75, 86, 97],
    [30, 41, 52, 63, 74],
    [41, 52, 63, 74, 85],
    [52, 63, 74, 85, 96],
    [40, 51, 62, 73, 84],
    [51, 62, 73, 84, 95],
    [50, 61, 72, 83, 94],
]


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Обратные крестики-нолики 10x10')
        self._main_canvas = None
        self.switch_canvas(StartPage)

    def switch_canvas(self, canvas_class):
        if self._main_canvas:
            self._main_canvas.pack_forget()
        canvas = canvas_class(self)
        self._main_canvas = canvas


class StartPage(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack(pady=25, padx=30)
        tk.Label(
            self, text="КРЕСТИКИ-НОЛИКИ",
            font=('Segoe Print', 20, 'bold')
        ).grid(column=0, row=0, pady=5, padx=30)
        tk.Button(
            self, text="Новая игра",
            font=('Segoe Print', 15, 'bold'), bg='white',
            command=lambda: master.switch_canvas(ReverseGame)
        ).grid(column=0, row=3, pady=2)
        tk.Button(
            self, text="Выход",
            font=('Segoe Print', 15, 'bold'), bg='white',
            command=master.destroy
        ).grid(column=0, row=4, pady=2)


class CreateBoard(tk.Canvas, ABC):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack(pady=(20, 60), padx=40)
        self.player_one = ''
        self.player_two = ''
        self.who_plays = ''
        self.board = {}
        self.buttons = []
        self.create_buttons()
        self.create_board()
        self.move_label = tk.Label(
            self, text="Выберите сторону", font=(
                'Segoe Print', 20, 'bold'), bd=4)
        self.move_label.grid(column=10, row=4, columnspan=2, padx=(32, 0))
        self.name_label = tk.Label(
            self, text="", font=(
                'Segoe Print', 20, 'bold'), bd=4)
        self.name_label.grid(column=0, row=0, columnspan=10, pady=(0, 20))
        self.restart = tk.Button(
            self,
            text="Новая игра",
            font=(
                'Segoe Print',
                14,
                'bold'),
            bg='white',
            width=10,
            bd=4,
            state=tk.DISABLED)
        self.restart.grid(column=10, row=8, columnspan=2, padx=(30, 0))
        self.main_button = tk.Button(
            self,
            text="Выход",
            font=(
                'Segoe Print',
                15,
                'bold'),
            bd=4,
            bg='white',
            width=10,
            command=master.destroy)
        self.main_button.grid(
            column=10,
            row=9,
            rowspan=2,
            columnspan=2,
            padx=(
                30,
                0))
        self.all_winning_conditions = WIN_LINES

    def create_board(self):
        for i in range(100):
            self.board[i] = ''

    def create_buttons(self):
        x = 0
        for i in range(10):
            for n in range(10):
                self.buttons.append(x)
                self.buttons[x] = tk.Button(
                    self,
                    text='',
                    bd=4,
                    height=1,
                    width=4,
                    font=(
                        "Segoe Print",
                        14,
                        'bold'),
                    state=tk.DISABLED,
                    command=lambda x=x: self.make_move(x))
                self.buttons[x].grid(row=i + 1, column=n)
                x += 1

    def check_winner_conditions(self):
        win = False
        for condition in self.all_winning_conditions:
            not_empty = all(self.board[ele] != '' for ele in condition)
            x_sign = all(self.board[ele] == 'X' for ele in condition)
            o_sign = all(self.board[ele] == 'O' for ele in condition)
            if not_empty and (x_sign or o_sign):
                win = True
                self.move_label['text'] = f'{self.who_plays}\nwins!'
                for i in condition:
                    self.buttons[i].configure(bg='#b7e4c7')
                break
        return win

    def check_draw(self):
        draw = False
        x = [k for k, v in self.board.items() if v == '']
        if not x:
            draw = True
            self.move_label['text'] = "It's Draw!"
        return draw

    def check_play_state(self):
        check_win = self.check_winner_conditions()
        check_draw = self.check_draw()

        endgame = False
        if check_win or check_draw:
            for i in self.buttons:
                i.configure(command=lambda: None)
                endgame = True
        return endgame

    @abstractmethod
    def start_game(self, sign):
        pass

    @abstractmethod
    def make_move(self, button_number):
        pass


class GameBaseSettings(CreateBoard, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_one = 'Player'
        self.player_two = 'AI'
        self.player_sign = ''
        self.ai_sign = ''
        self.bot_dict = {}
        self.player_dict = {}
        self.all_data = {}
        self.button = 0
        self.x_button = tk.Button(
            self,
            text="X",
            font=(
                'Segoe Print',
                13,
                'bold'),
            bg='white',
            height=0,
            width=4,
            bd=4,
            command=lambda: self.start_game('X'),
            fg="red")
        self.x_button.grid(column=10, row=5, padx=(30, 0))
        self.o_button = tk.Button(
            self,
            text="O",
            font=(
                'Segoe Print',
                13,
                'bold'),
            bg='white',
            height=0,
            width=4,
            bd=4,
            command=lambda: self.start_game('O'),
            fg="blue")
        self.o_button.grid(column=11, row=5, padx=(30, 0))

    def start_game(self, sign):
        for i in self.buttons:
            i['state'] = tk.NORMAL
        self.x_button.grid_forget()
        self.o_button.grid_forget()
        self.restart['state'] = tk.NORMAL
        self.move_label.grid(
            column=10,
            row=4,
            rowspan=2,
            columnspan=2,
            padx=(
                32,
                0))
        if sign == 'X':
            self.player_sign = 'X'
            self.ai_sign = 'O'
            self.who_plays = self.player_one
        if sign == 'O':
            self.player_sign = 'O'
            self.ai_sign = 'X'
            self.who_plays = self.player_two
            self.ai_move()
        self.move_label['text'] = 'Удачной игры!'

    def make_move(self, button_number):
        if self.buttons[button_number]['text'] != '':
            pass
        else:
            if self.who_plays == self.player_one:
                if self.player_sign == 'X':
                    self.buttons[button_number]['text'] = 'X'
                    self.buttons[button_number]['fg'] = 'red'
                    self.board[button_number] = 'X'
                else:
                    self.buttons[button_number]['text'] = 'O'
                    self.buttons[button_number]['fg'] = 'blue'
                    self.board[button_number] = 'O'
            else:
                if self.ai_sign == 'X':
                    self.buttons[button_number]['text'] = 'X'
                    self.buttons[button_number]['fg'] = 'red'
                    self.board[button_number] = 'X'
                else:
                    self.buttons[button_number]['text'] = 'O'
                    self.buttons[button_number]['fg'] = 'blue'
                    self.board[button_number] = 'O'
            x = self.check_play_state()
            if not x:
                if self.who_plays == self.player_one:
                    self.who_plays = self.player_two
                    self.ai_move()
                else:
                    self.who_plays = self.player_one
            self.check_play_state()

    def ai_win_conditions(self):
        for condition in self.all_winning_conditions:
            x_sign = 0
            o_sign = 0
            empty = 0

            for i in condition:
                if self.board[i] == 'X':
                    x_sign += 1
                elif self.board[i] == 'O':
                    o_sign += 1
                elif self.board[i] == '':
                    empty += 1
            self.all_data[self.all_winning_conditions.index(condition)] = {
                'X': x_sign,
                'O': o_sign,
                '': empty
            }
        for i in range(6):
            self.bot_dict[i] = [
                self.all_winning_conditions[k] for k, v in
                self.all_data.items() if
                v[self.player_sign] < 1 and v[self.ai_sign] == i
            ]

            self.player_dict[i] = [
                self.all_winning_conditions[k] for k, v in
                self.all_data.items() if
                v[self.ai_sign] < 1 and v[self.player_sign] == i
            ]

    @abstractmethod
    def ai_move(self):
        pass


class ReverseGame(GameBaseSettings):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_label['text'] = 'Обратные крестики нолики'
        self.restart.configure(
            command=lambda: self.master.switch_canvas(ReverseGame))
        self.best_ai_move = 0

    def check_winner_conditions(self):
        win = False
        for condition in self.all_winning_conditions:
            not_empty = all(self.board[ele] != '' for ele in condition)
            x_sign = all(self.board[ele] == 'X' for ele in condition)
            o_sign = all(self.board[ele] == 'O' for ele in condition)
            if not_empty and (x_sign or o_sign):
                win = True
                self.move_label['text'] = f'{self.who_plays}\nlost!'
                for i in condition:
                    self.buttons[i].configure(bg='#FF5C58')
                break
        return win

    def check_play_state(self):
        check_win = self.check_winner_conditions()
        endgame = False
        if check_win:
            for i in self.buttons:
                i.configure(command=lambda: None)
                endgame = True
        return endgame

    def ai_move(self):
        if all(self.board[i] == '' for i in range(100)):
            random_numbers = [33, 34, 35, 36, 43, 44,
                              45, 46, 53, 54, 55, 56, 63, 64, 65, 66]
            self.button = random.choice(random_numbers)
        else:
            self.ai_win_conditions()

            if len(
                self.bot_dict[1]) == 0 and len(
                self.bot_dict[2]) == 0 and len(
                self.bot_dict[3]) == 0 and len(
                    self.bot_dict[4]) == 0:
                move = random.choice([i for i in self.bot_dict[0]])
                self.button = random.choice(move)

            elif len(self.bot_dict[0]) > 0:
                possible_moves = [i for i in self.bot_dict[0]]
                all_moves = []
                self.best_ai_move = None
                current_length_2 = len(self.bot_dict[2])
                current_length_3 = len(self.bot_dict[3])
                current_length_4 = len(self.bot_dict[4])
                current_length_5 = len(self.bot_dict[5])
                for move in possible_moves:
                    for pos in move:
                        if pos not in all_moves:
                            all_moves.append(pos)
                shuffled_moves = random.sample(all_moves, len(all_moves))
                for move in shuffled_moves:
                    self.board[move] = self.ai_sign
                    self.ai_win_conditions()
                    if len(
                            self.bot_dict[2]) == current_length_2 and len(
                            self.bot_dict[3]) == current_length_3 and len(
                            self.bot_dict[4]) == current_length_4 and len(
                            self.bot_dict[5]) == current_length_5:
                        self.best_ai_move = move
                        self.board[move] = ''
                        break
                    else:
                        self.board[move] = ''
                if self.best_ai_move is None:
                    for move in shuffled_moves:
                        self.board[move] = self.ai_sign
                        self.ai_win_conditions()
                        if len(
                                self.bot_dict[3]) == current_length_3 and len(
                                self.bot_dict[4]) == current_length_4 and len(
                                self.bot_dict[5]) == current_length_5:
                            self.best_ai_move = move
                            self.board[move] = ''
                            break
                        else:
                            self.board[move] = ''
                if self.best_ai_move is None:
                    for move in shuffled_moves:
                        self.board[move] = self.ai_sign
                        self.ai_win_conditions()
                        if len(
                                self.bot_dict[4]) == current_length_4 and len(
                                self.bot_dict[5]) == current_length_5:
                            self.best_ai_move = move
                            self.board[move] = ''
                            break
                        else:
                            self.board[move] = ''
                if self.best_ai_move is None:
                    for move in shuffled_moves:
                        self.board[move] = self.ai_sign
                        self.ai_win_conditions()
                        if len(self.bot_dict[5]) == current_length_5:
                            self.best_ai_move = move
                            self.board[move] = ''
                            break
                        else:
                            self.board[move] = ''
                if self.best_ai_move is None:
                    self.best_ai_move = random.choice(shuffled_moves)
                self.button = self.best_ai_move

            elif len(self.bot_dict[1]) > 0:
                possible_moves = [i for i in self.bot_dict[1]]
                all_moves = []
                self.best_ai_move = None
                current_length_3 = len(self.bot_dict[3])
                current_length_4 = len(self.bot_dict[4])
                current_length_5 = len(self.bot_dict[5])
                for move in possible_moves:
                    for pos in move:
                        cond = (
                            pos not in all_moves and
                            self.board[pos] != self.ai_sign
                        )
                        if cond:
                            all_moves.append(pos)
                shuffled_moves = random.sample(all_moves, len(all_moves))
                for move in shuffled_moves:
                    self.board[move] = self.ai_sign
                    self.ai_win_conditions()
                    if len(
                            self.bot_dict[3]) == current_length_3 and len(
                            self.bot_dict[4]) == current_length_4 and len(
                            self.bot_dict[5]) == current_length_5:
                        self.best_ai_move = move
                        self.board[move] = ''
                        break
                    else:
                        self.board[move] = ''
                if self.best_ai_move is None:
                    for move in shuffled_moves:
                        self.board[move] = self.ai_sign
                        self.ai_win_conditions()
                        if len(
                                self.bot_dict[4]) == current_length_4 and len(
                                self.bot_dict[5]) == current_length_5:
                            self.best_ai_move = move
                            self.board[move] = ''
                            break
                        else:
                            self.board[move] = ''
                if self.best_ai_move is None:
                    for move in shuffled_moves:
                        self.board[move] = self.ai_sign
                        self.ai_win_conditions()
                        if len(self.bot_dict[5]) == current_length_5:
                            self.best_ai_move = move
                            self.board[move] = ''
                            break
                        else:
                            self.board[move] = ''
                if self.best_ai_move is None:
                    self.best_ai_move = random.choice(shuffled_moves)
                self.button = self.best_ai_move

            elif len(self.bot_dict[2]) > 0:
                possible_moves = [i for i in self.bot_dict[2]]
                all_moves = []
                self.best_ai_move = None
                current_length_4 = len(self.bot_dict[4])
                current_length_5 = len(self.bot_dict[5])
                for move in possible_moves:
                    for pos in move:
                        cond = (
                            pos not in all_moves and
                            self.board[pos] != self.ai_sign
                        )
                        if cond:
                            all_moves.append(pos)
                shuffled_moves = random.sample(all_moves, len(all_moves))
                for move in shuffled_moves:
                    self.board[move] = self.ai_sign
                    self.ai_win_conditions()
                    if len(
                            self.bot_dict[4]) == current_length_4 and len(
                            self.bot_dict[5]) == current_length_5:
                        self.best_ai_move = move
                        self.board[move] = ''
                        break
                    else:
                        self.board[move] = ''
                if self.best_ai_move is None:
                    for move in shuffled_moves:
                        self.board[move] = self.ai_sign
                        self.ai_win_conditions()
                        if len(self.bot_dict[5]) == current_length_5:
                            self.best_ai_move = move
                            self.board[move] = ''
                            break
                        else:
                            self.board[move] = ''
                if self.best_ai_move is None:
                    self.best_ai_move = random.choice(shuffled_moves)
                self.button = self.best_ai_move

            elif len(self.bot_dict[3]) > 0:
                possible_moves = [i for i in self.bot_dict[3]]
                all_moves = []
                self.best_ai_move = None
                current_length_5 = len(self.bot_dict[5])
                for move in possible_moves:
                    for pos in move:
                        cond = (
                            pos not in all_moves and
                            self.board[pos] != self.ai_sign
                        )
                        if cond:
                            all_moves.append(pos)
                shuffled_moves = random.sample(all_moves, len(all_moves))
                for move in shuffled_moves:
                    self.board[move] = self.ai_sign
                    self.ai_win_conditions()
                    if len(self.bot_dict[5]) == current_length_5:
                        self.best_ai_move = move
                        self.board[move] = ''
                        break
                    else:
                        self.board[move] = ''
                if self.best_ai_move is None:
                    spaces_left = [k for k, v in self.board.items() if v == '']
                    self.best_ai_move = random.choice(spaces_left)
                self.button = self.best_ai_move

        self.buttons[self.button].invoke()


gui = TicTacToe()
gui.mainloop()
