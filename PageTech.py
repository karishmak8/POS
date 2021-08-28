mem=int(input("enter memory size"))
page_Size=int(input("Enter the page size"))
num_pages=int(input("no. of pages available in memory are"))
p=int(input("Enter number of processes "))
sum1=0 
li=[]
for i in range(p):
    num=int(input("num of pages for p{}".format(i)))
    sum1+=num
    if sum1<=num_pages:
        li.append(list(map(int,input().split())))
    else:
        sum1-=num
        print("mem full")
        


print("\nEnter Logical Address to find Physical Address")

pno=int(input("process no."))
pagenum=int(input("page num "))
offset=int(input("offset "))

if(pno<p and pagenum<num_pages and offset<page_Size):
    print(li[pno-1][pagenum-1]*page_Size+offset)