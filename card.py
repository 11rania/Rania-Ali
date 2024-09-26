import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(rank, rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
            return card
        return None

    def play_card(self, index):
        return self.hand.pop(index)

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.deck = Deck()
        self.deck.shuffle()

    def deal_cards(self):
        for _ in range(13):
            for player in self.players:
                player.draw(self.deck)

    def play_round(self):
       pass
    def play_game(self):
        self.deal_cards()
        while True:
            self.play_round()
            # تحقق من شروط انتهاء اللعبة (مثلاً: عندما ينفد الدك)

# مثال على كيفية استخدام الكلاسات
game = Game(2)  # لعبة بين لاعبين
game.play_game()
