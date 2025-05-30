arr = list(map(int, input().split()))

max_val = arr[0]
for i in arr:
    if max_val < i:
        max_val = i

print(max_val)

#or
arr = list(map(int, input().split()))   
print(max(arr))


#or 
arr = list(map(int, input().split()))
print(sorted(arr)[-1])
