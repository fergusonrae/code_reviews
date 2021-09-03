"""
There are sets, A and B, each containing integers. 
You like all the integers in set A and dislike all the integers in set B. 

Your initial happiness is 0. For each integer in the array, if the int is in A,
you add 1 to your happiness. If the int is in set B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. 
However, the array might contain duplicate elements.
"""

from typing import List, Set

def get_happiness(integers: List[int], set_a: Set[int], set_b: Set[int]) -> int:
    happiness = 0
    for integer in integers:
        if integer in set_a:
            happiness += 1
        elif integer in set_b:
            happiness += -1
    return happiness
