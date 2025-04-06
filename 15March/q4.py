'''
Question:
You are given a list of integers of length N. Every element in the list appears exactly two times,
except for one unique element, which appears exactly once. Your task is to find and print this
unique element.
Input Format:
The first line contains an integer N, the length of the list.
The second line contains N space-separated integers representing the elements of the list.
Output Format:
Print the unique element that appears exactly once.
Constraints:
Example 1:
📌 Input:
9
1 1 2 2 5 6 6 7 7
📌 Output:
5
Example 2:
📌 Input:
7
3 3 4 4 9 2 2
📌 Output:
9

'''

n = int(input())

nums = list(map(int,input().split()))

print(sum(nums)- sum(set(nums)))

#Or
n = int(input())
nums = list(map(int,input().split()))
result = 0
for num in nums:
    result ^= num
print(result)