p=0
total_Inter_frag=0
ms=int(input("Enter the total memory available : "))
bs=int(input("Enter the block size : "))
no_of_blocks=(int)(ms/bs)
ext_frag=ms-no_of_blocks*bs
n=int(input("Enter the no. of processes :"))
mp=list(map(int,input().split()))
print("No. of Blocks available in memory : ",no_of_blocks)
print("Process\t Mem_Req\t Mem_alloc\tInter_frag")
for i in range(n):
    if(p<no_of_blocks):
        print(i+1,"\t  ",mp[i],end="\t")
        if(mp[i]>bs):
            print("\tNo\t\t---",)
        else:
            print("\tYES\t\t",bs-mp[i])
            total_Inter_frag+=bs-mp[i]
            p+=1
    print("Memory is full ,Remaining process cannot be accomodated")
print("No. of processes which are not allocated are : ",n-p)
print("Total Internal Fragmentation is : ",total_Inter_frag)
print("Total External Fragmentation is : ",ext_frag)
