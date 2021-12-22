from collections import defaultdict


class DiceGame:
    def __init__(self, data):
        line_1, line_2 = data.split('\n')
        self.position_1 = int(line_1.split()[-1])
        self.position_2 = int(line_2.split()[-1])
        self.score_1 = self.score_2 = 0
        self.roll_count = 0

    def roll(self, position, score):
        position = (position + 3 * self.roll_count + 5) % 10 + 1
        score += position
        return position, score

    def roll_player_1(self):
        self.position_1, self.score_1 = self.roll(self.position_1, self.score_1)
        self.roll_count += 3

    def roll_player_2(self):
        self.position_2, self.score_2 = self.roll(self.position_2, self.score_2)
        self.roll_count += 3

    def roll_until_win(self):
        while (self.score_1 < 1000) and (self.score_2 < 1000):
            self.roll_player_1()
            if self.score_1 >= 1000:
                break
            self.roll_player_2()


class DiracDice(DiceGame):
    def __init__(self, data):
        super().__init__(data)
        self.state_dict_1 = {(self.position_1, 0): 1}
        self.state_dict_2 = {(self.position_2, 0): 1}
        self.roll_dict = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    def dirac_roll(self, state_dict):
        new_dict = defaultdict(int)
        wins = 0
        for (position, score), count in state_dict.items():
            for roll, ways in self.roll_dict.items():
                new_position = (position + roll - 1) % 10 + 1
                new_score = score + new_position
                if new_score >= 21:
                    wins += count * ways
                else:
                    new_dict[(new_position, new_score)] += count * ways
        return wins, new_dict

    def roll_player_1(self):
        wins, self.state_dict_1 = self.dirac_roll(self.state_dict_1)
        return wins

    def roll_player_2(self):
        wins, self.state_dict_2 = self.dirac_roll(self.state_dict_2)
        return wins

    def count_winning_universes(self):
        total_wins_1 = total_wins_2 = 0
        while self.state_dict_1 and self.state_dict_2:
            wins_1 = self.roll_player_1()
            if wins_1:
                total_wins_1 += wins_1 * sum(self.state_dict_2.values())
            wins_2 = self.roll_player_2()
            if wins_2:
                total_wins_2 += wins_2 * sum(self.state_dict_1.values())
        return total_wins_1, total_wins_2


if __name__ == '__main__':
    with open('data/day_21_input.txt', 'r') as f:
        data = f.read().strip()
    game = DiceGame(data)

    game.roll_until_win()
    part_1 = min(game.score_1, game.score_2) * game.roll_count

    dirac_game = DiracDice(data)
    wins_1, wins_2 = dirac_game.count_winning_universes()
    part_2 = max(wins_1, wins_2)

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
