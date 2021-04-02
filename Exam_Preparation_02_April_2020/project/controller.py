from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            player = Beginner(username)
        else:
            player = Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            card = MagicCard(name)
        else:
            card = TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        searched_player = self.player_repository.find(username)
        searched_card = self.card_repository.find(card_name)
        if searched_card and searched_player:
            searched_player.card_repository.add(searched_card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            cards = p.card_repository.cards
            result += f"Username: {p.username} - Health: {p.health} - Cards {len(cards)}\n"
            for c in cards:
                result += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return result

