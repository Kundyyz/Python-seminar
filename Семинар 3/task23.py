arr = [0, -1, 5, 2, 3]
count= 0
for i in range(len(arr)):
    if arr[i-1] < arr[i]:
        count += 1
        print(f"{arr[i-1]} < {arr[i]}")
print(count)    