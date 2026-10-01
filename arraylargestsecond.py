arr = [10, 2, 7, 8, 4]
largest= float('-inf')
second = float('-inf')
for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x
        print("Largest =", largest)
        print("Second Largest =", second)
        
