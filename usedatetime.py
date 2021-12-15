from datetime import datetime, timedelta, timezone
import re

# dt = datetime(2015,4,19,12,20)

# print(datetime.fromtimestamp(dt.timestamp()))
# print(datetime.utcfromtimestamp(dt.timestamp()))

# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)

# print(dt.strftime('%a, %b %d %H:%M'))

# now = datetime.now()
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))

# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()
# dt = now.replace(tzinfo=tz_utc_8)
# print(now, '\n', dt)

# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)

# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)

# tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)

def to_timestamp(dt_str, tz_str):
    tz = int(re.match(r'^UTC([+|-]\d+)\:\d+$', tz_str).group(1))
    dt_utc = timezone(timedelta(hours=tz))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=dt_utc)
    return dt.timestamp()
    
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')    