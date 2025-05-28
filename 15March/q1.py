'''
Problem Statement: Range Sum Query
You are given two integers i and j, where Osi<js9999. Your task is to compute the sum of all
integers from index i to j, inclusive.
Input Format:
. A single integer T representing the number of queries.
. Each of the next T lines contains two integers i and j (Osi<j≤9999)
Output Format:
. For each query, print a single integer representing the sum of numbers from i to j.
Constraints:

1<T≤104
0≤i<j ≤9999

Example Input:
3
0 3
2 6 
10 20
Example Output:
6 20 invalid input i&j i <= j<10000
Explanation:
1. Sum from 0 to 3: 0+1+2+3=6
2. Sum from 2 to 6: 2+3+4+5+6=20
3. Sum from 10 to 20: 10+11+ ... +20=165

'''
def rangesum(i, j):
    if i <= j<10000:     
        res = 0
        for num in range(i, j+1):
            res += num
        return res
    else:
        return "invalid input i&j i <= j<10000"

T = int(input())
for i in range(T):
    i, j =  map(int, input().split())
    print(rangesum(i, j))


#without using loop
def sumrange(i, j):
    if i <= j < 10000:
        return ((j - i + 1) * (i + j)) // 2
    else:
        return "invalid input i&j i <= j<10000"

T = int(input())
for _ in range(T):
    i, j = map(int, input().split())
    print(sumrange(i, j))

    
