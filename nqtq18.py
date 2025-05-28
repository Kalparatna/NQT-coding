'''
Given two positive integers N and X, where N is the number of total patients and X is the time duration(in minutes) 
after which a new patient arrives. Also, doctor will give only 10 minutes to each patient. The task is to calculate the 
time (in minutes) the last patient needs to wait.

Input:

The input denote the total number of patients N and time interval X(in minutes) in which the next patients are visiting.

Output:

Output the waiting time of last patient

Public test cases

Input 4 5

Output 15

Input 5 3

Output 28
'''

N,X = map(int, input().split())

arrival_of_last = (N-1) * X
appointent_of_last = (N-1) * 10
waiting_of_last = appointent_of_last - arrival_of_last

print(waiting_of_last)
