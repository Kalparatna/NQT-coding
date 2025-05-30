arr = list(map(int, input().split()))

min_val = arr[0]
for i in arr:
    if min_val >= i:
        min_val = i

print(min_val)

#or
arr = list(map(int, input().split()))     #efficient
print(min(arr))


#or 
arr = list(map(int, input().split()))
print(sorted(arr)[0])
