arr = list(map(int, input().split()))
head = int(input())
dir = input()
prev = head
sum = 0

L = []
R= []

for i in arr:
    if i>head:
        R.append(i)
    else:
        L.append(i)

R.sort()
L.sort()

if dir=="right":
    r = 199-head
    l = max(L)-0
    print(R+L)
    print(l+r+199)

elif dir=='left':
    l = head-0
    r = 199-min(R)

    R.sort(reverse=True)
    L.sort(reverse=True)

    print(L+R)
    print(l+r+199)