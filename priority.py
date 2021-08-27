n = int(input("Enter no. of processes: "))
process = list(map(str, input("Process:").split()))
pri =list(map(int, input("Priority: ").split()))
At = list(map(int, input("Arrival time: ").split()))
Bt = list(map(int, input("Burst time: ").split()))
gc = []
ct = [0]*n
wt = [0]*n
tat = [0]*n
rt = [0]*n
val = 0
flag = 0
x = At.index(min(At))
for i in range(n):

    if At[x]>val:
         flag = 1
         x1 = x
         x2 = min(pri)
         pri[x1]=99999
         x = pri.index(min(pri))
         
    gc = gc + [(process[x])]
    ct[x] = val + Bt[x]
    tat[x] = ct[x]-At[x]
    wt[x] = tat[x]-Bt[x]
    rt[x] = val-At[x]
    val += Bt[x]
    pri[x]=99999 
    At[x]=99999
    x = pri.index(min(pri))
    if flag==1:
         x=x1
         pri[x1]=x2
         flag = 0
         
print("Processes       :", process)
print("Completion time :",ct)
print("Turn Around time:",tat)
print("Waiting time    :",wt)
print("Response time   :",rt)
print("Gantt Chart     :",gc)
print("Avg Turn Around Time:", round(sum(tat)/n,2))
print("Avg Wating Time     :", round(sum(wt)/n,2))




# 7
# process p1 p2 p3 p4 p5 p6 p7
# 3 4 4 5 2 6 1
# 0 1 3 4 5 6 10
# 8 2 4 1 6 5 1