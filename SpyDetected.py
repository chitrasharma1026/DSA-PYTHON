t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    if nums[0] == nums[1]:
        common = nums[0]
    elif nums[0] == nums[2]:
        common = nums[0]
    else:
        common = nums[1]

    for i in range(n):
        if nums[i] != common:
            print(i + 1)
            break