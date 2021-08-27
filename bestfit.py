print("\n\tMemory Management Scheme - Worst Fit")
blocksize=list(map(int,input("Enter the block sizes :").split()))
processsize=list(map(int,input("Enter the Process Sizes : ").split()))
nb=len(blocksize)
np=len(processsize)
allocation=[-1]*np
for i in range(np):
    wst=-1
    for j in range(nb):
        if(blocksize[j]>=processsize[i]):
            if(wst==-1):
               wst=j
            elif(blocksize[wst]<blocksize[j]):
               wst=j
    if(wst!=-1):
        allocation[i]=wst
        blocksize[wst]-=processsize[i]
print("Process_no.\tProcess_Size\tBlock_no")
for i in range(np):
    print(i+1,"\t\t",processsize[i],"\t\t",end=" ")
    if(allocation[i]!=-1):
        print(allocation[i]+1)
    else:
        print("Not allocated.")
