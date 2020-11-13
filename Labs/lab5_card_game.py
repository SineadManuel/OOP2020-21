# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle


class CardGame():

    # initialises the application
    def __init__(self):
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score
        self.the_cards = self.load_cards()
        #self.card_split = []
        self.player_score = 0
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        self.score_frame = LabelFrame(master=master_frame)
        self.score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file = self.pick_card())  # possibily add random card here
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        closed_deck = Button(cards_frame, command=self.pick_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!") #command=self.done_playing
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game) #command=self.reset_game
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        # self.score_label = Label(self.score_frame, text="Your score: " + str(self.player_score))
        # self.score_label.update_idletasks()
        # self.score_label.pack()

        root.mainloop()

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue
    def load_cards(self):
        cards = Queue(maxsize=52) #change this if you want to use a different data structure
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        card_deck = []
        card_dict = {}

        # populating list with the name of each card
        for suit in suits:
            for number in numbers:
                card_deck.append(number + "_" + suit)
            for person in people:
                card_deck.append(person + "_" + suit)

        # populating a dictionary using card_deck to give each card a value
        # i = 1
        # for card in card_deck:
        #     if 'jack' in card:
        #         card_dict[card] = 10
        #     elif 'queen' in card:
        #         card_dict[card] = 10
        #     elif 'king' in card:
        #         card_dict[card] = 10
        #         i = 1
        #     else:
        #         card_dict[card] = i
        #         i += 1

        # prints list
        print("List")
        print(card_deck)
        # prints dictionary
        # print("Dictionary")
        # print(card_dict)

        # count = 1
        # for card in card_dict:
        #     if card_dict[card] == count:
        #         self.player_score = count
        #         print(self.player_score)
        #     count += 1

        shuffle(card_deck)
        print("List - shuffled")
        print(card_deck)

        # Populates queue with elements from card_deck
        for i in range(0, 52):
            cards.put(card_deck[i])

        #self.check_scores(card_dict, cards)
        # TESTS:
        # Prints list
        #print(card_deck)
        # Prints length of list
        #print(len(card_deck))
        # Prints size of queue
        #print(cards.qsize())
        # Checks if queue is full or not
        if cards.full():
            print("\nIs the queue full: ", cards.full())
        else:
            print("\nIs the queue empty: ", cards.empty())

        #self.check_scores()

        # Spliting list
        # print("\nList - splited")
        # for card in self.card_deck:
        #     print(card.split("_"))
        # print("List - splited")
        # # for card in card_deck:
        # #     # card_deck.append(number + "_" + suit)
        # #     self.card_split.append(card)
        # #     print(self.card_split)
        #
        # print("list?")
        # print(self.card_split)

        self.check_scores()

        return cards

    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):
        # open_card is changed when closed_deck button is clicked
        new_card = self.the_cards.get()
        card_file = 'cards/' + new_card + '.gif'
        the_card = PhotoImage(file = card_file)
        self.open_card.config(image = the_card)
        self.open_card.photo = the_card

        # trying to load the value of the current card on the screen when the game is loaded
        if str(new_card.split('_')[0]) == 'queen':
            self.player_score = int(self.player_score + 10)
            print(self.player_score)
        elif str(new_card.split('_')[0]) == 'jack':
            self.player_score = int(self.player_score + 10)
            print(self.player_score)
        elif str(new_card.split('_')[0]) == 'king':
            self.player_score = int(self.player_score + 10)
            print(self.player_score)
        else:
            self.player_score = self.player_score + int(new_card.split('_')[0])
            print(self.player_score)

        self.score_label = Label(self.score_frame, text="Your score: " + str(self.player_score))
        self.score_label.update_idletasks()
        self.score_label.pack()

        #self.score_label.config(text="Your score: " + str(self.player_score))

        self.check_scores()

        return card_file

    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):

         #
         # for i in range(1, 11):
         #     if new_given_card == self.the_cards:
         #         self.player_score = self.player_score + i

        pass  # replace this line by your code

    # calculates the new score
    # takes a card argument of type
    def update_score(self, card):
        pass  # replace this line by your code

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        pass  # replace this line by your code

    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck
    def reset_game(self):
        self.player_score = 0
        self.the_cards = self.load_cards()
        the_card = PhotoImage(file=self.pick_card())


# object creation here:

app = CardGame()
