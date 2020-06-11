import pdb;


def quick_sort1(lst):
    """
    sort an array

    runtime is O(nlogn) in most cases
    storage complexity is potentially O(nlogn) to O(n^2)

    There is an alternative version of quick sort with better storage complexity. 
    The other version will sort in place.
    """

    if len(lst) < 2:
        return lst

    #select midpoint
    mid = len(lst)//2
    pivot = lst[mid]

    low = []
    high = []
    eq = []

    for elem in lst:
        if elem < pivot:
            low.append(elem)
        elif elem > pivot:
            high.append(elem)
        elif elem == pivot:
            eq.append(elem)

    return quick_sort1(low) + eq + quick_sort1(high)



if __name__ == '__main__':

    print(quick_sort1([5, 2, 18, 3]))