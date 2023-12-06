from unittest import TestCase, main

from unit_testing.LAB.test_worker.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Toni', 4000, 10)

    def test_is_initialization_correct(self):
        self.assertEqual('Toni', self.worker.name)
        self.assertEqual(4000, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_incremented_after_calling_rest_method(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_money_increment_by_salary_after_work_method_is_called(self):
        expected_money = self.worker.money + self.worker.salary

        self.worker.work()
        self.assertEqual(expected_money, self.worker.money)

    def test_energy_decrement_by_one_after_work_method_is_called(self):
        expected_energy = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_error_raised_when_worker_try_to_work_with_negative_or_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_get_info_return_correct_data(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()
