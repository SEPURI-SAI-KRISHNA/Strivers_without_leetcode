"""
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 1
Explanation: Index 1 is the smallest index such that arr[1] >= x.

Example 2:
Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] >= x.
"""


def lower_bound(arr, x, n):
    l = 0
    r = n - 1

    while l <= r:
        m = (l + r) // 2
        if x <= arr[m]:
            if x > arr[m - 1]:
                return m
            else:
                r = m - 1
        elif x > arr[m]:
            l = m + 1
    return -1


print(lower_bound([1, 2, 2, 3], 2, 4))
print(lower_bound([3, 5, 8, 15, 19], 9, 5))
