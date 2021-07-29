"""
There are disjoint sets, A and B, each containing integers. 
You like all the integers in set A and dislike all the integers in set B. 

Your initial happiness is 0. For each integer in the array, if the int is in A,
you add 1 to your happiness. If the int is in set B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. 
However, the array might contain duplicate elements.
"""

from typing import List, Set

def get_happiness(integers: List[int], set_a: Set[int], set_b: Set[int]) -> int:
    raise NotImplementedError


def test_get_happiness():

    # Test 1
    set_a = {1}
    set_b = {2}
    integers_to_check = [1]
    assert isinstance(get_happiness(integers_to_check, set_a, set_b), int)
    assert get_happiness(integers_to_check, set_a, set_b) == 1

    # Test 2
    set_a = {2}
    set_b = {1}
    integers_to_check = [1]
    assert get_happiness(integers_to_check, set_a, set_b) == -1

    # Test 3
    set_a = {1, 3, 4}
    set_b = {2, 5}
    integers_to_check = [1]
    assert get_happiness(integers_to_check, set_a, set_b) == 1

    # Test 4
    set_a = {1}
    set_b = {2}
    integers_to_check = [80]
    assert get_happiness(integers_to_check, set_a, set_b) == 0

    # Test 5
    set_a = {1, 80, 4, 3, 99}
    set_b = {2, 5, 34, 42, 12, 14}
    integers_to_check = [80, 5, 2, 12]
    assert get_happiness(integers_to_check, set_a, set_b) == -2

    # Test 5
    set_a = {1, 80, 4, 3, 99}
    set_b = {2, 5, 34, 42, 12, 14}
    integers_to_check = [80, 80, 80, 5, 2, 12]
    assert get_happiness(integers_to_check, set_a, set_b) == 0