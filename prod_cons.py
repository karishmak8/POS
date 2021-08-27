k=int(input("size"))
mutex=1
full=0
empty=k
x=0
def wait(s):
    s-=1
    return s
def signal(s):
    s+=1
    return s 

def producer():
    global mutex,full,empty,x
    mutex=wait(mutex)
    full=signal(full)
    empty=wait(empty)
    x+=1
    print("\nProducer produces the item",x)
    mutex=signal(mutex)


def consumer():
    global mutex,full,empty,x
    mutex=wait(mutex)
    full=wait(full)
    empty=signal(empty)
    print("\nProducer consumes the item",x)
    x-=1

    mutex=signal(mutex)
    

print("\n1.Producer\n2.Consumer\n3.Exit")
while(1):
    ch=int(input("choice"))
    if ch==1:
        if ((mutex==1) and (empty!=0)):
            producer()
        else:
            print("buffer is full!cant produce")
    elif ch==2:
        if((mutex==1) and (full!=0)):
            consumer()
        else:
            print("buffer is empty !cant consume")
    elif ch==3:
        exit(0)
    
    else:
        print("enter proper choice")
    
