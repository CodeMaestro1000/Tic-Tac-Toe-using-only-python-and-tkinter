import tkinter as tk
import tkinter.font as font
import tkinter.messagebox


def new_game():
    new_root = tk.Tk()
    GameWindow(new_root)
    new_root.mainloop()


class GameWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('X and O')
        self.parent.geometry('400x520+400+150')
        self.parent.resizable(0, 0)
        self.turn = tk.StringVar()
        self.turn.set('X')
        self.var = ''
        self.my_font = font.Font(family='Helvetica', size=17, weight='bold')
        self.other_font = font.Font(family='Helvetica', size=9, weight='bold')
        self.label = tk.Label(self.parent)
        self.turn_disp()
        self.frame = tk.Frame(self.parent)
        self.frame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=25)
        self.button1 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(1))
        self.button2 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(2))
        self.button3 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(3))
        self.button4 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(4))
        self.button5 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(5))
        self.button6 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(6))
        self.button7 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(7))
        self.button8 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(8))
        self.button9 = tk.Button(self.frame, bg='grey', width=15, height=9, command=lambda: self.button_click(9))
        self.place_buttons()
        self.undo_button = tk.Button(self.frame, text='Undo Last Move', command=self.undo_command)
        self.undo_button.grid(row=5, column=2, pady=3)
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.move_dict = {'button1': '', 'button2': '', 'button3': '', 'button4': '', 'button5': '', 'button6': '',
                          'button7': '', 'button8': '', 'button9': ''}
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.diagonal_a = []
        self.diagonal_b = []
        self.moves = 0
        self.track_moves = []

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
        self.turn_update()
        self.win_check()
        self.game_draw()

    def turn_disp(self):
        self.label.config(font=self.my_font, text='Turn for: {}'.format(self.turn.get()))
        self.label.grid(row=0, column=0, padx=20)

    def turn_get(self):
        val = self.turn.get()
        if val == 'X':
            self.turn.set('O')
        else:
            self.turn.set('X')

    def turn_update(self):
        self.frame.bind('<Button-1>', self.turn_get())
        self.label.config(font=self.my_font, text='Turn for: {}'.format(self.turn.get()))
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
                if self.row1[i] != '' and self.row1[i] == self.row1[i+1] and self.row1[i+1] == self.row1[i+2]:
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
                if self.diagonal_a[i] != '' and self.diagonal_a[i] == self.diagonal_a[i + 1] and self.diagonal_a[i + 1] == self.diagonal_a[i + 2]:
                    self.label.config(text=self.diagonal_a[0] + ' Is the Winner!!!')
                    self.winning_row('d1')
                    self.game_over()
            except IndexError:
                pass

        for i in range(len(self.diagonal_b)):
            try:
                if self.diagonal_b[i] != '' and self.diagonal_b[i] == self.diagonal_b[i + 1] and self.diagonal_b[i + 1] == self.diagonal_b[i + 2]:
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
            self.game_over()
        else:
            pass

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
                del self.diagonal_b[-1]
                self.turn_update()
            self.moves = self.moves - 1
            del self.track_moves[-1]
        except IndexError:
            tk.messagebox.showinfo('Invalid', 'No move to undo')


if __name__ == '__main__':
    root = tk.Tk()
    GameWindow(root)
    root.mainloop()
