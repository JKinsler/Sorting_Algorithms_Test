"""Test memory consumption of bubble_sort algorithm"""

#apply @profile decorator to enable memory profiling

from memory_profiler import profile
from make_list import lst_hard_coded
# import time

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

lst = [18, 34, 12, 21, 48, 59, 3, 82, 53, 6, 33, 7, 99, 91, 17, 13, 45, 38, 77, 81]

@profile
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


if __name__ == '__main__':
    bubble_sort(lst_hard_coded)
    
    # fig, ax = plt.subplots()
    
    # ax.plot(line_number, memory)

    # ax.set(xlabel='time (s)', ylabel='memory (MiB)',
    #        title='memory vs line_number')
    
    # ax.grid()
    
    # fig.savefig("binary_sort.png")