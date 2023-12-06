from unittest import TestCase, main

from unit_testing.LAB.test_cat.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_cat_size_is_increased_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_cat_cannot_sleep_if_not_fed_raises_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
