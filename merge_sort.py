"""Test memory consumption of merge_sort algorithm"""

#apply @profile decorator to enable memory profiling

from memory_profiler import profile
from make_list import lst_hard_coded
# import time

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

lst = [18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81]

@profile
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



if __name__ == '__main__':
    merge_sort(lst_hard_coded)
    
    # fig, ax = plt.subplots()
    
    # ax.plot(line_number, memory)

    # ax.set(xlabel='time (s)', ylabel='memory (MiB)',
    #        title='memory vs line_number')
    
    # ax.grid()
    
    # fig.savefig("binary_sort.png")


