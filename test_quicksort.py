import unittest
import random
import copy

from quicksort import quicksort

class TestQuickSort(unittest.TestCase):
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        self.assertEqual(quicksort(arr), [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        arr = [5]
        self.assertEqual(quicksort(arr), [5])
    
    def test_sorted_array(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = sorted(copy.deepcopy(arr))
        self.assertEqual(quicksort(arr), expected)
    
    def test_random_array(self):
        """Test sorting a random array."""
        arr = [random.randint(0, 1000) for _ in range(100)]
        expected = sorted(copy.deepcopy(arr))
        self.assertEqual(quicksort(arr), expected)
    
    def test_large_array(self):
        """Test sorting a large array."""
        arr = [random.randint(0, 10000) for _ in range(1000)]
        expected = sorted(copy.deepcopy(arr))
        self.assertEqual(quicksort(arr), expected)
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-5, 3, 0, -8, 7, -2, 4]
        self.assertEqual(quicksort(arr), [-8, -5, -2, 0, 3, 4, 7])
    
    def test_mixed_types(self):
        """Test sorting an array with mixed numeric types."""
        arr = [5, 3.14, -2, 0, 1.5, -6.7]
        self.assertEqual(quicksort(arr), [-6.7, -2, 0, 1.5, 3.14, 5])

if __name__ == '__main__':
    unittest.main()