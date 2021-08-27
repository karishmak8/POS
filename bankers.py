n = int(input("Enter no.of processes : "))
m=int(input("enter no:of resources:"))
Alloc= [ ]
Max=[]
Avail=[]
Need=[]
pro=[0]*n
pr=[]
for i in range(0,n):
	A=[]
	for i in range(0,m):
	   	ele = int(input("alloc: "))
	   	A.append(ele)
	Alloc.append(A)
for i in range(0,n):
	A=[]
	for i in range(0,m):
	   	ele = int(input("max: "))
	   	A.append(ele)
	Max.append(A)
A=[]
for i in range(0,m):
	ele=int(input("avail: "))
	A.append(ele)
Avail.append(A)
for i in range(0,n):
	A=[]
	for j in range(0,m):
	   	ele=Max[i][j]-Alloc[i][j]
	   	A.append(ele)
	Need.append(A)
p=0
for i in range(0,n):
			for i in range(0,n):
				if(pro[i]==0):
					count=0
					q=0
					for j in range(0,m):
						if(Need[i][j]<=Avail[p][q]):
							count=count+1
						q=q+1
					if(count==3):
						A=[]
						q=0
						for k in range(0,m):
							A.append(Avail[p][q]+Alloc[i][k])
							q=q+1
						Avail.append(A)
						p=p+1
						pro[i]=1
						pr.append("p"+str(i))		
print("Alloc:",Alloc)
print("Max:",Max)
print("Avail:",Avail)
print("Need:",Need)
print("safe sequence:",pr)