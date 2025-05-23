'''
Problem Description -: Given an array Arr[ ] of N integers and a positive integer K. The task is to cyclically rotate the array clockwise by K.

Note : Keep the first of the array unaltered. 

Example 1:

5  —Value of N
{10, 20, 30, 40, 50}  —Element of Arr[ ]
2  —–Value of K
Output :

40 50 10 20 30

Example 2:

4  —Value of N
{10, 20, 30, 40}  —Element of Arr[]
1  —–Value of K
Output :

40 10 20 30
'''
N = int(input())
Array = list(map(int, input().split()))
K =  int(input())

K = K % N
before = Array[:-K]    #-K: Last K element
after = Array[-K:]    #-K: From Kth element from last
Array = after + before
print(Array)