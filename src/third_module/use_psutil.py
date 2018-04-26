# -*- coding: utf-8 -*-

import psutil

count = psutil.cpu_count()  # CPU逻辑数量

print('CPU逻辑数量: ', count)
count = psutil.cpu_count(logical=False)  # CPU物理核心
print('CPU物理核心: ', count)

cpu_times = psutil.cpu_times()
print('cputime: ', cpu_times)

print()
print('cpu使用频率,')
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

virtu_memory = psutil.virtual_memory()
print('   物理内存: ', virtu_memory)
swap_memory = psutil.swap_memory()
print('   交换内存: ', swap_memory)
