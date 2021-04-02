from project.player.advanced import Advanced
from project.card.card_repository import CardRepository
import unittest

class TestAdvanced(unittest.TestCase):

    def test_empty_name_raises_error(self):
        with self.assertRaises(Exception) as exc:
            result = Advanced("")
        self.assertEqual(str(exc.exception), "Player's username cannot be an empty string.")

    def test_name_is_ok(self):
        result = Advanced("name")
        self.assertEqual(result.username, "name")

    def test_health_is_below_zero(self):
        result = Advanced("name")
        with self.assertRaises(Exception) as exc:
            result.health = -10
        self.assertEqual(str(exc.exception), "Player's health bonus cannot be less than zero.")

    def test_health_is_equal_to_initial(self):
        result = Advanced("name")
        self.assertEqual(result.health, 250)

    def test_card_repository(self):
        result = Advanced("name")
        self.assertIsInstance(result.card_repository, CardRepository)

    def test_is_not_dead(self):
        result = Advanced("name")
        self.assertEqual(result.health, 250)
        self.assertFalse(result.is_dead)

    def test_is_dead(self):
        result = Advanced("name")
        result.health = 0
        self.assertTrue(result.is_dead)

    def test_damage_points_below_zero(self):
        result = Advanced("name")
        with self.assertRaises(Exception) as exc:
            result.take_damage(-1)
        self.assertEqual(str(exc.exception), "Damage points cannot be less than zero.")

    def test_damage_points_are_all_set(self):
        name = Advanced("name")
        name.take_damage(10)
        result = name.health
        self.assertEqual(result, 240)









if __name__ == "main":
    unittest.main()
