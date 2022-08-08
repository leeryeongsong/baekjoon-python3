n = input()
ucpc = ["U", "C", "P", "C"]
s = ""
temp = 0
a = ""
for i in n:
    if i in ucpc:
        s += i
for i in s:
    if i == ucpc[temp]:
        a += i
        if temp == 3:
            break
        temp += 1
if a == "UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")