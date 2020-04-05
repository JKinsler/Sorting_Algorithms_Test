"""Compare timing on different sorting algorithims.

A note on timer units: The units follow the decault of your OS. Since I'm running 
Windows, the units should follow time.clock(), which runs in microseconds.
See Timeit documentation for more information 
https://docs.python.org/2/library/timeit.html"""


lst = [18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81]
number = 100000

"""BUBBLE SORT"""
def bubble_sort(lst):
    """Shorter and fast-win bubble sort."""

    for i in range(len(lst) - 1):
        # keep track of whether we made a swap
        made_swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
        if not made_swap:
            # If no swap, list already sorted
            break

    return lst


def merge_sort(lst):
    """Merge sort.

    Divide and conquer: reduce to lists of 0-1 items, then recombine.

    Runtime: O(n log n)
    """

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge-lecture-snippet-start
        left_index = right_index = new_index = 0

        # Interleave left and right into list

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1
        # merge-lecture-snippet-end

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1

    return lst


def binary_sort(lst):
    """Add items to binary heap (keeping them in order!) and then extract."""

    def move_down(first, last):
        """Move item down in heap to proper place."""

        # Assume left-hand child is bigger
        largest = 2 * first + 1

        while largest <= last:
            if largest < last and lst[largest] < lst[largest + 1]:
                # Right child exists and is larger than left child
                largest += 1

            if lst[largest] > lst[first]:
                # Selected child is bigger than parent, so swap
                lst[largest], lst[first] = lst[first], lst[largest]

                # Move down to largest child
                first = largest
                largest = 2 * first + 1

            else:
                # Once we don't swap, it's in the right place; exit
                return

    # Convert lst to heap

    length = len(lst) - 1
    least_parent = length // 2

    for i in range(least_parent, -1, -1):
        move_down(i, length)

    # Flatten heap into sorted array

    for i in range(length, 0, -1):
        if lst[0] > lst[i]:
            lst[0], lst[i] = lst[i], lst[0]
            move_down(0, i - 1)

    return lst

def quick_sort(lst):
    """Quicksort.

    Iteratively pivot, sort lists, and combine.

    Runtime: O(n log n)
    """

    import random

    def _quicksort(lst, first, last):
        if first < last:

            # Find pivot point

            pivot = first + random.randrange(last - first + 1)
            lst[pivot], lst[last] = lst[last], lst[pivot]

            pivot = first

            for i in range(pivot, last):
                if lst[i] <= lst[last]:
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    pivot += 1

            lst[pivot], lst[last] = lst[last], lst[pivot]

            # Recurse
            _quicksort(lst, first, pivot - 1)
            _quicksort(lst, pivot + 1, last)

    _quicksort(lst, 0, len(lst) - 1)

    return lst


if __name__ == '__main__':
    import timeit
    print('quick_sort run time:')
    print(timeit.timeit("quick_sort([18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81])",\
                        setup="from __main__ import quick_sort, number",\
                        number = number))

    print('merge_sort run time:')
    print(timeit.timeit("merge_sort([18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81])",\
                        setup="from __main__ import merge_sort, number",\
                        number = number))
    
    print('binary_sort run time:')
    print(timeit.timeit("binary_sort([18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81])",\
                        setup="from __main__ import binary_sort, number",\
                        number = number))

    print('bubble_sort run time:')
    print(timeit.timeit("bubble_sort([18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81])",\
                        setup="from __main__ import bubble_sort, number",\
                        number = number))

    

    

    
