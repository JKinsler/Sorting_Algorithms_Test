"""CCI problem 10.2, page 150

Group anagrams: Write a method to sort an array of strings so that all the 
anagrams are next to each other.


Solved 6/11/20
Time for solving(didn't get it), testing, debugging(1hr) = 2.5hr
"""

def group_grams(lst):

    """
    Sorts a list where anagrams are paired

    Estimated time: 30 min
    Actual time: 1hr. didn't get the solution, wasn't thinking of using a 
    built-in function

    Example:
    >>> group_grams([bob, dog, fish, god])
    [bob, dog, god, fish]

    steps:
    1. sort each word, match it with the orignial word in a tuple
      
    2. sort the tuples by the original word

    3. take the original word and put them in a list

    4. return the list

    Runtime estimation: O(nlogn*slogs)

    """
   
def group_anagrams(lst):

    pair_tuples = [(s, sorted(s)) for s in lst] #O(n*slogs)
    print(pair_tuples)
    pairs = sorted(pair_tuples, key = lambda pair: pair[1]) #O(n*logn)
    print(pairs)
    return [w[0] for w in pairs]


if __name__ == '__main__':
    print(group_anagrams(["cat", "dog", "tac", "god", "tar"]))
    