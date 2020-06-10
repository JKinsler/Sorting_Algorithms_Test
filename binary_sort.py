"""Test memory consumption of binary_sort algorithm"""

#apply @profile decorator to enable memory profiling

from memory_profiler import profile
from make_list import lst_hard_coded
# import time

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np



lst = [18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81]

@profile
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


if __name__ == '__main__':
    binary_sort(lst_hard_coded)
    
    # fig, ax = plt.subplots()
    
    # ax.plot(line_number, memory)

    # ax.set(xlabel='time (s)', ylabel='memory (MiB)',
    #        title='memory vs line_number')
    
    # ax.grid()
    
    # fig.savefig("binary_sort.png")