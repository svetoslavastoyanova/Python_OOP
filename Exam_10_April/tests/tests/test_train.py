import unittest
from project.train.train import Train

class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train("Train", 1)

    def test_init(self):
        self.assertEqual(self.train.name, "Train")
        self.assertEqual(self.train.capacity, 1)
        self.assertEqual(self.train.passengers, [])
        self.assertEqual(self.train.TRAIN_FULL, "Train is full")
        self.assertEqual(self.train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(self.train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(self.train.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(self.train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(self.train.ZERO_CAPACITY, 0)

    def test_add_raises_value(self):
        self.train.passengers.append("Mark")
        self.assertEqual(len(self.train.passengers), 1)
        with self.assertRaises(ValueError) as exc:
            self.train.add("Mark2")
        self.assertEqual(str(exc.exception), self.train.TRAIN_FULL)

    def test_raises_value_error(self):
        self.train.capacity = 10
        self.train.passengers.append("Mark")
        self.assertEqual(len(self.train.passengers), 1)
        with self.assertRaises(ValueError)as exc:
            self.train.add("Mark")
        self.assertEqual(str(exc.exception), self.train.PASSENGER_EXISTS.format("Mark"))

    def test_add_successfully(self):
        self.assertEqual(self.train.add("Mark"), self.train.PASSENGER_ADD.format("Mark"))

    def test_remove_raises_value_error(self):
        self.train.add("Mark")
        with self.assertRaises(ValueError) as exc:
            self.train.remove("John")
        self.assertEqual(str(exc.exception), self.train.PASSENGER_NOT_FOUND.format("John"))

    def test_remove_successfully(self):
        self.train.add("Mark")
        self.assertEqual(len(self.train.passengers), 1)
        self.assertEqual(self.train.remove("Mark"), self.train.PASSENGER_REMOVED.format("Mark"))
        self.assertEqual(len(self.train.passengers), 0)









if __name__ == "__main__":
    unittest.main()