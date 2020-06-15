"""CCI problem 10.5, page 150

Sparse Search: Given a sorted array of strings that is interspersed with empty
strings, write a method to find the location of a given string.


Solved 6/14/20
Estimated time for solving: 45min (4:30pm)
"""
import unittest

def sparse_search(lst, string):

    """
    Methods:
    use python built-in function to find the value and then return the index
        - enumerate?
        - O(n) runtime

    Binary search
        - O(logn)

    steps 
    """

    if [""]*len(lst) == lst:
        return None

    low = 0
    high = len(lst)-1

    while low <= high:

        mid = low + (high - low) // 2 # need middle to be the integer midpoint between low and high

        while lst[mid] == "" and mid < len(lst):
            mid += 1
            if mid == len(lst) - 1 and lst[mid] == "":
                mid = low 

        if lst[mid] < string:
            low = mid + 1
        elif lst[mid] > string:
            high = mid - 1
        elif mid == "":
            return None
        else:
            return mid

    return None


class TestSparseSearch(unittest.TestCase):

    def test_sparse_search(self):

        self.assertEqual(sparse_search(["a", "d", "e", "g"], "e"), 2)
        self.assertEqual(sparse_search(["a", "", "e", "g"], "e"), 2)
        self.assertEqual(sparse_search(["a", "", "", ""], "a"), 0)
        self.assertEqual(sparse_search(["", "", "", "g"], "g"), 3)
        self.assertEqual(sparse_search(["", "", "", ""], "g"), None)
        self.assertEqual(sparse_search([], "g"), None)
        self.assertEqual(sparse_search([], ""), None)


if __name__ == '__main__':

    unittest.main()
