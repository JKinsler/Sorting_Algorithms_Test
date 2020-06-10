"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Merge sort
Sorting array practice
6/9/20
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Sort an unsorted array in O(nlogn) time complexity

Developer notes: this is my favorite way to organize the merge sort algorithm
because I think it's easily readable.
"""

def merge_sort(arr):

    """
    Divide a conquer sort method with O(nlog(n)) runtime
    """

    # set the recursion base case
    if len(arr) < 2:
        return arr
    
    # divide the list
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    """
    combine the two sorted lists into a single sorted list
    """

    i_left = 0
    i_right = 0

    res = []

    #interleave right and left into a list
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            res.append(left[i_left])
            i_left += 1
        else:
            res.append(right[i_right])
            i_right += 1

    # add remaining values from the left index
    while i_left < len(left):
        res.append(left[i_left])
        i_left += 1

    # add remaining values from the right index
    while i_right < len(right):
        res.append(right[i_right])
        i_right += 1

    return res


if __name__ == '__main__':
    print(merge_sort([3, 1, 2]))
    print(merge_sort([]))
    print(merge_sort([8, 1, 35, 2, 16]))

