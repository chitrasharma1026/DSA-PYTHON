arr = [3, 5, 6, 7, 9, 10]
minimum = arr[0]
maximum = arr[0]
for i in range(len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]
print("Minimum =", minimum)
print("Maximum =", maximum)
    