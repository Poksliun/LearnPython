from math import *
tasks = 2500
proc = 25
pot_thr = 10
perc = ceil(tasks/proc)
if perc>=proc :
    perc = proc
stt = []
remain = tasks
while remain > 0:
    pr = min(remain, proc)
    stt.append(pr)
    remain -= pr
if sum(stt) == tasks and len(stt) == perc:
    print(stt)
    print("Num of processes: ", len(stt))
else:
    print("Too much tasks")
