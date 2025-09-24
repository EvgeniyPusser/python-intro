from unittest import TestCase, main
from codes_testing import find_sums   # функция из hello.py
from codes_testing import maxNumberWithOppositeSigns  # функция из codes_testing.py

class TestFindSums(TestCase):
    def test_find_sums(self):
        self.assertEqual(find_sums([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(find_sums([1, 2, 3, 4], 8), None)
        self.assertEqual(find_sums([0, 0, 0, 0], 0), (0, 1))


    
    
class TestMaxNumberWithOppositeSigns(TestCase):
    def test_max_number_with_opposite_signs(self):
        from codes_testing import maxNumberWithOppositeSigns  # функция из codes_testing.py
        
        self.assertEqual(maxNumberWithOppositeSigns([3, -1, -4, -90, 90, 2, 4, -3]), (90, 4))
        self.assertEqual(maxNumberWithOppositeSigns([1, 2, 3, 4]), None)
        self.assertEqual(maxNumberWithOppositeSigns([-5, -10, 5, 10]), (10, 3))
        self.assertEqual(maxNumberWithOppositeSigns([0, 0, 0]), None)
        self.assertEqual(maxNumberWithOppositeSigns([7, -7, 8, -8, 9]), (8, 3))
        
if __name__ == "__main__":
    main()
    
    
