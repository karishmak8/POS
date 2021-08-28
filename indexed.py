ch=1
files=[0]*100
index=[0]*100
while ch:
    ind=int(input('enter the index '))
    if index[ind]==0:
        i=int(input('enter the number of files to be allocated '))
        alloc=list(map(int,input().split()))
        flag=0
        for i in alloc:
            if files[i]==0:
                files[i]=1
                
            else:
                flag=1
               
                break
        if flag==0:
            print("file allocation done")
            index[ind]=1
        else:
            print("cant allocate ")



    else:
        print("index is not free ")
    
    ch=int(input())