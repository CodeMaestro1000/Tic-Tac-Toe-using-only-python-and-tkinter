import tkinter as tk
import tkinter.font as font
import tkinter.messagebox
import random


def new_game():
    new_root = tk.Tk()
    GameWindow(new_root)
    new_root.mainloop()


def delay(val):
    i = 0
    while i < val:
        i += 1


class GameWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('X and O')
        self.parent.geometry('400x520+400+150')
        self.parent.resizable(0, 0)
        self.turn = tk.StringVar()
        self.turn.set('X')
        self.player_mark = 'X'
        self.player_turn = 0
        self.player = ''
        self.var = ''
        self.my_font = font.Font(family='Helvetica', size=17, weight='bold')
        self.other_font = font.Font(family='Helvetica', size=9, weight='bold')
        self.label = tk.Label(self.parent)
        self.frame = tk.Frame(self.parent)
        self.frame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=25)
        self.button1 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(1))
        self.button2 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(2))
        self.button3 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(3))
        self.button4 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(4))
        self.button5 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(5))
        self.button6 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(6))
        self.button7 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(7))
        self.button8 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(8))
        self.button9 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.play_to(9))
        self.place_buttons()
        self.undo_button = tk.Button(self.frame, text='Undo Last Move', command=self.undo_command)
        self.undo_button.grid(row=5, column=2, pady=3)
        self.move_dict = {'button1': '', 'button2': '', 'button3': '', 'button4': '', 'button5': '', 'button6': '',
                          'button7': '', 'button8': '', 'button9': ''}
        self.row1 = []
        self.row2 = []
        self.row3 = []

        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.diagonal_a = []
        self.diagonal_b = []

        self.board = {'row1': self.row1, 'row2': self.row2, 'row3': self.row3, 'col1': self.col1, 'col2': self.col2,
                      'col3': self.col3, 'diagonal_a': self.diagonal_a, 'diagonal_b': self.diagonal_b}
        self.moves = 0
        self.track_moves = []
        self.possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.first = ''

        self.ai_win = {'row1': [], 'row2': [], 'row3': [], 'col1': [], 'col2': [], 'col3': [], 'diagonal_a': [],
                       'diagonal_b': []}
        self.track_ai_moves = []
        self.edge_picked = False

        self.first_player()
        self.turn_disp()
        if self.AI_plays():
            self.AI_move()

    def AI_plays(self):
        if self.player_turn == 0:
            return True
        else:
            return False

    def AI_move(self):
        b_id = self.get_best_move()
        self.button_click(b_id)
        self.place_ai_data(b_id)

    def get_best_move(self):
        try:
            last_move = self.track_moves[-1]
            print(last_move)
        except IndexError:
            last_move = None
        if last_move is not None:
            win_space = self.check_struct()  # check if there is a win
            if win_space != 0:
                move = self.place_winning_mark()
                print("Win Detected")
            else:
                last_move = self.track_moves[-1]
                block = self.should_block(last_move)
                if block['block']:  # check if should block opponent
                    move = self.block_pos(block['space'])
                else:
                    if self.move_dict['button5'] == '':
                        move = 5
                    else:
                        diagonal = self.pick_diagonals()
                        if diagonal != 0:
                            move = diagonal
                            print("Diagonal Picked")
                        else:
                            move = random.choice(self.possible_moves)
                            print("Random MOve")
        else:
            move = 5
        if move in self.track_moves:
            move = random.choice(self.possible_moves)
        return move

    def should_block(self, last_move):
        b_dict = {'block': False, 'space': ''}
        if last_move == 1:
            if self.check_spaces(self.row1):
                b_dict['block'] = True
                b_dict['space'] = 'row1'
            if self.check_spaces(self.col1):
                b_dict['block'] = True
                b_dict['space'] = 'col1'
            if self.check_spaces(self.diagonal_a):
                b_dict['block'] = True
                b_dict['space'] = 'diagonal_a'
            return b_dict
        elif last_move == 2:
            if self.check_spaces(self.row1):
                b_dict['block'] = True
                b_dict['space'] = 'row1'
            if self.check_spaces(self.col2):
                b_dict['block'] = True
                b_dict['space'] = 'col2'
            return b_dict
        elif last_move == 3:
            if self.check_spaces(self.row1):
                b_dict['block'] = True
                b_dict['space'] = 'row1'
            if self.check_spaces(self.col3):
                b_dict['block'] = True
                b_dict['space'] = 'col3'
            if self.check_spaces(self.diagonal_b):
                b_dict['block'] = True
                b_dict['space'] = 'diagonal_b'
            return b_dict
        elif last_move == 4:
            if self.check_spaces(self.row2):
                b_dict['block'] = True
                b_dict['space'] = 'row2'
            if self.check_spaces(self.col1):
                b_dict['block'] = True
                b_dict['space'] = 'col1'
            return b_dict
        elif last_move == 5:
            if self.check_spaces(self.row2):
                b_dict['block'] = True
                b_dict['space'] = 'row2'
            if self.check_spaces(self.col2):
                b_dict['block'] = True
                b_dict['space'] = 'col2'
            if self.check_spaces(self.diagonal_a):
                b_dict['block'] = True
                b_dict['space'] = 'diagonal_a'
            if self.check_spaces(self.diagonal_b):
                b_dict['block'] = True
                b_dict['space'] = 'diagonal_b'
            return b_dict
        elif last_move == 6:
            if self.check_spaces(self.row2):
                b_dict['block'] = True
                b_dict['space'] = 'row2'
            if self.check_spaces(self.col3):
                b_dict['block'] = True
                b_dict['space'] = 'col3'
            return b_dict
        elif last_move == 7:
            if self.check_spaces(self.row3):
                b_dict['block'] = True
                b_dict['space'] = 'row3'
            if self.check_spaces(self.col1):
                b_dict['block'] = True
                b_dict['space'] = 'col1'
            if self.check_spaces(self.diagonal_b):
                b_dict['block'] = True
                b_dict['space'] = 'diagonal_b'
            return b_dict
        elif last_move == 8:
            if self.check_spaces(self.row3):
                b_dict['block'] = True
                b_dict['space'] = 'row3'
            if self.check_spaces(self.col2):
                b_dict['block'] = True
                b_dict['space'] = 'col2'
            return b_dict
        elif last_move == 9:
            if self.check_spaces(self.row3):
                b_dict['block'] = True
                b_dict['space'] = 'row3'
            if self.check_spaces(self.col3):
                b_dict['block'] = True
                b_dict['space'] = 'col3'
            if self.check_spaces(self.diagonal_a):
                b_dict['block'] = True
                b_dict['space'] = 'diagonal_a'
            return b_dict
        else:
            return b_dict

    def block_pos(self, loc):
        diagonal_a = ['button1', 'button5', 'button9']
        diagonal_b = ['button3', 'button5', 'button7']
        row1 = ['button1', 'button2', 'button3']
        row2 = ['button4', 'button5', 'button6']
        row3 = ['button7', 'button8', 'button9']
        col1 = ['button1', 'button4', 'button7']
        col2 = ['button2', 'button5', 'button8']
        col3 = ['button3', 'button6', 'button9']
        if loc == 'diagonal_a':
            for i in diagonal_a:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    print('Move to : ', str(index))
                    return index
        if loc == 'diagonal_b':
            for i in diagonal_b:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index
        if loc == 'row1':
            for i in row1:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index
        if loc == 'row2':
            for i in row2:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index
        if loc == 'row3':
            for i in row3:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index
        if loc == 'col1':
            for i in col1:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index
        if loc == 'col2':
            for i in col2:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index
        if loc == 'col3':
            for i in col3:
                if self.move_dict[i] == '':
                    index = int(i[-1])
                    return index

    def check_struct(self):
        """ This function checks if there is a potential win and returns the row, column or diagonal"""
        for i, j in self.ai_win.items():
            if len(j) > 1:
                print("Yes!!!")
                return i
            else:
                print("No")
                return 0

    def place_ai_data(self, move):
        a = [1, 5, 9]
        b = [3, 5, 7]
        if move % 3 == 1:
            self.ai_win['col1'].append(move)
        if move % 3 == 2:
            self.ai_win['col2'].append(move)
        if move % 3 == 0:
            self.ai_win['col3'].append(move)
        if move <= 3:
            self.ai_win['row1'].append(move)
        if 3 < move <= 6:
            self.ai_win['row2'].append(move)
        if move > 6:
            self.ai_win['row3'].append(move)
        if move in a:
            self.ai_win['diagonal_a'].append(move)
        if move in b:
            self.ai_win['diagonal_b'].append(move)

    @staticmethod
    def check_move_list(space):
        for i in space:
            if i == '':
                return space.index(i)

    def place_winning_mark(self):
        move_to = None
        row1 = [self.move_dict['button1'], self.move_dict['button2'], self.move_dict['button3']]
        row2 = [self.move_dict['button4'], self.move_dict['button5'], self.move_dict['button6']]
        row3 = [self.move_dict['button7'], self.move_dict['button8'], self.move_dict['button9']]
        col1 = [self.move_dict['button1'], self.move_dict['button4'], self.move_dict['button7']]
        col2 = [self.move_dict['button2'], self.move_dict['button5'], self.move_dict['button8']]
        col3 = [self.move_dict['button3'], self.move_dict['button6'], self.move_dict['button9']]
        diagonal_a = [self.move_dict['button1'], self.move_dict['button5'], self.move_dict['button9']]
        diagonal_b = self.move_dict['button3'], self.move_dict['button5'], self.move_dict['button7']
        space = self.check_struct()
        if space == 'row1':
            move_to = self.check_move_list(row1)
        if space == 'row2':
            move_to = self.check_move_list(row2)
        if space == 'row3':
            move_to = self.check_move_list(row3)
        if space == 'col1':
            move_to = self.check_move_list(col1)
        if space == 'col2':
            move_to = self.check_move_list(col2)
        if space == 'col3':
            move_to = self.check_move_list(col3)
        if space == 'diagonal_a':
            move_to = self.check_move_list(diagonal_a)
        if space == 'diagonal_b':
            move_to = self.check_move_list(diagonal_b)
        return move_to

    def opp_edge_place(self):
        """This function checks if the opponent placed a marker on an edge"""
        diagonals = [1, 3, 7, 9]
        last_move = self.track_moves[-1]
        if last_move in diagonals:
            return True
        else:
            return False

    def edge_picked_action(self):
        """
         This function places a marker on the opposite edge of the diagonal that
         the opponent placed a marker on
        """
        last_move = self.track_moves[-1]
        if last_move == 1:
            return 9
        elif last_move == 3:
            return 7
        elif last_move == 7:
            return 3
        elif last_move == 9:
            return 1
        else:
            return 0

    def pick_diagonals(self):
        diagonals = [1, 3, 7, 9]
        for i in diagonals:
            if i in self.track_moves:
                diagonals.remove(i)
        if diagonals:
            picked = random.choice(diagonals)
            self.edge_picked = True
            return picked
        else:
            return 0

    def check_spaces(self, space_list):
        i = 0
        if self.player_mark == 'X':
            if len(space_list) > 1:
                if space_list[i] == space_list[i + 1] and space_list[i] == self.player_mark:
                    return True
            else:
                return False
        if self.player_mark == 'O':
            if len(space_list) > 1:
                if space_list[i] == space_list[i + 1] and space_list[i] == self.player_mark:
                    return True
        else:
            return False

    def update_turn(self):
        if self.player_turn == 1:
            self.player_turn = 0
        else:
            self.player_turn = 1

    def first_player(self):
        choice = tk.messagebox.askyesno('Go First?', 'Do you wish to start first?')
        if choice:
            self.player_turn = 1
            self.player_mark = 'X'
            self.first = 'player'
        else:
            self.player_turn = 0
            self.player_mark = 'O'
            self.first = 'AI'
        if self.player_turn == 1:
            tk.messagebox.showinfo('First Player', 'Player Goes first')
        else:
            tk.messagebox.showinfo('First Player', 'AI Goes first')

    def place_buttons(self):
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=1, column=2)
        self.button3.grid(row=1, column=3)
        self.button4.grid(row=2, column=1)
        self.button5.grid(row=2, column=2)
        self.button6.grid(row=2, column=3)
        self.button7.grid(row=3, column=1)
        self.button8.grid(row=3, column=2)
        self.button9.grid(row=3, column=3)

    def button_click(self, button_id):
        """This method updates the button that a user clicks
            if the player's turn is X, the selected space becomes blue
            else it becomes red
            the last line of every loop stores the move into a dictionary
        """
        if button_id == 1:
            var = self.turn.get()
            self.button1.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button1.config(bg='light blue')
            else:
                self.button1.config(bg='pink')
            self.store_moves(1)
            self.track_moves.append(1)

        elif button_id == 2:
            var = self.turn.get()
            self.button2.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button2.config(bg='light blue')
            else:
                self.button2.config(bg='pink')
            self.store_moves(2)
            self.track_moves.append(2)

        elif button_id == 3:
            var = self.turn.get()
            self.button3.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button3.config(bg='light blue')
            else:
                self.button3.config(bg='pink')
            self.store_moves(3)
            self.track_moves.append(3)

        elif button_id == 4:
            var = self.turn.get()
            self.button4.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button4.config(bg='light blue')
            else:
                self.button4.config(bg='pink')
            self.store_moves(4)
            self.track_moves.append(4)

        elif button_id == 5:
            var = self.turn.get()
            self.button5.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button5.config(bg='light blue')
            else:
                self.button5.config(bg='pink')
            self.store_moves(5)
            self.track_moves.append(5)

        elif button_id == 6:
            var = self.turn.get()
            self.button6.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button6.config(bg='light blue')
            else:
                self.button6.config(bg='pink')
            self.store_moves(6)
            self.track_moves.append(6)

        elif button_id == 7:
            var = self.turn.get()
            self.button7.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button7.config(bg='light blue')
            else:
                self.button7.config(bg='pink')
            self.store_moves(7)
            self.track_moves.append(7)

        elif button_id == 8:
            var = self.turn.get()
            self.button8.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button8.config(bg='light blue')
            else:
                self.button8.config(bg='pink')
            self.store_moves(8)
            self.track_moves.append(8)

        else:
            var = self.turn.get()
            self.button9.config(text=var, state=tk.DISABLED)
            if var == 'X':
                self.button9.config(bg='light blue')
            else:
                self.button9.config(bg='pink')
            self.store_moves(9)
            self.track_moves.append(9)
        self.moves += 1
        self.possible_moves.pop(self.possible_moves.index(button_id))
        self.turn_update()
        self.win_check()
        draw = self.game_draw()
        if not draw:
            if self.AI_plays() and self.moves != 9:
                delay(10000)
                self.AI_move()
        else:
            self.game_over()

    def play_to(self, loc):
        self.button_click(loc)

    def turn_disp(self):
        player_turn = self.player_turn
        if player_turn == 1:
            self.player = 'Player'
            self.label.config(font=self.my_font, text='Turn for: {} ({})'.format(self.player, self.turn.get()))
        else:
            self.player = 'AI'
            self.label.config(font=self.my_font, text='Turn for: {} ({})'.format(self.player, self.turn.get()))
        self.label.grid(row=0, column=0, padx=20)

    def turn_get(self):
        val = self.turn.get()
        if self.player_turn == 1:
            self.player = 'AI'
            self.player_turn = 0
        else:
            self.player = 'Player'
            self.player_turn = 1
        if val == 'X':
            self.turn.set('O')
        else:
            self.turn.set('X')

    def turn_update(self):
        self.frame.bind('<Button-1>', self.turn_get())
        self.label.config(font=self.my_font, text='Turn for: {} ({})'.format(self.player, self.turn.get()))
        self.label.grid(row=0, column=0, padx=20)

    def store_moves(self, button_id):
        diagonal_a = [1, 5, 9]
        diagonal_b = [3, 5, 7]
        self.var = self.turn.get()
        self.move_dict['button{}'.format(button_id)] = self.var
        if button_id % 3 == 1:
            self.col1.append(self.var)
        elif button_id % 3 == 2:
            self.col2.append(self.var)
        else:
            self.col3.append(self.var)
        if button_id <= 3:
            self.row1.append(self.var)
        elif 3 < button_id <= 6:
            self.row2.append(self.var)
        else:
            self.row3.append(self.var)
        if button_id in diagonal_a:
            self.diagonal_a.append(self.var)
        if button_id in diagonal_b:
            self.diagonal_b.append(self.var)

    def win_check(self):
        for i in range(len(self.row1)):
            try:
                if self.row1[i] != '' and self.row1[i] == self.row1[i + 1] and self.row1[i + 1] == self.row1[i + 2]:
                    self.label.config(text=self.row1[0] + ' Is the Winner!!!')
                    self.winning_row('r1')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.row2)):
            try:
                if self.row2[i] != '' and self.row2[i] == self.row2[i + 1] and self.row2[i + 1] == self.row2[i + 2]:
                    self.label.config(text=self.row2[0] + ' Is the Winner!!!')
                    self.winning_row('r2')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.row3)):
            try:
                if self.row3[i] != '' and self.row3[i] == self.row3[i + 1] and self.row3[i + 1] == self.row3[i + 2]:
                    self.label.config(text=self.row3[0] + ' Is the Winner!!!')
                    self.winning_row('r3')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.col1)):
            try:
                if self.col1[i] != '' and self.col1[i] == self.col1[i + 1] and self.col1[i + 1] == self.col1[i + 2]:
                    self.label.config(text=self.col1[0] + ' Is the Winner!!!')
                    self.winning_row('c1')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.col2)):
            try:
                if self.col2[i] != '' and self.col2[i] == self.col2[i + 1] and self.col2[i + 1] == self.col2[i + 2]:
                    self.label.config(text=self.col2[0] + ' Is the Winner!!!')
                    self.winning_row('c2')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.col3)):
            try:
                if self.col3[i] != '' and self.col3[i] == self.col3[i + 1] and self.col3[i + 1] == self.col3[i + 2]:
                    self.label.config(text=self.col3[0] + ' Is the Winner!!!')
                    self.winning_row('c3')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.diagonal_a)):
            try:
                if self.diagonal_a[i] != '' and self.diagonal_a[i] == self.diagonal_a[i + 1] and self.diagonal_a[
                    i + 1] == self.diagonal_a[i + 2]:
                    self.label.config(text=self.diagonal_a[0] + ' Is the Winner!!!')
                    self.winning_row('d1')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.diagonal_b)):
            try:
                if self.diagonal_b[i] != '' and self.diagonal_b[i] == self.diagonal_b[i + 1] and self.diagonal_b[
                    i + 1] == self.diagonal_b[i + 2]:
                    self.label.config(text=self.diagonal_b[0] + ' Is the Winner!!!')
                    self.winning_row('d2')
                    self.game_over()
            except IndexError:
                pass

    def game_over(self):
        self.button1.config(state=tk.DISABLED)
        self.button2.config(state=tk.DISABLED)
        self.button3.config(state=tk.DISABLED)
        self.button4.config(state=tk.DISABLED)
        self.button5.config(state=tk.DISABLED)
        self.button6.config(state=tk.DISABLED)
        self.button7.config(state=tk.DISABLED)
        self.button8.config(state=tk.DISABLED)
        self.button9.config(state=tk.DISABLED)
        choice = tk.messagebox.askyesno('Game Over', 'Play another?')
        if choice:
            self.parent.destroy()
            new_game()
        else:
            self.parent.destroy()

    def winning_row(self, line):
        if line == 'r1':
            self.button1.config(bg='light green')
            self.button2.config(bg='light green')
            self.button3.config(bg='light green')
        elif line == 'r2':
            self.button4.config(bg='light green')
            self.button5.config(bg='light green')
            self.button6.config(bg='light green')
        elif line == 'r3':
            self.button7.config(bg='light green')
            self.button8.config(bg='light green')
            self.button9.config(bg='light green')
        elif line == 'c1':
            self.button1.config(bg='light green')
            self.button4.config(bg='light green')
            self.button7.config(bg='light green')
        elif line == 'c2':
            self.button2.config(bg='light green')
            self.button5.config(bg='light green')
            self.button8.config(bg='light green')
        elif line == 'c3':
            self.button3.config(bg='light green')
            self.button6.config(bg='light green')
            self.button9.config(bg='light green')
        elif line == 'd1':
            self.button1.config(bg='light green')
            self.button5.config(bg='light green')
            self.button9.config(bg='light green')
        elif line == 'd2':
            self.button3.config(bg='light green')
            self.button5.config(bg='light green')
            self.button7.config(bg='light green')

    def game_draw(self):
        if self.moves == 9:
            self.label.config(text='Draw, No Winner!!')
            return True
        else:
            return False

    def undo_command(self):
        try:
            var = self.track_moves[-1]
            if var == 1:
                self.button1.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button1'] = ''
                del self.row1[-1]
                del self.col1[-1]
                del self.diagonal_a[-1]
                self.turn_update()
            elif var == 2:
                self.button2.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button2'] = ''
                del self.row1[-1]
                del self.col2[-1]
                self.turn_update()
            elif var == 3:
                self.button3.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button3'] = ''
                del self.row1[-1]
                del self.col3[-1]
                del self.diagonal_b[-1]
                self.turn_update()
            elif var == 4:
                self.button4.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button4'] = ''
                del self.row2[-1]
                del self.col1[-1]
                self.turn_update()
            elif var == 5:
                self.button5.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button5'] = ''
                del self.row2[-1]
                del self.col2[-1]
                del self.diagonal_a[-1]
                del self.diagonal_b[-1]
                self.turn_update()
            elif var == 6:
                self.button6.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button6'] = ''
                del self.row2[-1]
                del self.col3[-1]
                self.turn_update()
            elif var == 7:
                self.button7.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button7'] = ''
                del self.row3[-1]
                del self.col1[-1]
                del self.diagonal_b[-1]
                self.turn_update()
            elif var == 8:
                self.button8.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button8'] = ''
                del self.row3[-1]
                del self.col2[-1]
                self.turn_update()
            elif var == 9:
                self.button9.config(state=tk.NORMAL, bg='grey', text='')
                self.move_dict['button9'] = ''
                del self.row3[-1]
                del self.col3[-1]
                del self.diagonal_a[-1]
                self.turn_update()
            self.moves = self.moves - 1
            del self.track_moves[-1]
            self.possible_moves.append(var)
        except IndexError:
            tk.messagebox.showinfo('Invalid', 'No move to undo')


if __name__ == '__main__':
    root = tk.Tk()
    GameWindow(root)
    root.mainloop()
