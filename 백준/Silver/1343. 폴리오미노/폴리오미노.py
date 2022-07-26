n = input()
tem = ""
cnt = 0
ans = ""

for i in range(len(n)):
    if n[i] == 'X':
        tem += 'X'
    if n[i] == '.' or i == len(n) - 1:
        t = len(tem)
        if t % 2 == 1:
            ans = "-1"
            break
        ans += 'AAAA' * (t // 4)
        ans += 'BB' * ((t % 4) // 2)
        if n[i] == '.':
            ans += '.'
        tem = ""

print(ans)