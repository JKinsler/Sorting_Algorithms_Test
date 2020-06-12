
"""CCI problem 10.1

Sorted Merge: You are given two sorted arrays, A and B, where A has a large 
enough buffer at the end to hold B. Write a method to merge B into A in sorted 
order.


Solved 6/11/20
Time for solving(15min), testing, debugging(15min) = 30min
- the correct solution would have taken longer
"""


def s_merge(arr1, arr2):

    """
    Return a sorted array given two sorted input arrys. Arr1 has a long enough
    buffer to hold arr2.

    plan
    1. make a pointer for each arr
    2. check value at the pointer
    3. intsert B into A where needed for sorted order
        Insert methods will have O(n) rutime --> worst case On^2 runtime
        Better runtime: create a new list (will have space penalty)
    """

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr1 = arr1[:i]+[arr2[j]]+arr1[i:-1]
            j+= 1

        i+=1

    return arr1


def s_merge_CCI(lst_a, lst_b):
    i_a = 0
    i_b = 0
    i_ab = 0

    while i_b >=0:
        if i_a >= 0 and lst_a[i_a] > lst_b[i_b]:
            lst_a[i_ab] = lst_[i_a]

if __name__ == '__main__':

    print(s_merge([1, 3, 0], [2]))

"""
Notes:
CCI solution has better runtime because they start adding elements at the end
of the list, then swap the rest of the contents into place.
"""