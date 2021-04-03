import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("Test", "type", 200, 200)

    def test_init(self):
        self.assertEqual(self.hardware.name, "Test")
        self.assertEqual(self.hardware.type, "type")
        self.assertEqual(self.hardware.capacity, 200)
        self.assertEqual(self.hardware.memory, 200)
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_install_is_all_set(self):
        to_install = Software("Software", "Express", 20, 50)
        self.hardware.install(to_install)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_install_raises_error(self):
        to_install = Software("Software", "Express", 1000, 1000)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(to_install)
        self.assertEqual(str(exc.exception), "Software cannot be installed")
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_uninstall(self):
        to_install = Software("Software", "Express", 50, 50)
        self.hardware.install(to_install)
        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(to_install)
        self.assertEqual(len(self.hardware.software_components), 0)




if __name__ == "__main__":
    unittest.main()