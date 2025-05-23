'''
Question: Find Common Height Difference or Detect Invalid Input
Given the height of a tree for 4 consecutive weeks, calculate the difference between each week.
If any height is negative, return "Not valid inputs".
If any two weekly differences are the same, return that difference.
If all differences are different, return "None".

APPROACH
Step 1: Check if any height is negative. If so, return "Not valid inputs".
Step 2: Calculate the differences:

diff1 = height2 - height1
diff2 = height3 - height2
diff3 = height4 - height3
Step 3: If any two of the above differences are the same, return the common difference.
Step 4: If all differences are different, return "None".

Input:
Four integers representing the height of the tree in 4 consecutive weeks.
Example 1:

Input: 2, 4, 6, 7
Output: 2

4-2 =2
6-4=2

Explanation: Differences are 2, 2, and 1 -> 2 appears twice.

Example 2:

Input: 5, 10, 11, 13
Output: None
Explanation: Differences are 5, 1, and 2 - all different.

Example 3:

Input: -1, 3, 4, 5
Output: Not valid inputs
Explanation: Negative height is invalid.


'''
h = list(map(int, input().split()))

if any(i < 0 for i in h):
    print("Not valid inputs")
else:

    d1 = h[1] - h[0]
    d2 = h[2] - h[1]
    d3 = h[3] - h[2]

    if d1 == d2 == d3:
        print(d1)
    elif d1 == d2 or d1 == d3:
        print(d1)
    elif d2 == d3:
        print(d2)
    else:
        print("None")


#Or  where weeks sized is less or more than 4
heights = list(map(int, input().split()))

if any(num < 0 for num in heights):
    print("Not valid inputs")
else:
    diff1 = heights[1] - heights[0]
    diff2 = heights[2] - heights[1]
    diff3 = heights[3] - heights[2]

    differences = [diff1, diff2, diff3]

    comm_diff = None 
    for i in differences:
        if differences.count(i) > 1:
            comm_diff = i
            break

    if comm_diff is not None:
        print(comm_diff)
    else:
        print("None")

