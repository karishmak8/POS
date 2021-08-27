ms=int(input("Enter the memory size: "))
ps=int(input("Enter the page size : "))
nop=(ms/ps)
print("The no. of pages available in memory are : ",nop)
np=int(input("Enter the no. of processes : "))
rempages=nop
s=[0 for i in range(10)]
fno=[[0 for i in range(10)] for j in range(20)]
for i in range(1,np+1):
    s[i]=int(input(f"Enter the no. of pages required for p[{i}] : "))
    if(s[i]>rempages):
        print("Memoey is Full")
        break
    rempages=rempages-s[i]
    print(f"Enter page table for p[{i}]")
    for j in range(s[i]):
        fno[i][j]=int(input())
print("Enter Logical address to find physical address : ")
x=int(input("Enter process no. : "))
y=int(input("Enter the page no. : "))
offset=int(input("Enter the offset : "))
if(x>np or y>=s[i] or offset>=ps):
    print("Invalid process or page no. or offset")
else:
    pa=fno[x][y]*ps+offset
    print("The physical Address is : ",pa)
