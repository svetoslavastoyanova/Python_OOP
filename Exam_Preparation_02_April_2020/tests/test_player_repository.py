import unittest
from project.player.player_repository import PlayerRepository
from project.player.advanced import Advanced


class TestPlayerRepository(unittest.TestCase):
    def test_init(self):
        result = PlayerRepository()
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.players), 0)

    def test_add(self):
        result = PlayerRepository()
        player = Advanced("name")
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.players), 0)
        result.add(player)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.players), 1)

    def test_add_raises_error(self):
        result = PlayerRepository()
        player = Advanced("name")
        result.add(player)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.players), 1)
        with self.assertRaises(Exception) as exc:
            result.add(player)
        self.assertEqual(str(exc.exception), f"Player {player.username} already exists!")

    def test_remove(self):
        result = PlayerRepository()
        player = Advanced("name")
        result.add(player)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.players), 1)
        result.remove(player.username)
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.players), 0)

    def test_remove_raises_error(self):
        result = PlayerRepository()
        with self.assertRaises(Exception) as exc:
            result.remove("")
        self.assertEqual(str(exc.exception), "Player cannot be an empty string!")
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.players), 0)

    def test_find(self):
        result = PlayerRepository()
        player = Advanced("name")
        result.add(player)
        self.assertEqual(result.find(player.username), player)


if __name__ == "__main__":
    unittest.main()