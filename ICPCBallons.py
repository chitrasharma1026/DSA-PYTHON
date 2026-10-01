t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    solved = set()
    balloons = 0
    
    for ch in s:
        balloons += 1
        
        if ch not in solved:
            balloons += 1
            solved.add(ch)
            
    print(balloons)
    