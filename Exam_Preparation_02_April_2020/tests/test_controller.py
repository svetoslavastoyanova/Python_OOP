import unittest

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner

class TestController(unittest.TestCase):
    def test_init_controller(self):
        result = Controller()
        self.assertEqual(len(result.player_repository.players), 0)
        self.assertEqual(len(result.card_repository.cards), 0)

    def test_add_players(self):
        result = Controller()
        test_one = result.add_player("Beginner", "name_one")
        test_two = result.add_player("Advanced", "name_two")
        self.assertEqual(test_one, f"Successfully added player of type Beginner with username: name_one")
        self.assertEqual(test_two, f"Successfully added player of type Advanced with username: name_two")

    def test_add_cards(self):
        result = Controller()
        card_one = result.add_card("Magic", "name_one")
        card_two = result.add_card("Trap", "name_two")
        self.assertEqual(card_one, f"Successfully added card of type MagicCard with name: name_one")
        self.assertEqual(card_two, f"Successfully added card of type TrapCard with name: name_two")

    def test_add_player_card(self):
        result = Controller()
        result.add_player("Beginner", "test_player_name")
        result.add_card("Magic", "test_card_name")
        final = result.add_player_card("test_player_name", "test_card_name")
        self.assertEqual(final, f"Successfully added card: test_card_name to user: test_player_name")

    def test_fight(self):
        result = Controller()
        result.add_player("Beginner", "player")
        result.add_player("Advanced", "enemy")
        self.assertEqual(result.fight("player", "enemy"),
        f"Attack user health 90 - Enemy user health 250")

    def test_report(self):
        result = Controller()
        result.add_player("Beginner", "player")
        result.add_player("Advanced", "enemy")
        self.assertEqual(result.report(), f"Username: player - Health: 50 - Cards 0\nUsername: enemy - Health: 250 - Cards 0\n")






if __name__ == "__main__":
    unittest.main()