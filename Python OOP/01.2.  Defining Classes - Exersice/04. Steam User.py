class SteamUser:

    def __init__(self, username, games, played_hours=0):
        self.username = username
        self.games = list(games)
        self.played_hours = played_hours

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        return f'{game} is not in library'

    def buy_game(self, game):
        if game in self.games:
            return f'{game} is already in your library'
        else:
            self.games.append(game)
            return f'{self.username} bought {game}'

    def stats(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


# Test code:

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.stats())

# Expected output:

# Peter is playing Fortnite
# Oxygen Not Included not in library
# CS:GO is already in your library
# Peter bought Oxygen Not Included
# Peter is playing Oxygen Not Included
# Peter has 4 games. Total play time: 9

