"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Merge sort
Sorting array practice
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Sort an unsorted array in O(nlogn) time complexity

"""

def merge_sort(arr):
    """
    decompose the array into arrays of length 1
    recombine the arrays in a sorted manner, using the helper function
    
    Developer notes: 
    This solution is not ideal because it uses 'pop(0)' in the helper function, 
    which adds O(n) run time.
    """

    if len(arr) < 2:
        print(f'returning arr: {arr}')
        return arr

    mid = len(arr)//2
    
    lst1 = merge_sort(arr[:mid])
    lst2 = merge_sort(arr[mid:])

    return merge(lst1, lst2)


def merge(lst1, lst2):
    """combine two sorted arrays into a single sorted array"""

    res = []

    # add the lowest value to res
    while len(lst1) > 0 or len(lst2) > 0:
        
        # add the value of the remaining list if one list is empty
        if lst1 == []:
            res.append(lst2.pop(0))

        elif lst2 == []:
            res.append(lst1.pop(0))

        # append the lesser value to res
        elif lst1[0] < lst2[0]:
            res.append(lst1.pop(0))
        
        else:
            res.append(lst2.pop(0))
        
    return res


if __name__ == '__main__':

    print(merge_sort([3, 1, 4]))