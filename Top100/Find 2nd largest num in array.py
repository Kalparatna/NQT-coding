arr = list(map(int, input().split()))

unique_vals = list(set(arr))  # remove duplicates
if len(unique_vals) < 2:
    print("No second largest element")
else:
    unique_vals.sort()
    print(unique_vals[-2])





#Or : Best One
arr = list(map(int, input().split()))

first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

if second == float('-inf'):
    print("No second largest element")
else:
    print(second)




#or
arr = list(map(int, input().split()))

max_val = max(arr)
filtered = [x for x in arr if x != max_val]

if filtered:
    print(max(filtered))  
else:
    print("No second largest element")

