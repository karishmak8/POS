arr = list(map(int, input().split()))
head = int(input())
prev = head
sum = 0

for i in arr:
    if i>prev:
        sum += i-prev
    else:
        sum+= prev-i
    prev = i

print("Seek Sequence ", [head]+arr)
print(sum)

        