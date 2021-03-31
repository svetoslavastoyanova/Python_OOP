from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Any", "dog", "bark")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Any")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "bark")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Any makes bark")

    def test_get_kingdom_returns_value_of_private_attribute(self):
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_get_info(self):
        self.assertEqual(self.mammal.info(), "Any is of type dog")



if __name__ == "__main__":
    unittest.main()


