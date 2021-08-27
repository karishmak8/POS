n = int(input("Enter no. of processes: "))
process = list(map(str, input("Process:").split()))
Bt = list(map(int, input("Burst time: ").split()))
pri =list(map(int, input("Priority: ").split()))
Qpri =list(map(int, input("Queue Priority: ").split()))

#assuming arrival for all processes is 0
#Q1 = Priority, non preemptive
#Q2 = SJF, non preemptive
gc = []
ct = [0]*n
wt = [0]*n
tat = [0]*n
rt = [0]*n
val = 0
hold = [] 

for i in range(n):
    ind = pri.index(min(pri)) 

    if Qpri[ind]!= min(Qpri):
        hold.append(ind)
    else:
        gc = gc + [(process[ind])]
        ct[ind] = val + Bt[ind]
        tat[ind] = ct[ind]-0 #At[ind]
        wt[ind] = tat[ind]-Bt[ind]
        rt[ind] = val- 0 #At[ind]
        val += Bt[ind]
    pri[ind]=99999

for i in hold:
    gc = gc + [(process[i])]
    ct[i] = val + Bt[i]
    tat[i] = ct[i]-0 # At[ind]
    wt[i] = tat[i]-Bt[i]
    rt[i] = val- 0 #At[ind]
    val += Bt[i]

print("Processes       :", process)
print("Completion time :",ct)
print("Turn Around time:",tat)
print("Waiting time    :",wt)
print("Response time   :",rt)
print("Gantt Chart     :",gc)
print("Avg Turn Around Time:", round(sum(tat)/n,2))
print("Avg Wating Time     :", round(sum(wt)/n,2))


# Burst time: 4 9 4 7 6 
# Priority: 2 1 2 1 1      
# Queue Priority: 1 1 2 2 1