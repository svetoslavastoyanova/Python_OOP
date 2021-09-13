class Person:
    count_id = 0

    def __init__(self, name , surname ):
        self.name  = name
        self.surname = surname
        self.id = self.get_next_id ()

    @staticmethod
    def get_next_id():
        Person.count_id += 1
        next_id = Person.count_id
        return next_id


    def __add__(self, other):
        return f"{self.name} {other.surname}"

    def __repr__(self):
        return f"Person {self.id}: {self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name , people ):
        self.name  = name
        self.people  = people

    def __add__(self, other):
        return self.people + other.people

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"


    def __str__(self):
        members = ", ".join ( str(p) for p in self.people )
        return f"Group {self.name} with members {members}"


import unittest


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.p0 = Person('Aliko', 'Dangote')
        self.p1 = Person('Bill', 'Gates')
        self.p2 = Person('Warren', 'Buffet')
        self.p3 = Person('Elon', 'Musk')

    def test_person_init(self):
        self.assertEqual(self.p0.name, 'Aliko')
        self.assertEqual(self.p0.surname, 'Dangote')

    def test_person_str(self):
        self.assertEqual(str(self.p1), 'Bill Gates')

    def test_person_add(self):
        self.assertEqual(str(self.p2 + self.p3), 'Warren Musk')

    def test_group_init(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(first_group.name, '__VIP__')
        self.assertEqual(first_group.people, [self.p0, self.p1, self.p2])

    def test_group_str(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(str(first_group), "Group __VIP__ with members Aliko Dangote, Bill Gates, Warren Buffet")

    def test_group_len(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(len(first_group), 3)


if __name__ == "__main__":
    unittest.main()






