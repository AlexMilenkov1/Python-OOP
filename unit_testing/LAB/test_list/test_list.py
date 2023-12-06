from unittest import TestCase, main

from unit_testing.LAB.test_list.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, '23', True, False, 2.1222, 3)

    def test_init_correction_and_get_data_result(self):
        expected_result = [1, 2, 3]

        self.integer_list.get_data()

        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_add_method_add_el_and_returns_the_new_list(self):
        expected_list = self.integer_list.get_data() + [4]

        self.integer_list.add(4)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_add_method_receives_non_integer_el_and_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list.add('A')

        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_if_remove_index_method_removes_the_el_at_the_given_index(self):
        removed_element = self.integer_list.get_data().pop(0)

        self.integer_list.remove_index(0)

        self.assertNotIn(removed_element, self.integer_list.get_data())

    def test_when_remove_index_method_is_called_and_not_index_in_range_is_raised_index_error(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.remove_index(60)

        self.assertEqual(str(error.exception), "Index is out of range")

    def test_get_method_is_called_returning_element(self):
        expected_element = 1
        actual_element = self.integer_list.get(0)

        self.assertEqual(expected_element, actual_element)

    def test_get_method_with_invalid_index_then_raised_index_error(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.get(678)

        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_method_index_out_of_range_then_raised_index_error(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.insert(97, 1)

        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_method_type_of_element_in_not_integer_then_is_raised_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list.insert(0, 0.553)

        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_insert_method_added_on_correct_index_integer_element(self):
        added_element = 4

        self.integer_list.insert(0, 4)

        self.assertEqual(added_element, self.integer_list.get_data()[0])

    def test_get_biggest_method_returns_the_biggest_element(self):
        expected_biggest_element = 3

        actual_result = self.integer_list.get_biggest()

        self.assertEqual(expected_biggest_element, actual_result)

    def test_get_index_method_returning_the_index_of_the_element_given(self):
        expected_index = 2

        actual_index = self.integer_list.get_index(3)

        self.assertEqual(expected_index, actual_index)


if __name__ == "__main__":
    main()
