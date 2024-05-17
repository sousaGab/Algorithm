import random
arr = []
for x in range(10):
    arr.append(random.randint(1, 100))
sz = len(arr)-1

print('unsorted array:')
print(arr)

for i in range(sz):
    for j in range(sz-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print('sorted array:')
print(arr)
