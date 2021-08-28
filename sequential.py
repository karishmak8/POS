files=[0]*100
ch=1
while ch:
    s=int(input('enter starting point '))
    l=int(input('enter length '))
    for i in range(s,s+l):
        if files[i]==0:
            print(i,'->',1)
            files[i]=1
        else:
            print('cant allocate ')
            break
    ch=int(input())
    