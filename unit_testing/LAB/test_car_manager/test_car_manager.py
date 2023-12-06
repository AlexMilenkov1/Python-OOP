from unittest import TestCase, main

# from car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car('BMW', 'E36', 8, 70)

    def test_correct_init(self):
        self.assertEqual('BMW', self.car.make)
        self.assertEqual('E36', self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_given_empty_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car('', 'E36', 8, 70)

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_given_empty_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car('BMW', '', 8, 70)

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car('BMW', 'E36', -1, 70)

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car('BMW', 'E36', 8, -10)

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -30

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_the_value_for_refuel_is_negative_number_and_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_is_refueling_and_do_not_extend_the_capacity(self):
        self.car.refuel(75)

        self.assertEqual(70, self.car.fuel_amount)

    def test_drive_with_enough_fuel(self):
        self.car.refuel(1000)
        self.car.drive(20)

        self.assertEqual(68.4, self.car.fuel_amount)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(70)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    main()
