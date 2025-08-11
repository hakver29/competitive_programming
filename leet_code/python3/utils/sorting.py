import unittest
from typing import List


class Sorting:
    def quicksort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[-1]
            lte = [x for x in arr[:-1] if x <= pivot]
            gt = [x for x in arr[:-1] if x > pivot]
            return self.quicksort(lte) + [pivot] + self.quicksort(gt)

    def mergesort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]
        left_sort = self.mergesort(left_side)
        right_sort = self.mergesort(right_side)

        i = j = k = 0
        sorted_arr = [None] * len(arr)
        while i < len(left_sort) and j < len(right_sort):
            if left_sort[i] < right_sort[j]:
                sorted_arr[i + j] = left_sort[i]
                i += 1
                k += 1
            else:
                sorted_arr[i + j] = right_sort[j]
                j += 1
                k += 1

        while i < len(left_side):
            sorted_arr[k] = left_sort[i]
            i += 1
            k += 1

        while j < len(right_side):
            sorted_arr[k] = right_sort[j]
            j += 1
            k += 1

        return sorted_arr


class TestCases(unittest.TestCase):
    test_case_1_input = [2, 23, 1, 23, 54, 23, 5433, 3, 44, 1, 2, 3]
    test_case_1_output = [1, 1, 2, 2, 3, 3, 23, 23, 23, 44, 54, 5433]

    def test_quicksort_example1(self):
        self.assertEqual(
            Sorting().quicksort(self.test_case_1_input),
            self.test_case_1_output,
        )

    def test_mergesort_example1(self):
        self.assertEqual(
            Sorting().mergesort(self.test_case_1_input),
            self.test_case_1_output,
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
