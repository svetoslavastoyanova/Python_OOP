import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):

    def setUp(self):
        self.factory = PaintFactory("Factory", 10)

    def test_init(self):
        self.assertEqual(self.factory.name, "Factory")
        self.assertEqual(self.factory.capacity, 10)
        self.assertEqual(len(self.factory.ingredients), 0)
        self.assertEqual(self.factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.factory.products, self.factory.ingredients)

    def test_add_ingredient_raises_type_error(self):
        self.assertEqual(len(self.factory.ingredients), 0)
        with self.assertRaises(Exception) as exc:
            self.factory.add_ingredient("black", 1)
        self.assertEqual(str(exc.exception), "Ingredient of type black not allowed in PaintFactory")
        self.assertEqual(len(self.factory.ingredients), 0)

    def test_add_ingredient_raises_value_error(self):
        with self.assertRaises(Exception) as exc:
            self.factory.add_ingredient("white", 11)
        self.assertEqual(str(exc.exception), "Not enough space in factory")
        self.assertEqual(len(self.factory.ingredients), 0)

    def test_add_ingredient_successfully_first_test(self):
        self.assertEqual(len(self.factory.ingredients), 0)
        self.factory.add_ingredient("white", 1)
        self.assertEqual(self.factory.ingredients["white"], 1)

    def test_add_ingredient_successfully_second_test(self):
        self.factory.add_ingredient("white", 1)
        self.factory.add_ingredient("white", 2)
        self.assertEqual(self.factory.ingredients["white"], 3)

    def test_remove_ingredient_raises_key_error(self):
        self.factory.add_ingredient("white", 1)
        with self.assertRaises(KeyError) as exc:
            self.factory.remove_ingredient("black", 1)
        # self.assertEqual(str(exc.exception), "No such product in the factory")
        self.assertEqual(len(self.factory.ingredients), 1)

    def test_remove_ingredient_raises_value_error(self):
        self.factory.add_ingredient("white", 1)
        with self.assertRaises(ValueError) as exc:
            self.factory.remove_ingredient("white", 2)
        self.assertEqual(str(exc.exception), "Ingredient quantity cannot be less than zero")
        self.assertEqual(self.factory.ingredients["white"], 1)

    def test_remove_ingredient_successfully(self):
        self.factory.add_ingredient("white", 2)
        self.factory.remove_ingredient("white", 1)
        self.assertEqual(self.factory.ingredients["white"], 1)

    def test_remove_ingredient_successfully_second_test(self):
        self.factory.add_ingredient("white", 2)
        self.factory.remove_ingredient("white", 2)
        self.assertEqual(self.factory.ingredients["white"], 0)

    def test_can_add_returns_true(self):
        self.factory.add_ingredient("white", 1)
        self.assertTrue(self.factory.can_add(2))

    def test_can_add_returns_true_for_equal_to_zero(self):
        self.factory.add_ingredient("white", 9)
        self.assertTrue(self.factory.can_add(1))

    def test_can_add_returns_false(self):
        self.factory.add_ingredient("white", 10)
        self.assertFalse(self.factory.can_add(10))


if __name__ == "__main__":
    unittest.main()