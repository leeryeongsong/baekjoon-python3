s = input()
num_str = ''
num = 0
sum = 0
is_minus = False

for i in s:
    if i != '-' and i != '+':
        num_str += i
    else:
        num = int(num_str)
        num_str = ''
        if is_minus == True:
            sum -= num
        else:
            sum += num

    if i == '-':
        if is_minus == False:
            is_minus = True

num = int(num_str)
if is_minus == True:
    sum -= num
else:
    sum += num


print(sum)