# https://www.acmicpc.net/problem/9654
# https://dongdongfather.tistory.com/67 # [파이썬 기초] PRINT() 함수에서 %와 FORMAT()를 사용하여 서식에 맞게 출력(1)

list = [["SHIP NAME","CLASS","DEPLOYMENT","IN SERVICE"],["N2 Bomber","Heavy Fighter","Limited","21"],["J-Type 327","Light Combat","Unlimited","1"],["NX Cruiser","Medium Fighter","Limited","18"],["N1 Starfighter","Medium Fighter","Unlimited","25"],["Royal Cruiser","Light Combat","Limited","4"]]
for i in range(6):
    print("{:15}{:15}{:11}{:10}".format(list[i][0],list[i][1], list[i][2], list[i][3]))
