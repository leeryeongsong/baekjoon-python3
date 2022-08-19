import sys
t = int(input())
for _ in range(t):
    string = sys.stdin.readline()
    cnt = 0
    p = False
    for i in string:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            p = True
            print("NO")
            break
    if cnt == 0:
        print("YES") 
    elif p == False:
        print("NO")   