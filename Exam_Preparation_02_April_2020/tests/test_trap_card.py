import unittest

from project.card.card import Card
from project.card.trap_card import TrapCard

DAMAGE_POINTS = 120
HEALTH_POINTS = 5


class TestTrapCard(unittest.TestCase):
    def test_if_name_empty_str(self):
        with self.assertRaises(Exception) as exc:
            result = TrapCard("")
        self.assertEqual(str(exc.exception), "Card's name cannot be an empty string.")

    def test_name_is_all_set(self):
        result = TrapCard("name")
        self.assertEqual(result.name, "name")

    def test_damage_points_less_than_zero(self):
        result = TrapCard("name")
        with self.assertRaises(Exception) as exc:
            result.damage_points = -1
        self.assertEqual(str(exc.exception), "Card's damage points cannot be less than zero.")

    def test_damage_points_are_all_set(self):
        result = TrapCard("name")
        self.assertEqual(result.damage_points, DAMAGE_POINTS)

    def test_health_points_less_than_zero(self):
        result = TrapCard("name")
        with self.assertRaises(Exception) as exc:
            result.health_points = -1
        self.assertEqual(str(exc.exception), "Card's HP cannot be less than zero.")

    def test_health_points_are_all_set(self):
        result = TrapCard("name")
        self.assertEqual(result.health_points, HEALTH_POINTS)


if __name__ == "__main__":
    unittest.main()