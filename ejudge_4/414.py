from datetime import datetime, timedelta

def parse(dt_str):
    date_p, tz_p = dt_str.split()
    date = datetime.strptime(date_p, "%Y-%m-%d")

    sign = 1 if tz_p[3] == "+" else -1
    hours = int(tz_p[4:6])
    minutes = int(tz_p[7:9])

    offset = timedelta(hours=hours, minutes=minutes) * sign

    return date - offset

t1 = parse(input().strip())
t2 = parse(input().strip())

days = int(abs((t2 - t1).total_seconds()) // 86400)
print(days)
