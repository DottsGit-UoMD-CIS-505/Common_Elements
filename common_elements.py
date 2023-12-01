"""
Author: Nicholas Butzke
"""


def find_common_elements(s, t):
    """
    Finds all common elements between s and t and stores them in u.
    """
    u = []

    # Convert s to a set for fast lookup: O(m)
    s_set = set(s)

    # Iterate through T and check for common elements: O(n)
    for ele in t:
        if ele in s_set:
            u.append(ele)
            s_set.remove(ele)

    return u
