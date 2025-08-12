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

    def heapify(self, arr, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[i] < arr[left_child]:
            largest = left_child

        if right_child < n and arr[largest] < arr[right_child]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapify(arr, n, largest)

    def heapsort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]

            self.heapify(arr, i, 0)

        return arr

    def countingsort(self, arr):
        if not arr:
            return []

        max_val = max(arr)

        count = [0] * (max_val + 1)

        for num in arr:
            count[num] += 1

        output = []

        for i, freq in enumerate(count):
            output.extend([i] * freq)

        return output

    def insertionsort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]

            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
        return arr


class TestCases(unittest.TestCase):
    test_case_1_input = [2, 23, 1, 23, 54, 23, 5433, 3, 44, 1, 2, 3]
    test_case_1_output = [1, 1, 2, 2, 3, 3, 23, 23, 23, 44, 54, 5433]

    test_case_2_input = [12, 11, 13, 5, 6, 7]
    test_case_2_output = [5, 6, 7, 11, 12, 13]

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

    def test_heapsort_example_1(self):
        self.assertEqual(
            Sorting().heapsort(self.test_case_2_input), self.test_case_2_output
        )

    def test_countingsort_example_1(self):
        self.assertEqual(
            Sorting().countingsort(self.test_case_2_input), self.test_case_2_output
        )

    def test_insertionsort_example_1(self):
        self.assertEqual(
            Sorting().insertionsort(self.test_case_2_input), self.test_case_2_output
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
