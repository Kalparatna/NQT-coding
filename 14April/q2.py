'''
Q2)Question: Standard Deviation of an Array

Problem Statement:
Write a program to calculate the standard deviation of a given array of integers.The formula for standard deviation is
Your program should:
Read an integer n representing the number of elements in the array.
Read n integers.
Calculate the mean of the array.
Use the mean to compute the standard deviation.
Print the standard deviation rounded to 2 decimal places.

Input Format:

First line: An integer n (number of elements)
Second line: n space-separated integers

Output Format:

A single line containing the standard deviation as a double with 2 decimal places.
'''

n = int(input())
nums = list(map(int, input().split()))
mean = sum(nums) / n

temp = 0
for i in range(n):
    temp += (nums[i] - mean) ** 2

variance = (temp / n)
sd = variance ** 0.5  
print(sd)
