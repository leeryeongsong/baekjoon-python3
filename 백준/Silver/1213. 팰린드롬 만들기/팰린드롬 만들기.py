str = input()
word = {}
key_list = []
cnt = 0
answer = ""
odd = ""

for i in str:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1
        key_list.append(i)

key_list.sort()

for i in key_list:
    if word[i] % 2 != 0:
        cnt += 1
        odd = i
        answer += i * ((word[i] - 1) // 2)
    else:
        answer += i * (word[i] // 2)

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    answer = answer + odd + answer[::-1]
    print(answer)