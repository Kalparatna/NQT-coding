'''
Problem Statement:-

Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number 
greater than b by interchanging the digits of a and if not possible print -1.

Input Format
2 numbers a and b, separated by space.
Output Format
A single number greater than b.
If not possible, print -1

Constraints
1 <= a,b <= 10000000

Example 1:

Sample Input:

    459 500

Sample Output:
    549

Example 2:

Sample Input:

    645757 457765

Sample Output:
    465577

'''
from itertools import permutations

a, b = map(int, input().split())

p = list(permutations(str(a)))

array = ["".join(perm) for perm in p]

sorted_arr = sorted(array)
for i in sorted_arr:
    if int(i) > b:
        print(i)
        break

