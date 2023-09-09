import random


class Deck:
    '''
    Так как реализовать колоду максимум может быть 4 карты каждой масти как это хранить думаю можно сделать словарь
    в котором хранятся все карты первое значение это 1 значение карты второе значение это масть карты
    '''
    def __init__(self):
        self.card_list = [6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.card_types = ['♣', '♦', '♥', '♠']
        self.cards = [{'value': x, 'suit': j} for j in self.card_types for x in self.card_list]
        [str(x['value']) + ' ' + x['suit'] for x in self.cards]

    def __str__(self):
        return '\n'.join([str(x['value']) + ' ' + x['suit'] for x in self.cards])


class FoolGame:
    ''' Тут я пытаюсь реализовать карточную игру "дурак".
    Я реализую её так: сначала пользователю первому выдается 6 случайных карт.
    Может быть, надо реализовать класс игрока, в котором содержатся его карты, или можно сделать это в одном классе.
    Также нужно было возможность отбивать карты, поднимать карты и получать. И можно сделать так, чтобы ход переходил
    от одного пользователя к другому. `player_one` это будет пустой список, и `player_two` тоже, в которых будет храниться карты.
    Потом будет переменная, которая будет означать ход пользователя, и переменная `move`,
    которая будет отслеживать чей ход: 0 - первого игрока, 1 - второго.
    теперь поочередно нужно реализовать функции ход на игрока и отбивание так же поднятие
    Еще нужна переменная стол где храняться все данные
    '''
    def __init__(self, my_deck: Deck):
        self.deck = my_deck
        self.trump = random.choice(my_deck.card_types)
        self.player_one = self._give_cards_for_players(6)
        self.player_two = self._give_cards_for_players(6)
        self.move = self._find_smallest_trump()
        self.players = [self.player_one, self.player_two]
        self.card_table = []
        print(f'Козырь партии {self.trump}')

    def _give_cards_for_players(self, count_of_cards):
        user_deck = random.sample(self.deck.cards, count_of_cards)
        for i in user_deck:
            self.deck.cards.remove(i)
        return user_deck

    def _find_smallest_trump(self):
        current_trump = self.trump
        first_player_trumps = [x.get('value') for x in self.player_one if x['suit'] == current_trump]
        second_player_trumps = [x.get('value') for x in self.player_two if x['suit'] == current_trump]
        print(first_player_trumps, second_player_trumps)
        if first_player_trumps and second_player_trumps: # если в колодах у двух игроков есть козыри
            if min(first_player_trumps) < min(second_player_trumps):
                return 0  # если значение карты у первого игрока меньше, то он ходит
            else:
                return 1  # если нет, то ходит второй
        elif first_player_trumps:  # если у первого пользователя не пуста колода, то он ходит
            return 0
        elif second_player_trumps:  # аналогично
            return 1
        else:  # если две колоды пустые, то выбираем случайно
            return random.randint(0, 1)

    def _get_current_cards(self):
        cards = self.players[self.move]
        return '\n'.join([str(str(j) + ') ' + str(x['value'])) + ' ' + x['suit'] for j, x in enumerate(cards, 1)])

    def _value_in_list(self, value):
        values = [x['value'] for x in self.card_table]
        print(values)
        print(value)
        if value in values:
            return True
        else:
            return False

    def hit_cards(self):
        player_cards = self.players[self.move]
        if player_cards == 0:
            print(f'Пользователь {self.move}+1 выиграл')
        print(self.card_table)
        if len(self.card_table) >= 1:
            hit_card_choose = int(input('Выберите карту которую вы хотите отбить ')) -1
            hit_card = self.card_table[hit_card_choose]
            print(hit_card)
            cards = self._get_current_cards()
            print(cards)
            index = int(input(f'Игрок {self.move+1} Выберите Карту которой хотите отбить  или поднимите карты')) - 1

            if index == -1:
                for i in self.card_table:
                    player_cards.append(i)
                self.card_table.clear()
                self.move = not self.move
                return self.player_move()
            card = player_cards[index]
            print(card)
            print(hit_card)
            if card['suit'] == self.trump and hit_card['suit'] != self.trump:
                player_cards.pop(index)
                self.card_table.pop(hit_card_choose)
                print('Вы отбили карту')
                self.hit_cards()
            elif hit_card['suit'] == card['suit'] and hit_card['value'] < card['value']:
                player_cards.pop(index)
                self.card_table.pop(hit_card_choose)
                print('Вы отбили карту')
                self.hit_cards()
            else:
                print('Вы не отбили карту')
                self.hit_cards()
        else:
            player_cards = self.players[self.move]
            if len(self.card_table) == 0:
                card_len = 6 - len(player_cards)
                if card_len > 0:
                    if len(self.deck) > card_len:
                        gave_cards = self._give_cards_for_players(card_len)
                        player_cards.extend(gave_cards)
                    else:
                        if self.deck == 0:
                            pass
            print(f'Стол закончился пользователь {self.move+1} Ходите')
            self.player_move()

    def player_move(self):
        player_cards = self.players[self.move]
        if len(self.card_table) == 0:
            card_len = 6 - len(player_cards)
            if card_len > 0:
                if len(self.deck) > card_len:
                    gave_cards = self._give_cards_for_players(card_len)
                    player_cards.extend(gave_cards)
                else:
                    if self.deck == 0:
                        pass
        if player_cards == 0:
            print(f'Игрок {self.move+1} выиграл')
            return 1
        cards = self._get_current_cards()
        print('Текущий стол')
        print(self.card_table)

        print(cards)
        index = int(input(f'Игрок {self.move+1} Выберите Карты которые хотите скинуть или завершите ход ')) -1
        print(index)
        if index == -1:

            if len(self.card_table) >= 1:
                print('Вы завершили ход')
                self.move = not self.move
                self.hit_cards()
            else:
                print('Вы не можете завершить ход пока стол пустой')
                self.player_move()
        player_cards = self.players[self.move]
        card = player_cards[index]
        if self._value_in_list(card['value']) and len(self.card_table) >= 1:
            self.card_table.append(player_cards[index])
            player_cards.pop(index)
            print(f'Карта которую вы поставили {card}')
            self.player_move()
        elif len(self.card_table) == 0:
            self.card_table.append(player_cards[index])
            player_cards.pop(index)
            print(f'Карта которую вы поставили {card}')
            self.player_move()
        else:
            print('Вы не можете поставить эту карту на стол')
            self.player_move()


deck = Deck()
game = FoolGame(deck)
game.player_move()
