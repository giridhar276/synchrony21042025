

import psutil

## cpu percent
print(psutil.cpu_percent())
# memory 
print(psutil.swap_memory())
print(psutil.virtual_memory())
# hard disk related
print(psutil.disk_partitions())
print(psutil.disk_usage("/"))    # mac
#print(psutil.disk_usage("C://")) # windows