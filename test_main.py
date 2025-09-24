from unittest import TestCase, main
from hello import bSearch   # функция из hello.py

class BinarySearchTest(TestCase):
    def setUp(self):
        self.numbers = [1, 2, 2, 2, 5, 6, 7, 8, 9]

    def test_found_occurrence(self):
        # первый элемент
        self.assertEqual(bSearch(self.numbers, 1), 0)
        # последний элемент
        self.assertEqual(bSearch(self.numbers, 9), len(self.numbers) - 1)
        # число 2 встречается несколько раз → результат может быть 1, 2 или 3
        self.assertIn(bSearch(self.numbers, 2), [1, 2, 3])
        # число 5 в массиве на позиции 4
        self.assertEqual(bSearch(self.numbers, 5), 4)

    def test_not_found(self):
        # число меньше минимального
        self.assertEqual(bSearch(self.numbers, -10), -1)
        # число между 2 и 5, которого нет
        self.assertEqual(bSearch(self.numbers, 4), -1)
        # число больше максимального
        self.assertEqual(bSearch(self.numbers, 90), -1)

    def test_empty_array(self):
        self.assertEqual(bSearch([], 1), -1)

if __name__ == "__main__":
    main()

        