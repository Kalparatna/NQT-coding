'''
Shift – 2 

Question 1: Tower of Hanoi - Print Only Number of Steps
Problem Statement:
Given the number of disks n, print the total number of moves required to solve the Tower of Hanoi problem. You do not need to print the
actual steps, just the number of steps.

Formula:
The number of steps required to solve Tower of Hanoi with n disks is:
steps = 2n - 1
Test Case 1:
Input:
1
Output:
1
Explanation:
21 - 1 = 1 move

Test Case 2:
Input:
2
Output:
3
Explanation:
22 - 1 = 3 moves


'''

n = int(input())
print((2**n)-1)