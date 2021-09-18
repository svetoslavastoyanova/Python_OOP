class Guild:
    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != self.name and player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        self.list_of_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        player_names = [p.name for p in self.list_of_players]
        if player_name not in player_names:
            return f"Player {player_name} is not in the guild."
        else:
            del self.list_of_players[player_name.index(player_name)]
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.list_of_players:
            result += f"{p.player_info()}\n"
        return result
