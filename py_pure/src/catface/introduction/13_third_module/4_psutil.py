# -psutil[获取系统信息]
import psutil

# 1. 获取CPU信息
print('cpu_count-->', psutil.cpu_count())
print('cpu_freq-->', psutil.cpu_freq())
print('cpu_percent-->', psutil.cpu_percent())
print('cpu_stats-->', psutil.cpu_stats())
print('cpu_times-->', psutil.cpu_times())

# 2. 实现类似top命令的CPU使用率
for x in range(2):
    r = psutil.cpu_percent(interval=1, percpu=True)
    print(r)

# 3. 获取内存信息
print('virtual_memory-->', psutil.virtual_memory())
print('swap_memory-->', psutil.swap_memory())

# 4. 获取磁盘信息
print('disk_partitions-->', psutil.disk_partitions())
print('disk_usage-->', psutil.disk_usage('/'))
print('disk_io_counters-->', psutil.disk_io_counters())

# 5. 获取网络信息
print('net_io_counters-->', psutil.net_io_counters())  # 获取网络读写字节／包的个数
print('net_if_addrs-->', psutil.net_if_addrs())  # 获取网络接口信息
print('net_if_stats-->', psutil.net_if_stats())  # 获取网络接口状态
print('net_connections-->', psutil.net_connections())  # 获取当前网络连接信息

# 6. 获取进程信息
print('pids-->', psutil.pids())
print('test-->', psutil.test())
