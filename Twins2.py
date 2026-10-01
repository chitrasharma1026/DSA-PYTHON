n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

total = sum(a)
my_sum = 0
count = 0

for coin in a:
    my_sum += coin
    count += 1
    
    if my_sum > total - my_sum:
        break
print(count)
    