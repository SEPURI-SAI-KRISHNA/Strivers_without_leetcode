"""
Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}
Output:
 5
Explanation:

5 is the largest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}
Output:
 10
Explanation:

10 is the largest element in the array.
"""


def largest_number(arr):
    temp = float('-inf')

    for i in arr:
        if i > temp:
            temp = i
    return temp


print(largest_number([2, 5, 1, 3, 0]))
print(largest_number([8, 10, 5, 7, 9]))
