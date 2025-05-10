import random
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image


class App(ctk.CTk):

    def __init__(self):

        super().__init__()
        # Define clicked holder
        self.die_one_is_clicked = False
        self.die_two_is_clicked = False
        self.die_three_is_clicked = False
        self.die_four_is_clicked = False
        self.die_five_is_clicked = False
        self.die_six_is_clicked = False
        self.is_staying = False
        self.is_rolling = False
        self.can_score = True

        # Define dice images
        self.die_one_image = CTkImage(Image.open("Dice_pngs/Die_one.png"), size=(80, 80))
        self.die_two_image = CTkImage(Image.open("Dice_pngs/Die_two.png"), size=(80, 80))
        self.die_three_image = CTkImage(Image.open("Dice_pngs/Die_three.png"), size=(80, 80))
        self.die_four_image = CTkImage(Image.open("Dice_pngs/Die_four.png"), size=(80, 80))
        self.die_five_image = CTkImage(Image.open("Dice_pngs/Die_five.png"), size=(80, 80))
        self.die_six_image = CTkImage(Image.open("Dice_pngs/Die_six.png"), size=(80, 80))

        # Define fonts and text
        self.title_font = ctk.CTkFont(family='Times New Roman', size=100, weight='bold')
        self.rules_font = ctk.CTkFont(family='Georgia', size=15, weight='bold')
        self.scoring_font = ctk.CTkFont(family='Georgia', size=15, weight='bold')
        self.score_font = ctk.CTkFont(family='Georgia', size=20, weight='bold')
        self.button_font = ctk.CTkFont(family='Georgia', size=20, weight='bold')

        self.list_of_dice_clicked = [self.die_one_is_clicked, self.die_two_is_clicked, self.die_three_is_clicked, self.die_four_is_clicked, self.die_five_is_clicked, self.die_six_is_clicked]
        self.score_list = []

        with open('scoring.txt', 'r') as f:
            scoring_text = f.read()
        with open('rules.txt', 'r') as f:
            rules_text = f.read()

        self.title = "5000 Dice Game"
        self.resizable(False, False)
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Screens Setup
        self.splash_frame = ctk.CTkFrame(self, fg_color='#b68f20')
        self.how_to_play_frame = ctk.CTkFrame(self, fg_color='#b68f20')
        self.main_game_frame = ctk.CTkFrame(self, fg_color='#b68f20')
        self.end_game_frame = ctk.CTkFrame(self, fg_color='#b68f20')

        self.how_to_play_frame.grid_columnconfigure(0, weight=1)
        self.how_to_play_frame.grid_columnconfigure(1, weight=1)
        self.how_to_play_frame.grid_columnconfigure(2, weight=1)

        self.how_to_play_frame.grid_rowconfigure(0, weight=1)
        self.how_to_play_frame.grid_rowconfigure(1, weight=1)
        self.how_to_play_frame.grid_rowconfigure(2, weight=1)

        self.splash_frame.grid_rowconfigure(0, weight=1)
        self.splash_frame.grid_rowconfigure(1, weight=1)
        self.splash_frame.grid_rowconfigure(2, weight=1)
        self.splash_frame.grid_rowconfigure(3, weight=1)
        self.splash_frame.grid_rowconfigure(4, weight=1)

        self.splash_frame.grid_columnconfigure(0, weight=1)
        self.splash_frame.grid_columnconfigure(1, weight=1)
        self.splash_frame.grid_columnconfigure(2, weight=1)
        self.splash_frame.grid_columnconfigure(3, weight=1)
        self.splash_frame.grid_columnconfigure(4, weight=1)
        self.splash_frame.grid_columnconfigure(5, weight=1)

        self.main_game_frame.grid_rowconfigure(0, weight=1)
        self.main_game_frame.grid_rowconfigure(1, weight=1)
        self.main_game_frame.grid_rowconfigure(2, weight=1)
        self.main_game_frame.grid_rowconfigure(3, weight=1)
        self.main_game_frame.grid_rowconfigure(4, weight=1)
        self.main_game_frame.grid_rowconfigure(5, weight=1)
        self.main_game_frame.grid_columnconfigure(0, weight=1)
        self.main_game_frame.grid_columnconfigure(1, weight=1)
        self.main_game_frame.grid_columnconfigure(2, weight=1)
        self.main_game_frame.grid_columnconfigure(3, weight=1)
        self.main_game_frame.grid_columnconfigure(4, weight=1)
        self.main_game_frame.grid_columnconfigure(5, weight=1)
        self.main_game_frame.grid_columnconfigure(6, weight=1)
        self.main_game_frame.grid_columnconfigure(7, weight=1)
        self.main_game_frame.grid_columnconfigure(8, weight=1)

        self.end_game_frame.grid_rowconfigure(0, weight=1)
        self.end_game_frame.grid_rowconfigure(1, weight=1)
        self.end_game_frame.grid_rowconfigure(2, weight=1)
        self.end_game_frame.grid_rowconfigure(3, weight=1)
        self.end_game_frame.grid_rowconfigure(4, weight=1)
        self.end_game_frame.grid_columnconfigure(0, weight=1)
        self.end_game_frame.grid_columnconfigure(1, weight=1)
        self.end_game_frame.grid_columnconfigure(2, weight=1)
        self.end_game_frame.grid_columnconfigure(3, weight=1)
        self.end_game_frame.grid_columnconfigure(4, weight=1)

        self.splash_frame.grid(sticky='nsew')

        # Splash nodes
        self.s_game_title_label = ctk.CTkLabel(self.splash_frame, text='5000 Dice Game',
                                               font=self.title_font)  # text_color to change color
        self.author_label = ctk.CTkLabel(self.splash_frame, text='By Roxanne Girol', font=self.rules_font)
        self.start_button = ctk.CTkButton(self.splash_frame, font=self.button_font, width=40, height=35, text='Start',
                                          text_color='black', command=lambda: self.start_game(), fg_color='#f7f4ee',
                                          hover_color='#c5bca9')
        self.rules_button = ctk.CTkButton(self.splash_frame, font=self.button_font, width=40, height=35, text='Rules',
                                          text_color='black', command=lambda: self.show_rules(), fg_color='#f7f4ee',
                                          hover_color='#c5bca9')
        self.s_quit_button = ctk.CTkButton(self.splash_frame, font=self.button_font, width=40, height=35, text='Quit',
                                           text_color='black', command=quit, fg_color='#f7f4ee', hover_color='#c5bca9')
        self.s_game_title_label.grid(row=1, column=1, columnspan=4)
        self.author_label.grid(row=2, column=1, columnspan=4)
        self.start_button.grid(row=4, column=2, sticky='w')
        self.rules_button.grid(row=4, column=3, sticky='w')
        self.s_quit_button.grid(row=4, column=4, sticky='w')

        # rules nodes
        self.scrollable_frame = ctk.CTkScrollableFrame(self.how_to_play_frame, width=800, height=600)
        self.scrollable_frame.grid_columnconfigure(3, weight=1)
        self.scrollable_frame.grid_rowconfigure(3, weight=1)
        self.rules_label = ctk.CTkLabel(self.scrollable_frame, font=self.rules_font, text=rules_text)
        self.r_main_menu_button = ctk.CTkButton(self.scrollable_frame, font=self.button_font, width=40, height=35,
                                                text='Main Menu',
                                                # TO FIX: add button func and set correct location on frame
                                                text_color='black', command=lambda: self.main_menu(),
                                                fg_color='#f7f4ee', hover_color='#c5bca9')
        self.r_start_button = ctk.CTkButton(self.scrollable_frame, font=self.button_font, width=40, height=35, text='Start',
                                            text_color='black', command=lambda: self.start_game(), fg_color='#f7f4ee',
                                            hover_color='#c5bca9')
        self.r_start_button.grid(row=3, column=2)
        self.r_main_menu_button.grid(row=3, column=0)
        self.scrollable_frame.grid(sticky='nsew')
        self.rules_label.grid(row=0, column=0, columnspan=3)

        # Main game nodes
        self.mg_game_title_label = ctk.CTkLabel(self.main_game_frame, text='5000 Dice Game', font=self.rules_font)
        self.scoring_guide_label = ctk.CTkLabel(self.main_game_frame, font=self.scoring_font, text=scoring_text,
                                                justify='left')
        self.p1_label = ctk.CTkLabel(self.main_game_frame, text_color='black', font=self.score_font, text='Player 1:')
        self.p2_label = ctk.CTkLabel(self.main_game_frame, text_color='black', font=self.score_font, text='Player 2:')
        self.p1_score_label = ctk.CTkLabel(self.main_game_frame, font=self.score_font, text='0')
        self.p2_score_label = ctk.CTkLabel(self.main_game_frame, font=self.score_font, text='0')
        self.current_label = ctk.CTkLabel(self.main_game_frame, font=self.score_font, text='Current Score:')
        self.current_score_label = ctk.CTkLabel(self.main_game_frame, font=self.score_font, text='0')
        self.roll_again_button = ctk.CTkButton(self.main_game_frame, font=self.button_font, text='Roll Again',
                                               text_color='black', fg_color='#f7f4ee', hover_color='#c5bca9')
        self.stay_button = ctk.CTkButton(self.main_game_frame, font=self.button_font, text='Stay', text_color='black',
                                         fg_color='#f7f4ee', hover_color='#c5bca9')
        self.mg_game_title_label.grid(row=0, column=2, columnspan=6)
        self.p1_label.grid(row=0, column=1, sticky='s')
        self.p2_label.grid(row=0, column=8, sticky='s')
        self.p1_score_label.grid(row=1, column=1, sticky='n')
        self.p2_score_label.grid(row=1, column=8, sticky='n')
        self.roll_again_button.grid(row=4, column=8, sticky='s')
        self.stay_button.grid(row=5, column=8)
        self.scoring_guide_label.grid(row=1, column=2, columnspan=5)
        self.current_label.grid(row=2, column=2, columnspan=5, sticky ='s')
        self.current_score_label.grid(row=3, column=2, columnspan=5, sticky='n')

        # Dice
        self.die_one_button = ctk.CTkButton(self.main_game_frame, image=self.die_one_image, width=80, height=80, text="",
                                            fg_color='#f7f4ee', hover_color='#f7f4ee', command=lambda: self.is_die_clicked(1))
        self.die_two_button = ctk.CTkButton(self.main_game_frame, image=self.die_two_image, width=80, height=80, text="",
                                            fg_color='#f7f4ee', hover_color='#f7f4ee', command=lambda: self.is_die_clicked(2))
        self.die_three_button = ctk.CTkButton(self.main_game_frame, image=self.die_three_image, width=80, height=80, text="",
                                              fg_color='#f7f4ee', hover_color='#f7f4ee', command=lambda: self.is_die_clicked(3))
        self.die_four_button = ctk.CTkButton(self.main_game_frame, image=self.die_four_image, width=80, height=80, text="",
                                             fg_color='#f7f4ee', hover_color='#f7f4ee', command=lambda: self.is_die_clicked(4))
        self.die_five_button = ctk.CTkButton(self.main_game_frame, image=self.die_five_image, width=80, height=80, text="",
                                             fg_color='#f7f4ee', hover_color='#f7f4ee', command=lambda: self.is_die_clicked(5))
        self.die_six_button = ctk.CTkButton(self.main_game_frame, image=self.die_six_image, width=80, height=80, text="",
                                            fg_color='#f7f4ee', hover_color='#f7f4ee', command=lambda: self.is_die_clicked(6))
        self.die_button_list = [self.die_one_button, self.die_two_button, self.die_three_button, self.die_four_button, self.die_five_button, self.die_six_button]

        self.die_one_button.grid(row=4, column=1, rowspan=2)
        self.die_two_button.grid(row=4, column=2, rowspan=2)
        self.die_three_button.grid(row=4, column=3, rowspan=2)
        self.die_four_button.grid(row=4, column=4, rowspan=2)
        self.die_five_button.grid(row=4, column=5, rowspan=2)
        self.die_six_button.grid(row=4, column=6, rowspan=2)

        # End game Screen
        self.p1_end_score_label = ctk.CTkLabel(self.end_game_frame, font=self.score_font, text='Player 1: 0')
        self.p2_end_score_label = ctk.CTkLabel(self.end_game_frame, font=self.score_font, text='Player 2: 0')
        self.winner_label = ctk.CTkLabel(self.end_game_frame, font=self.title_font, text='')

        self.play_again_button = ctk.CTkButton(self.end_game_frame, font=self.button_font, text='Play Again', text_color='black',
                                         fg_color='#f7f4ee', hover_color='#c5bca9', command=lambda: self.start_game())
        self.end_quit_button = ctk.CTkButton(self.end_game_frame, font=self.button_font, text='Quit', text_color='black',
                                         fg_color='#f7f4ee', hover_color='#c5bca9', command=quit)
        self.p1_end_score_label.grid(row=0, column=3)
        self.p2_end_score_label.grid(row=1, column=3, sticky='n')
        self.winner_label.grid(row=0, column=1, sticky='s')
        self.play_again_button.grid(row=2, column=3, sticky='s')
        self.end_quit_button.grid(row=3, column=3)

    def is_die_clicked(self, die_num):
        index = die_num - 1
        self.list_of_dice_clicked[index] = not self.list_of_dice_clicked[index]

        if self.list_of_dice_clicked[index]:
            self.die_button_list[index].configure(fg_color='#c5bca9', hover_color='#c5bca9')
        else:
            self.die_button_list[index].configure(fg_color='#f7f4ee', hover_color='#f7f4ee')

    def randomize_dice(self) -> list:
        die_num_list = []

        for i in range(6):

            die = random.randint(1, 6)
            die_num_list.append(die)
            if self.die_button_list[i].cget('state') != 'disabled':
                match die:
                    case 1:
                        self.die_button_list[i].configure(image=self.die_one_image)
                    case 2:
                        self.die_button_list[i].configure(image=self.die_two_image)
                    case 3:
                        self.die_button_list[i].configure(image=self.die_three_image)
                    case 4:
                        self.die_button_list[i].configure(image=self.die_four_image)
                    case 5:
                        self.die_button_list[i].configure(image=self.die_five_image)
                    case 6:
                        self.die_button_list[i].configure(image=self.die_six_image)

        return die_num_list

    def end_game(self):
        self.main_game_frame.grid_forget()
        self.end_game_frame.grid(sticky='nsew')

    def main_menu(self):
        self.how_to_play_frame.grid_forget()
        self.splash_frame.grid(sticky='nsew')

    def show_rules(self):
        self.splash_frame.grid_forget()
        self.how_to_play_frame.grid(sticky='nsew')

    def start_game(self):
        self.end_game_frame.grid_forget()
        self.how_to_play_frame.grid_forget()
        self.splash_frame.grid_forget()
        self.main_game_frame.grid(sticky='nsew')


if __name__ == '__main__':
    app = App()
    app.mainloop()
