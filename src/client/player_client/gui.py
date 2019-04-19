from tkinter import *


class LobbyWindow:
    """This class handles all UI elements for the lobby"""

    def __init__(self):
        self.listbox_options = {
            'My Game': {
                'game_id': 43,
                'player_count': 3,
                'max_players': 10,
            },
            'Another Game': {
                'game_id': 23,
                'player_count': 7,
                'max_players': 8
            },
        }
        self.top = Tk()
        self.top.title("Contact Lobby")
        self.top.geometry("640x400")
        self._init_username()
        self._init_lobby_interface()


    def run(self):

        self.update_listbox()
        self.top.mainloop()

    def _init_username(self):
        """Enter username elements"""

        self.title_frame = Frame(self.top)
        self.title_label = Label(self.title_frame, text="Contact Lobby", font=('Helvetica', '24'))
        self.title_label.pack()
        self.title_frame.pack()

        self.username_frame = Frame(self.top)
        self.username_label = Label(self.username_frame, text="Username: ")
        self.username_entry = Entry(self.username_frame)
        self.username_button = Button(self.username_frame, text="Update", command=self.username_change)
        self.username_label.pack(side=LEFT)
        self.username_entry.pack(side=LEFT)
        self.username_button.pack(side=LEFT)
        self.username_frame.pack(side=TOP)

    def _init_lobby_interface(self):
        """initialize the lobby elements"""


        self.create_game_button = Button(self.top, text="Create Game", command=self._init_create_game)
        self.create_game_button.pack()

        self.list_frame = Frame(self.top)
        self.list_scrollbar = Scrollbar(self.list_frame)
        self.list_scrollbar.pack(side=RIGHT, fill=Y)
        self.lobby_listbox = Listbox(self.list_frame, selectmode=SINGLE, width=100, yscrollcommand=self.list_scrollbar.set)
        self.lobby_listbox.pack()

        self.lobby_listbox.bind('<<ListboxSelect>>', self.game_select)
        self.list_scrollbar.config(command=self.lobby_listbox.yview)

        self.list_frame.pack()

        self.player_count_label_var = StringVar()
        self.player_count_label_var.set("Players: ")
        self.join_frame = Frame(self.top)
        self.player_count_label = Label(self.join_frame, textvariable=self.player_count_label_var)
        self.join_game_button = Button(self.join_frame, text="Join Game", command=self.join_game)
        self.player_count_label.pack()
        self.join_game_button.pack()
        self.join_frame.pack()

    def update_listbox(self):
        """Update the game list"""
        count = 1
        self.lobby_listbox.delete(0, END)
        for key in self.listbox_options.keys():
            self.lobby_listbox.insert(count, key)
            count += 1


    def username_change(self):
        """Update the username"""
        self.username_entry.get()
        # TODO: update username in client code



    def _init_create_game(self):
        """Swap out widgets for game creation widgets"""
        # TODO if the button is clicked multiple times it will keep adding things below, need to check if still there
        self.join_frame.pack_forget()
        self.create_game_frame = Frame(self.top)
        self.new_game_name_label = Label(self.create_game_frame, text="Game Name: ")
        self.new_game_name_entry = Entry(self.create_game_frame)
        self.new_game_players_label = Label(self.create_game_frame, text="Max Players: ")
        self.new_game_players_entry = Entry(self.create_game_frame)
        self.new_game_submit_button = Button(self.create_game_frame, text="Create Game", command=self.create_game)
        self.new_game_cancel_button = Button(self.create_game_frame, text="Cancel", command=self.cancel_creation)

        self.new_game_name_label.pack()
        self.new_game_name_entry.pack()
        self.new_game_players_label.pack()
        self.new_game_players_entry.pack()
        self.new_game_submit_button.pack()
        self.new_game_cancel_button.pack()

        self.create_game_frame.pack()


    def create_game(self):
        """When Create Game button is pressed this is executed"""
        name = self.new_game_name_entry.get()
        max = self.new_game_players_entry.get()
        # TODO generate game_id or create the game server and have it return the game_id here
        self.listbox_options[name] = {
            'game_id': 22,
            'player_count': 0,
            'max_players': int(max)

        }
        self.create_game_frame.pack_forget()
        self.join_frame.pack()
        self.update_listbox()

    def cancel_creation(self):
        """Cancels game creation"""
        self.create_game_frame.pack_forget()
        self.join_frame.pack()

    def game_select(self, e):
        game_name = self.lobby_listbox.get(self.lobby_listbox.curselection()[0])
        game = self.listbox_options[game_name]

        self.player_count_label_var.set(f"Players: {game['player_count']}/{game['max_players']}")

    def join_game(self):
        game_name = self.lobby_listbox.get(self.lobby_listbox.curselection()[0])
        game = self.listbox_options[game_name]
        # TODO: call function to join game with game_id
        self.top.destroy()
        game_object = GamePlayWindow()
        game_object.run()


