"""

Juego de cartas simple "Guerra"
El juego termina cuando se han repartido todas las cartas del reparto inicial; no continúa
hasta que un "jugador" haya ganado todas las cartas como algunas versiones del juego.
Si la última mano es "guerra" (y ninguno de los "jugadores" tiene suficientes cartas para jugar la guerra) entonces
la mano se considera un empate.
"""

import random

suits = "corazones espadas tréboles diamantes".split()

rankings = "2 3 4 5 6 7 8 9 10 J Q K A".split()

SUIT_SYMBOLS = {
    'espadas': u'♠',
    'diamantes': u'♦',
    'tréboles': u'♣',
    'corazones': u'♥',
}


class Card:

    def __init__(self, suit, ranking):
        self.suit = suit
        self.ranking = ranking

    def __repr__(self):
        str = SUIT_SYMBOLS[self.suit] + self.ranking
        return(str)


class Deck:

    def __init__(self):
        self.deck = []
        for i in suits:
            for j in rankings:
                self.deck.append(Card(i, j))
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

    def __getitem__(self, position):
        return self.deck[position]

    def deal(self, num_cards):
        """
        Distribuye num_cards número de cartas y las elimina del mazo y
         devuelve una lista
        """
        return [self.deck.pop() for i in range(num_cards)]


class Player:

    def __init__(self):
        self.hand = []

    def __len__(self):
        return len(self.hand)

    def __iter__(self):
        return iter(self.hand)

    def __getitem__(self, position):
        return self.hand[position]

    def flip_card(self, num_cards):
        return [self.hand.pop() for i in range(num_cards)]


def initial_deal(deck, player1, player2):

    '''
        Reparte las 52 cartas a dos jugadores. Se supone que el jugador 1 es el crupier.
        Primero, el jugador 2 obtiene todas las demás cartas del mazo barajado. El jugador 1 obtiene
        tarjetas restantes.
    '''

    for i in range(0, len(deck), 2):
        player2.hand += deck.deal(1)

    player1.hand += deck.deck  # Give player 1 (delear) all remaining cards


def get_ranking(card):
    '''
     devuelve el índice de una clasificación de cartas de la lista "clasificaciones" como una forma de comparar
     dos cartas y determina cuál gana
    '''

    return rankings.index(card.ranking)


def determine_winner(player_1_card, player_2_card):
    return [player_1_card, player_2_card]


def war(player1, player2, p1_pile, p2_pile):
    tie = True
    while tie and (len(player_1.hand) > 2) and (len(player_2.hand) > 2):
        p1_pile += player1.flip_card(2)
        p2_pile += player2.flip_card(2)
        print("Player 1 draws: X and {}".format(p1_pile[-1]))
        print("Player 2 draws: X and {}\n".format(p2_pile[-1]))

        if get_ranking(p1_pile[-1]) > get_ranking(p2_pile[-1]):
            print("Player 1 wins! \n")
            p1_pile += p2_pile
            tie = False
            return(1, p1_pile)
        elif get_ranking(p1_pile[-1]) < get_ranking(p2_pile[-1]):
            print("Player 2 wins! \n")
            p2_pile += p1_pile
            tie = False
            return(2, p2_pile)
        else:
            print("!!Guerra de nuevo!!")


#  ABAJO ESTÁ EL METODO MAIN

deck = Deck()
player_1 = Player()
player_2 = Player()
initial_deal(deck, player_1, player_2)
p1_discard_pile = []  # Estos son los montones de cartas ya jugadas
p2_discard_pile = []

round = 0  #contará cuántas rondas se necesitan para terminar el juego
while (len(player_1.hand) > 0) and (len(player_2.hand) > 0):
    p1_current_pile = []  # Pila de manos actual. Por lo general, 1 carta a menos que esté en guerra.
    p2_current_pile = []
    round += 1
    print("************ Round {} ************\n".format(round))

    p1_total_cards = len(player_1.hand) + len(p1_discard_pile)
    p2_total_cards = len(player_2.hand) + len(p2_discard_pile)

    print("Player 1 has {} total cards: {} holding and {} discarded"
          .format(p1_total_cards, len(player_1.hand), len(p1_discard_pile)))
    print("Player 2 has {} total cards: {} holding and {} discarded\n"
          .format(p2_total_cards, len(player_2.hand), len(p2_discard_pile)))

    p1_current_pile += player_1.flip_card(1)
    p2_current_pile += player_2.flip_card(1)

    print("Player 1 draws: {}".format(p1_current_pile[0]))
    print("Player 2 draws: {}\n".format(p2_current_pile[0]))

    if get_ranking(p1_current_pile[0]) > get_ranking(p2_current_pile[0]):
        print("Player 1 wins round {}! \n".format(round))
        p1_discard_pile += p1_current_pile + p2_current_pile
    elif get_ranking(p1_current_pile[0]) < get_ranking(p2_current_pile[0]):
        print("Player 2 wins round {}! \n".format(round))
        p2_discard_pile += p1_current_pile + p2_current_pile
    else:
        if (len(player_1.hand) > 2) and (len(player_2.hand) > 2):
            print("!!War!!\n")
            winner, war_pile = war(player_1, player_2, p1_current_pile,p2_current_pile)
            if winner == 1:
                p1_discard_pile += war_pile
            else:
                p2_discard_pile += war_pile

p1_total_cards = len(player_1.hand) + len(p1_discard_pile)
p2_total_cards = len(player_2.hand) + len(p2_discard_pile)
print("Final score: {} cards for Player 1, {} cards for Player 2"
      .format(p1_total_cards, p2_total_cards))