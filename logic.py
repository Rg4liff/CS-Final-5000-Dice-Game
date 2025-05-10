from collections import Counter
from gui import *


class Logic(App):
    def __init__(self):
        """
        Initialize variables for logic parts of game.
        Connects gui buttons to new logic functions
        """
        super().__init__()
        self.current_player_score = 0
        self.win_condition = False
        self.current_player_name = ''
        self.player_list = [(self.p1_label, self.p1_score_label), (self.p2_label, self.p2_score_label)]

        self.play_again_button.configure(command=lambda: self.play_game())
        self.r_start_button.configure(command=lambda: self.play_game())
        self.start_button.configure(command=lambda: self.play_game())
        self.roll_again_button.configure(command=lambda: self.roll_again())
        self.stay_button.configure(command=lambda: self.end_turn())
        self.current_dice = []
        self.saved_dice_list = []
        self.validated_dice_list = []
        self.temp_saved = []
        self.winner = ''
    """
    List of needed nodes:
    self.die_one_button, self.die_two_button, self.die_three_button, self.die_four_button, self.die_five_button, self.die_six_button
    self.roll_again_button, self.stay_button
    self.p1_score_label, self.p2_score_label, self.p1_label, self.p2_label,
    self.score_list
    self.play_again_button, self.r_start_button, self.start_button
    
    """
    def play_game(self) -> None:
        """
        Starts the game and does the following:
        1. Resets the game variables
        2. Rolls dice for initial start
        3. Checks if there are any dice that can score or else create Bust
        :return: None
        """
        self.win_condition = False
        self.start_game()
        self.current_score_label.configure(text='0')
        self.p1_score_label.configure(text='0')
        self.p2_score_label.configure(text='0')
        self.current_player_score = 0
        self.current_player_name = self.player_list[0][0]
        self.current_player_score = int(self.player_list[0][1].cget('text'))
        self.player_list[0][0].configure(text_color='red')

        self.roll_dice()
        if self.can_score:
            pass
        else:
            self.bust_params()

    def check_can_score(self, d_num_list) -> bool:
        """
        Checks if there are any dice that can score( 3 of a kind, or a one or five)
        :param d_num_list: list of dice values
        :return: True if there are
        """
        for i in range(6):
            if self.die_button_list[i].cget('state') == 'disabled' and len(d_num_list) > 0:
                d_num_list[i] = 0
            else:
                pass

        counts = Counter(d_num_list)
        for num, count in counts.items():
            if num == 0:
                pass
            # Three of a kind
            elif count >= 3:
                return True
            elif num == 1:
                return True
            elif num == 5:
                return True

        return False

    def roll_dice(self) -> None:
        """
        Calls rand dice function from GUI and validates roll for savable dice
        :return: None
        """
        self.current_dice = self.randomize_dice()
        if self.check_can_score(self.current_dice):
            self.can_score = True
        else:
            self.can_score = False

    def check_win_conditions(self) -> None:
        """
        Checks if either player has reached at least 5000 at end of turn
        :return: None
        """
        p1_score = int(self.p1_score_label.cget('text'))
        p2_score = int(self.p2_score_label.cget('text'))
        self.p1_end_score_label.configure(text=f'Player 1:\n{p1_score}')
        self.p2_end_score_label.configure(text=f'Player 2:\n{p2_score}')
        if p1_score >= 5000:
            self.win_condition = True
            self.winner_label.configure(text='Player 1 Wins!')
            self.end_game()
        elif p2_score >= 5000:
            self.win_condition = True
            self.winner_label.configure(text='Player 2 Wins!')
            self.end_game()

    def enable_all_dice(self) -> None:
        """
        Ensures all dice buttons are re-enabled and colors are reset.
        Resets Dice Clicked bools to false.
        Re-enables roll again button
        :return: None
        """
        for button in self.die_button_list:
            button.configure(state='normal', fg_color='#f7f4ee', bg_color='#f7f4ee')

        # Reset clicked state for all dice by resetting the list of dice clicked
        self.list_of_dice_clicked = [False] * len(self.die_button_list)

        self.roll_again_button.configure(state='normal')

    def validate_selection(self, sdl) -> bool:
        """
        Checks if the dice clicked are scorable die
        :param sdl: List of dice values, and index of each value
        in relation to which dice rolled it
        :return: True if all dice clicked are valid, False otherwise
        """
        counts = Counter(sdl)
        for num, count in counts.items():
            if num not in (1, 5) and count % 3 != 0:
                return False
        return True

    def talley_score(self, sdl) -> int:
        """
        Tallies the score for each validated dice clicked
        :param sdl: List of dice values, and index of each value
        :return: Integer score total
        """
        counts = Counter(sdl)
        score = 0

        # Straight (1 through 6)
        if sorted(sdl) == [1, 2, 3, 4, 5, 6]:
            return 1500

        for num, count in counts.items():
            remainder = count  # make a copy for adjusting below

            # Handle "Three of a Kind"
            if count >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
                remainder -= 3  # subtract only from remainder

            # Handle leftover 1s and 5s
            if num == 1:
                score += remainder * 100
            elif num == 5:
                score += remainder * 50

        return score

    def disable_clicked_dice(self) -> list:
        """
        Disables clicked dice and adds, die index and die value to temp list.
        :return: List if die index, and value
        """
        self.current_label.configure(text='Current Score', text_color='white')
        self.temp_saved = []
        j_v = []

        for die_num in range(len(self.die_button_list)):
            if self.list_of_dice_clicked[die_num] and self.die_button_list[die_num].cget('state') != 'disabled':
                self.temp_saved.append((die_num, self.current_dice[die_num]))
                self.die_button_list[die_num].configure(state='disabled')
        for die_index, die_value in self.temp_saved:
            j_v.append(die_value)
        return j_v

    def bust_params(self) -> None:
        """
        Resets score and notifies player that no valid dice are rolled
        :return: None
        """
        self.roll_again_button.configure(state='disabled')
        self.current_label.configure(text='BUST', text_color='red')
        for button in self.die_button_list:
            button.configure(state='disabled')
        self.current_player_score = 0
        self.current_score_label.configure(text='0')
        self.can_score = True

    def roll_again(self) -> None:
        """
        Sets up Roll again button to go through 1 turn:
        1. disables clicked die
        2. Checks if any dice are clicked to not allow for reroll cheating
        3. validates dice, if not resets roll to previous state and undos only clicked dice for that roll.
        4. if valid: calls talley and adds dice to list of valid rolls.
        5. checks if all 6 were valid and clicked, resets dice for new roll
        6. rolls again and check for bust params
        :return: None
        """
        just_values = self.disable_clicked_dice()

        if not just_values and self.can_score:
            self.current_label.configure(text='You must select a die!', text_color='red')
            return

        elif not self.validate_selection(just_values):
            self.current_label.configure(text='Invalid selection, choose again', text_color='red')
            for die_num, _ in self.temp_saved:
                self.die_button_list[die_num].configure(state='normal', fg_color='#f7f4ee', bg_color='#f7f4ee')
                self.list_of_dice_clicked[die_num] = False
            print('list of dice clicked: invalid: ', self.list_of_dice_clicked)
            return

        # Valid selection
        self.saved_dice_list.extend(just_values)
        self.validated_dice_list.extend(just_values)

        new_score = self.talley_score(just_values)
        self.current_player_score += new_score
        self.current_score_label.configure(text=self.current_player_score)

        all_disabled = all(button.cget('state') == 'disabled' for button in self.die_button_list)
        if all_disabled:
            self.enable_all_dice()

        self.roll_dice()

        if not self.can_score:
            self.bust_params()

    def end_turn(self) -> None:
        """
        Sets up Roll again button to go through 1 turn:
        1. disables clicked die
        2. Checks if any dice are clicked to not allow for reroll cheating
        3. validates dice, if not resets roll to previous state and undos only clicked dice for that roll.
        4. if valid: calls talley and adds dice to list of valid rolls.
        5. checks if all 6 were valid and clicked, resets dice for new roll
        6. Sets score for current player and switches to new player
        6. rolls again and check for bust params
        :return: None
        :return:
        """
        just_values = self.disable_clicked_dice()

        if just_values:
            if not self.validate_selection(just_values):
                self.current_label.configure(text='Invalid selection, choose again', text_color='red')
                for die_num, _ in self.temp_saved:
                    self.die_button_list[die_num].configure(state='normal', fg_color='#f7f4ee', bg_color='#f7f4ee')
                    self.list_of_dice_clicked[die_num] = False
                return

            self.saved_dice_list.extend(just_values)
            self.validated_dice_list.extend(just_values)
            new_score = self.talley_score(just_values)
            self.current_player_score += new_score
            self.current_score_label.configure(text=self.current_player_score)

        if self.current_player_name == self.player_list[0][0]:
            self.current_player_score += int(self.player_list[0][1].cget('text'))
            self.player_list[0][1].configure(text=str(self.current_player_score))
            self.current_player_name = self.player_list[1][0]
            self.player_list[1][0].configure(text_color='red')
            self.player_list[0][0].configure(text_color='black')
        else:
            self.current_player_score += int(self.player_list[1][1].cget('text'))
            self.player_list[1][1].configure(text=str(self.current_player_score))
            self.current_player_name = self.player_list[0][0]
            self.player_list[0][0].configure(text_color='red')
            self.player_list[1][0].configure(text_color='black')

        self.current_player_score = 0
        self.current_score_label.configure(text='0')
        self.validated_dice_list.clear()
        self.saved_dice_list.clear()
        self.temp_saved.clear()
        self.enable_all_dice()
        self.roll_dice()
        self.check_win_conditions()

        if not self.can_score:
            self.bust_params()
