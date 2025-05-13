'''
Problem Statement: Making Triplets Equal
You are given a triplet of integers (a,b,c). You can perform the following operation any
number of times:
1. Select any two numbers from the triplet.
2. Add 1 to both selected numbers.
3. Subtract 1 from the remaining number.
Your task is to determine whether it is possible to make all three numbers equal using the
given operations.
Input:
. A single integer T representing the number of test cases.
. Each test case consists of three integers a,b,c.
Output:
. For each test case, print "YES" if it is possible to make all three numbers equal; otherwise,
print "NO".
Constraints:
1<T≤10^4
-10^9 ≤ a, b, c ≤ 10^9

Example:
Input:
3
1 2 3
4 4 4 
3 3 7
Output:
-1
0
2

'''

def min_steps_to_equal(P, Q, R):
    arr = [P, Q, R]
    arr.sort()

    if arr[0] == arr[1] == arr[2]:
        return 0

    steps = 0
    while True:
        arr[0] += 1
        arr[1] += 1
        arr[2] -= 1
        steps += 1
        arr.sort()

        if arr[0] == arr[1] == arr[2]:
            return steps

        if (arr[0] == arr[1] and arr[1] + 1 == arr[2]) or \
           (arr[1] == arr[2] and arr[0] + 1 == arr[1]):
            return -1

T = int(input())  
for _ in range(T):
    res = 0
    P, Q, R = map(int, input().split())
    print(min_steps_to_equal(P, Q, R))
        