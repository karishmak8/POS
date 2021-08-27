def wait(s):
  s-=1
  return s
def signal(s):
  s+=1
  return s
def Philosopher():
	global n
	global C
	for i in range(0,n):
		if(C[i]==1 and C[(i+1)%n]==1):
			C[i]=wait(C[i])
	i=n-1
	while(C[0]!=1):
		if(C[i]==1):
			C[i]=wait(C[i])
		for j in range(0,5):
			if(j==i-1):
				print("philosopher p"+str(i-1)+" is eating")
			else:
				print("philosopher p"+str(j)+" is waiting")
		C[i]=signal(C[i])
		C[(i-1)%5]=signal(C[(i-1)%5])
		i=i-1
		print("\n")
	print("philosopher p"+str(4)+" dies because of starvation")


n=5
C=[1,1,1,1,1]
print("all philosophers are in thinking state")
print("\n")
Philosopher()