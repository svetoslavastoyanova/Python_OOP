import unittest
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_init(self):
        result = CardRepository()
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.cards), 0)

    def test_add(self):
        result = CardRepository()
        card = MagicCard("name")
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.cards), 0)
        result.add(card)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.cards), 1)

    def test_add_raises_error(self):
        result = CardRepository()
        card = MagicCard("name")
        result.add(card)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.cards), 1)
        with self.assertRaises(Exception) as exc:
            result.add(card)
        self.assertEqual(str(exc.exception), f"Card {card.name} already exists!")

    def test_remove(self):
        result = CardRepository()
        card = MagicCard("name")
        result.add(card)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.cards), 1)
        result.remove(card.name)
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.cards), 0)

    def test_remove_raises_error(self):
        result = CardRepository()
        with self.assertRaises(Exception) as exc:
            result.remove("")
        self.assertEqual(str(exc.exception), "Card cannot be an empty string!")
        self.assertEqual(result.count, 0)
        self.assertEqual(len(result.cards), 0)

    def test_find(self):
        result = CardRepository()
        card = MagicCard("name")
        result.add(card)
        self.assertEqual(result.find(card.name), card)












if __name__ == "__main__":
    unittest.main()