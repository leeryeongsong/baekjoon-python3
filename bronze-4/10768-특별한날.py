# https://www.acmicpc.net/problem/10768
# 월과 일을 한 줄에 하나씩 입력받아 저장한다.
month = int(input())
day = int(input())

# 2월 18일보다 입력받은 날이 빠르면, Before를 출력하고 2월 18일이면 Special을 출력, 2월 19일부터 After를 출력한다.
if month < 2 :
    print('Before')
elif month == 2 and day < 18:
    print('Before')
elif month == 2 and day == 18:
    print('Special')
else :
    print('After')
