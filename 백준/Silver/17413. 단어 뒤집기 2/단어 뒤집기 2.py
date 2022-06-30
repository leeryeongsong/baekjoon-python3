raw = input()
ans = ""
tem = ""
tag = False

for i in raw:
    if i == "<":
        tag = True
        ans += tem[::-1]
        tem = ""
        tem += i
    elif i == ">":
        tag = False
        tem += i
        ans += tem
        tem = ""
    elif i == " " and tag == False:
        ans += tem[::-1] + " "
        tem = ""
    else:
        tem += i

if tem != "":
    ans += tem[::-1]

print(ans.lstrip())