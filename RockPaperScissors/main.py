class Game:
    variants = ['камень', 'ножницы', 'бумага']


    def __init__(self, players_n=2, bots_n=1, victory_limit = 1):
        self.players_n = players_n
        self.bots = [Bot for i in range(bots_n)]
        self.victory_limit = victory_limit
        self.victory_points = [0 for i in range(self.players_n + len(self.bots))]
        self.is_finished = False
        self.winner = None
        self.round_n = 0
        self.rounds_history = list()
        self.this_round = list()

    def get_last_rounds(self, n=1):
        # возвращает выборы каждого игрока на проивзовльное
        # количетсво раундов по запросу
        pass

    def make_round(self):
        self.this_round = list()
        for i in range(1, self.players_n + 1):
            while True:
                print('Ход игрока', i)
                print('Выбери камень "к" - ножницы "н" - бумага "б"')
                answ = input().strip().lower()
                if answ not in 'кнб':
                    print('Укажи одну букву')
                    continue
                else:
                    break
            self.this_round.append(answ)
        for bot in self.bots:
            self.this_round.append(bot.make_choice())
        self.check_round_victory()

    def check_round_victory(self):
        pass

    def check_endgame(self):
        if any(map(lambda x: True if x == self.victory_limit else False, self.victory_points)):
            res = self.victory_points.index(self.victory_limit) + 1
            if res <= self.players_n:
                self.winner = 'игрок ' + str(res)
            else:
                self.winner = 'бот ' + str(res - self.players_n)
            self.is_finished = False


class Bot:
    def __init__(self):
        pass

    def make_choice(self):
        return None

print('Игра "Камень-Ножницы-Бумага"')
print('В ней могут участовать игроки и боты')
p = int(input('Укажите количество игроков\n'))
b = int(input('Укажите количество ботов?\n'))
v = int(input('До скольки побед играем?\n'))
game = Game(p, b, v)
while not game.is_finished:
    game.make_round()