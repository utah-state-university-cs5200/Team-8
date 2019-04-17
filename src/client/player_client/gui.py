from tkinter import *


class LobbyWindow:

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

    def run(self):

        self.top = Tk()
        self.top.title("Contact")
        self.top.geometry("640x400")

        self.username()
        self.lobby_interface()
        self.update_listbox()

        self.top.mainloop()

    def username(self):
        """Enter username elements"""

        self.title_frame = Frame(self.top)
        self.title_label = Label(self.title_frame, text="Contact")
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

    def lobby_interface(self):
        """initialize the lobby elements"""

        self.create_game_button = Button(self.top, text="Create Game", command=self.create_game_init)
        self.create_game_button.pack()

        self.lobby_listbox = Listbox(self.top, selectmode=SINGLE, width=100)
        self.lobby_listbox.pack()
        self.lobby_listbox.bind('<<ListboxSelect>>', self.game_select)



        self.player_count_label_var = StringVar()
        self.player_count_label_var.set("Players: ")
        self.join_frame = Frame(self.top)
        self.player_count_label = Label(self.join_frame, textvariable=self.player_count_label_var)
        self.join_game_button = Button(self.join_frame, text="Join Game", command=self.join_game)
        self.player_count_label.pack()
        self.join_game_button.pack()
        self.join_frame.pack()


    def creation_interface(self):
        """initialize the elements for game creation"""
        pass

    def update_listbox(self):
        count = 1
        self.lobby_listbox.delete(0, END)
        for key in self.listbox_options.keys():
            self.lobby_listbox.insert(count, key)
            count += 1


    def username_change(self):
        self.username_entry.get()
        # TODO: update username in client code

    def join_game(self):
        game_name = self.lobby_listbox.get(self.lobby_listbox.curselection()[0])
        game = self.listbox_options[game_name]
        # TODO: call function to join game with game_id


    def create_game_init(self):
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

        self.create_game_frame.pack_forget()
        self.join_frame.pack()
        pass

    def game_select(self, e):
        game_name = self.lobby_listbox.get(self.lobby_listbox.curselection()[0])
        game = self.listbox_options[game_name]

        self.player_count_label_var.set(f"Players: {game['player_count']}/{game['max_players']}")

test = LobbyWindow()
test.run()
