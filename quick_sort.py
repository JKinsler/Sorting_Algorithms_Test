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
    quick_sort(lst_hard_coded)
    
    # fig, ax = plt.subplots()
    
    # ax.plot(line_number, memory)

    # ax.set(xlabel='time (s)', ylabel='memory (MiB)',
    #        title='memory vs line_number')
    
    # ax.grid()
    
    # fig.savefig("binary_sort.png")