class GamePlayWindow:

    def __init__(self):
        self.top = Tk()
        self.top.title("Contact")
        self.top.geometry("640x400")
        self._init_player_ui()
        self.game_data = {
            'game_name': 'Default Game',
            'secret_word': "",
            'secret_word_pos': 1,
            'hints': []}

    def _init_player_ui(self):
        self.title_frame = Frame(self.top)
        self.title_label = Label(self.title_frame, text="Contact Game", font=('Helvetica', '24'))
        self.title_label.pack()
        self.title_frame.pack()

        self.secret_keeper_frame = Frame(self.top)
        self.secret_word_label = Label(self.secret_keeper_frame, text="Enter Secret Word: ")
        self.secret_word_entry = Entry(self.secret_keeper_frame)
        self.secret_word_submit = Button(self.secret_keeper_frame, text="Submit", command=self.submit_secret_word)
        self.secret_word_label.pack(side=LEFT)
        self.secret_word_entry.pack(side=LEFT)
        self.secret_word_submit.pack(side=RIGHT)
        self.secret_keeper_frame.pack()

        self.current_word_display_frame = Frame(self.top)
        self.current_word_label = Label(self.current_word_display_frame, text="Word: ", font=('Helvetica', '18'))
        self.current_word_var = StringVar()
        self.current_word_display = Label(self.current_word_display_frame, textvariable=self.current_word_var, font=('Helvetica', '18'))
        self.current_word_label.pack(side=LEFT)
        self.current_word_display.pack(side=LEFT)
        self.current_word_display_frame.pack()

        self.hint_large_frame = Frame(self.top)

        self.hint_display_frame = Frame(self.hint_large_frame)
        self.hint_display_label = Label(self.hint_display_frame, text="Current Hint Phrases")
        self.hint_listbox = Listbox(self.hint_display_frame, selectmode=SINGLE)
        self.hint_listbox.bind('<<ListboxSelect>>', self.hint_select)
        self.hint_display_label.pack()
        self.hint_listbox.pack()
        self.hint_display_frame.grid(row=0, column=0)

        self.hint_full_frame = Frame(self.hint_large_frame)
        self.hint_full_var = StringVar()
        self.hint_full_label = Label(self.hint_full_frame, textvariable=self.hint_full_var)
        self.hint_contact_button = Button(self.hint_full_frame, text="Contact", command=self.make_contact)
        self.hint_full_label.pack()

        self.new_hint_button = Button(self.hint_full_frame, text="New Hint", command=self.show_new_hint)
        self.new_hint_button.pack()

        self.hint_full_frame.grid(row=0, column=2)

        self.hint_large_frame.pack()

    def submit_secret_word(self):
        self.game_data['secret_word'] = self.secret_word_entry.get()
        self.update_current_word()

    def update_current_word(self):
        self.current_word_var.set(self.game_data['secret_word'][:self.game_data['secret_word_pos']])

    def update_hint_listbox(self):
        self.hint_listbox.delete(0, END)
        count = 1
        for hint in self.game_data['hints']:
            self.hint_listbox.insert(count, hint)
            count += 1

    def move_hidden_letter(self):
        if self.game_data['secret_word_pos'] <= len(self.game_data['secret_word']):
            self.game_data['secret_word_pos'] += 1
            self.update_current_word()
        # TODO: else the word is already fully shown, so we need to start game on new word

    def hint_select(self, e):
        hint = self.hint_listbox.get(self.hint_listbox.curselection()[0])
        self.hint_full_var.set(hint)
        self.new_hint_button.pack_forget()
        self.hint_contact_button.pack()
        self.hint_full_frame.grid(row=0, column=2)

    def make_contact(self):

        self.contact_guess_label = Label(self.hint_full_frame, text="Guess: ")
        self.contact_guess_submit = Button(self.hint_full_frame, text="Submit", command=self.submit_contact)
        self.hint_contact_button.pack_forget()
        self.hint_full_label.pack_forget()


        self.new_hint_button.pack()


    def submit_contact(self):

        pass

    def show_new_hint(self):
        self.new_hint_button.pack_forget()
        self.hint_contact_button.pack_forget()
        self.new_hint_entry = Entry(self.hint_full_frame)
        self.new_hint_submit = Button(self.hint_full_frame, text="Submit Hint", command=self.submit_new_hint)
        self.new_hint_entry.pack()
        self.new_hint_submit.pack()


    def submit_new_hint(self):
        self.new_hint_entry.pack_forget()
        self.new_hint_submit.pack_forget()
        self.game_data['hints'].append(self.new_hint_entry.get())

        self.new_hint_button.pack()
        self.hint_full_frame.grid(row=0, column=2)

        self.update_hint_listbox()

    def run(self):

        self.top.mainloop()


test = LobbyWindow()
test.run()
