
"""
A newly opened multinational brand has decided to base their company logo on the 
three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on 
this condition. 

Given a string , which is the company name in lowercase letters, your task is to 
find the top three most common characters in the string.

Return the three most common characters along with their occurrence count as tuples.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above, Google would have 
its logo with the letters g, o, e. And the return of get_company_logo('Google')
would look like [('g', 2), ('o', 2), ('e', 1)]

"""

from typing import List


def get_company_logo(logo) -> List[tuple]:
    return NotImplementedError


if __name__ == '__main__':
    s = input()
    get_company_logo(s)

def test_get_company_logo():

    logo = "aabc"
    assert isinstance(get_company_logo(logo), list)
    assert len(get_company_logo(logo)) == 3
    assert get_company_logo(logo) == [('a', 2), ('b', 1), ('c', 1)]

    logo = "aabbbc"
    assert get_company_logo(logo) == [('b', 3), ('a', 2), ('c', 1)]

    logo = "aabbbcc"
    assert get_company_logo(logo) == [('b', 3), ('a', 2), ('c', 2)]

    logo = "ccbbbaa"
    assert get_company_logo(logo) == [('b', 3), ('a', 2), ('c', 2)]
