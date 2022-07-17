doc = input()
word = input()

l = len(word)
index = 0
count = 0


while index < len(doc) - l + 1:
    if doc[index:index+l] == word:
        count += 1
        index += l
    else:
        index += 1


print(count)