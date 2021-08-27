def first_fit(p,mem_required,block_size):
    frag=block_size.copy()
    for i in range(len(p)):
        for j in range(len(block_size)):
            if(mem_required[i]<=block_size[j]):
                frag[j]=block_size[j]-mem_required[i]
                print(p[i],"\t\t  ",mem_required[i],"\t\t   ",j+1,"\t\t    ",block_size[j],)
                block_size[j]-=mem_required[i]
                break
    print(frag)
            


def best_fit(p,mem_required,block_size):
    for i in range(len(p)):
        for j in range(len(block_size)):
            li=[]
            for k in range(len(block_size)):
                if mem_required[i]<=block_size[k]:
                    li.append([block_size[k],k])
            if li==[]:
                return 
            
            li.sort()
            print(p[i],"\t\t  ",mem_required[i],"\t\t  ",li[0][0],"\t\t  ",li[0][1]+1,"\t\t  ",li[0][0]-mem_required[i])
            block_size[li[0][1]]=0
            break



def worst_fit(p,mem_required,block_size):
    for i in range(len(p)):
        for j in range(len(block_size)):
            li=[]
            for k in range(len(block_size)):
                if mem_required[i]<=block_size[k]:
                    li.append([block_size[k],k])
            if li==[]: 
                print("other processors cant be allocated")
                return 
            
            li.sort()
            print(p[i],"\t\t  ",mem_required[i],"\t\t  ",li[len(li)-1][0],"\t\t  ",li[len(li)-1][1]+1,"\t\t  ",li[len(li)-1][0]-mem_required[i])
            block_size[li[len(li)-1][1]]=0
            break


p=list(map(str,input('enter processors :').split()))
mem_required=list(map(int,input('memory required:').split()))
block_size=list(map(int,input('blocks size ').split()))
ch=int(input('1-->first fit \n2-->best fit \n3-->worst fit\n'))
if ch==1:
    print("processor\tmemory_req\tblock_number\tblock_size")
    first_fit(p,mem_required,block_size)
elif ch==2:
    print("processor\tmemory required\tblock_number\tblock_size\tmemory wasted")
    best_fit(p,mem_required,block_size)
elif ch==3:
    print("processor\tmemory required\tblock_number\tblock_size\tmemory wasted")
    worst_fit(p,mem_required,block_size)




'''

p1 p2 p3
1 4 7
5 8 4 10
1

p1 p2 p3
1 4 7
5 8 4 10
2



p1 p2 p3
1 4 7
5 8 4 10
3

'''


'''
#ACTUAL
def first_fit(p,mem_required,block_size):
    frag=block_size.copy()
    for i in range(len(p)):
        for j in range(len(block_size)):
            if(mem_required[i]<=block_size[j]):
                frag[j]=block_size[j]-mem_required[i]
                print(p[i],"\t\t  ",mem_required[i],"\t\t   ",j+1,"\t\t    ",block_size[j],)
                block_size[j]-=mem_required[i]
                break
    print(frag)
            


def best_fit(p,mem_required,block_size):
    for i in range(len(p)):
        for j in range(len(block_size)):
            li=[]
            for k in range(len(block_size)):
                if mem_required[i]<=block_size[k]:
                    li.append([block_size[k],k])
            if li==[]:
                return 
            
            li.sort()
            print(p[i],"\t\t  ",mem_required[i],"\t\t  ",li[0][0],"\t\t  ",li[0][1]+1,"\t\t  ",li[0][0]-mem_required[i])
            block_size[li[0][1]]=0
            break



def worst_fit(p,mem_required,block_size):
    for i in range(len(p)):
        for j in range(len(block_size)):
            li=[]
            for k in range(len(block_size)):
                if mem_required[i]<=block_size[k]:
                    li.append([block_size[k],k])
            if li==[]: 
                print("other processors cant be allocated")
                return 
            
            li.sort()
            print(p[i],"\t\t  ",mem_required[i],"\t\t  ",li[len(li)-1][0],"\t\t  ",li[len(li)-1][1]+1,"\t\t  ",li[len(li)-1][0]-mem_required[i])
            block_size[li[len(li)-1][1]]=0
            break


p=list(map(str,input('enter processors :').split()))
mem_required=list(map(int,input('memory required:').split()))
block_size=list(map(int,input('blocks size ').split()))
ch=int(input('1-->first fit \n2-->best fit \n3-->worst fit\n'))
if ch==1:
    print("processor\tmemory_req\tblock_number\tblock_size")
    first_fit(p,mem_required,block_size)
elif ch==2:
    print("processor\tmemory required\tblock_size\tblock_number\tmemory wasted")
    best_fit(p,mem_required,block_size)
elif ch==3:
    print("processor\tmemory required\tblock_size\tblock_number\tmemory wasted")
    worst_fit(p,mem_required,block_size)




p1 p2 p3
1 4 7
5 8 4 10
1

p1 p2 p3
1 4 7
5 8 4 10
2



p1 p2 p3
1 4 7
5 8 4 10
3

'''