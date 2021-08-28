ch=1
files=[0]*100
while ch:
    s=int(input('starting indx of file '))
    len1=int(input('length of file '))
    
    count=0
    while count!=len1 and s<len(files):
        if files[s]==0:
            files[s]=1
            print(s,'->',1)
            count+=1


        s+=1

    ch=int(input())
    


