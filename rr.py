n = int(input("Enter no. of processes: "))
process = list(map(str, input("Process: ").split()))
At = list(map(int, input("Arrival time: ").split()))
Bt = list(map(int, input("Burst time: ").split())) 
t = int(input("Time Quantum: "))
At1 = sorted(At)
Bt1 = Bt.copy()
gc = []
rQ = []
ct = [0]*n
wt = [0]*n
tat = [0]*n
rt = [0]*n
val = cnt = flg = i = 0
s = sum(Bt)
while (max(ct)!=s):
    while(i<len(At1) and cnt>=At1[i]):
        rQ.append(At1[i])
        i+=1

    if flg==1:
        rQ.append(At[x])
        
    x = At.index(rQ[0])
    if process[x] not in gc:
        rt[x] = val-At[x] 

    gc.append(process[x])
    rQ.remove(At[x])

    if Bt[x]<=t and Bt[x]!=0:
        ct[x] = Bt[x] + cnt
        tat[x] = ct[x]-At[x]
        wt[x] = tat[x]-Bt1[x]
        val += Bt[x]
        cnt += Bt[x]
        Bt[x]=0
        flg=0

    else:
        #flag to append incompleted processes
        Bt[x] = Bt[x]-t
        cnt+=t
        val = cnt
        flg=1           
        
print("Processes       :", process)
print("Completion time :",ct)
print("Turn Around time:",tat)
print("Waiting time    :",wt)
print("Response time   :",rt)
print("Gantt Chart     :",gc)
print("Avg Turn Around Time:", round(sum(tat)/n,3))
print("Avg Wating Time     :", round(sum(wt)/n,3))


# 5
# process p1 p2 p3 p4 p5
# 0 5 1 6 8
# 8 2 7 3 5
# time quantum = 3