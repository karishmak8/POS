arr = list(map(int, input().split()))
head = int(input())
dir = input()
max1 = max(arr)
min1 = min(arr)

print(head)

L = []
R= []

for i in arr:
    if i>head:
        R.append(i)
    else:
        L.append(i)

R.sort()
L.sort(reverse=True)

if dir=="right":
    r = 199-head
    l = 199-min1
    print(R+L)
    print(l+r)

elif dir=='left':
    l = head-0
    r = max1-0
    print(L+R)
    print(l+r)