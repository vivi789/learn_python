import psutil
from psutil._common import bytes2human
import socket

"""HEADER"""
print("🩺 HEALTH CHECK 🩺")
print("-----------------------------------")

"""Checking Hostname"""
print(f"Hostname: {socket.gethostname()}")

"""Checking CPU Usage"""
percent_cpu = float(psutil.cpu_percent(1))
if percent_cpu > 90:
    print("CPU Status: CRITICAL")
    print(f"Load Avg: {psutil.getloadavg()}")
elif percent_cpu >80:
    print("CPU Staus: Warning")
    print(f"Load Avg: {psutil.getloadavg()}")
else:
    print("CPU Status: OK")
    print(f"Load Avg: {psutil.getloadavg()}")


"""Checking Memory Usage"""
mem = psutil.virtual_memory()

def caculate_mem(percent_mem,used_mem):
    if percent_mem > 90:
        print(f"Memory Status: CRITICAL - Used Memory: {bytes2human(used_mem)} GB")
    elif percent_mem > 80:
        print(f"Memory Status: WARNING - Used Memory: {bytes2human(used_mem)} GB")
    else:
        print(f"Memory Status: OK - Used Memory: {bytes2human(used_mem)} GB")

caculate_mem(used_mem=mem.used,percent_mem=mem.percent)

"""Checking Swap Usage"""

swap = psutil.swap_memory()
def caculate_swap(percent_swap=0,used_swap=0):
    if percent_swap > 90:
        print(f"Swap Status: CRITICAL - Used Swap: {bytes2human(used_swap)}")
    elif percent_swap > 80:
        print(f"Swap Status: WARNING - Used Swap: {bytes2human(used_swap)}")
    else:
        print(f"Swap status: OK - Used Swap: {bytes2human(used_swap)}")

caculate_swap(percent_swap=swap.percent,used_swap=swap.used)

"""Cheking disk usge"""

#print(psutil.disk_partitions())
#print(psutil.disk_usage('C:\\').used)

for part in psutil.disk_partitions(all=False):
    percent_part = psutil.disk_usage(part.mountpoint).percent
    print("Status Disk Usage")
    print(f"Mountpoint: {part.mountpoint}" , end='\t\t')
    print(f"Percent: {percent_part} %", end='\t\t')
    if percent_part > 90:
        print("Status: CRITICAL")
    elif percent_part > 80:
        print("Status: WARNING")
    else:
        print("Status: OK")