import sys

input=sys.stdin.readline

n = int(input())
stack = []
str = ""


def push(x):
    stack.append(x)
def stack_pop():
    if stack == []:
        print(-1)
    else:
        x = stack.pop()
        print(x)
def size():
    print(len(stack))
def empty():
    if stack == []:
        print(1)
    else:
        print(0)
def top():
    if stack == []:
        print(-1)
    else:
        x = stack[-1]
        print(x)

for _ in range(n):
    str = input().strip()
    if str[:4] == "push":
        push(int(str[4:]))
    elif str == "pop":
        stack_pop()
    elif str == "size":
        size()
    elif str == "empty":
        empty()
    elif str == "top":
        top()