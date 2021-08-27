print("\n\tMemory Management Scheme - First Fit")
blocksize=list(map(int,input("Enter the block sizes :").split()))
processsize=list(map(int,input("Enter the Process Sizes : ").split()))
nb=len(blocksize)
np=len(processsize)
allocation=[-1]*np
for i in range(np):
    for j in range(nb):
        if(blocksize[j]>=processsize[i]):
           allocation[i]=j
           blocksize[j]-=processsize[i]
           break
print("Process_no.\tProcess_Size\tBlock_no")
for i in range(np):
    print(i+1,"\t\t",processsize[i],"\t\t",end=" ")
    if(allocation[i]!=-1):
        print(allocation[i]+1)
    else:
        print("Not allocated.")
