# -datetime
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print(now)
print(now.time())
print(type(now))

# 获取指定日期和时间
now = datetime(2017, 11, 13, 14, 50)
print(now)
now = datetime(2017, 11, 13, 14, 50, 29, 999999)  # microsecond must be in 0..999999
print(now)

# datetime转换为timestamp[小数位为毫秒数 | timestamp与时区无关,故建议存储为时间戳]
timestamp = now.timestamp()
print(timestamp)

# timestamp转换为datetime
now = datetime.fromtimestamp(1301279292.5)
print(now)
# timestamp直接被转换到UTC标准时区的时间
now = datetime.utcfromtimestamp(1301279292.5)
print(now)

# str转换为datetime[无时区]
now = datetime.strptime('2017-11-13 15:01:27', '%Y-%m-%d %H:%M:%S')
print(now)

# datetime转str
r = now.strftime('%a, %b, %d %H:%M')
print('datetime转str的结果：', r)

from datetime import timedelta

# datetime加减
now += timedelta(days=2, hours=2, minutes=2, seconds=2, milliseconds=222)
print(now)

from datetime import timezone

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 转换为东八时区
utc_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(utc_dt)

# today
print('today:', datetime.today())

# ---
# n = datetime.fromtimestamp(1301279292.5)
t = datetime.fromtimestamp(1585825278)
print('t', t)
