import os
import psutil
tot_m, used_m, free_m = map(int, os.popen('free -t -g').readlines()[-1].split()[1:])
cpup = psutil.cpu_percent()
print "Used Memory:", used_m,"GB | ","Available Mem:", free_m,"GB | ", "CPU %:" cpup,"%"
