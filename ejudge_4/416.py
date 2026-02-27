from datetime import datetime, timedelta

def parse(s):
    date_p, time_p, tz_p = s.split()

    local_dt = datetime.strptime(
        date_p + " " + time_p,
        "%Y-%m-%d %H:%M:%S"
    )

    sign = 1 if tz_p[3] == "+" else -1
    hours = int(tz_p[4:6])
    minutes = int(tz_p[7:9])

    offset = timedelta(hours=hours, minutes=minutes) *sign
    return local_dt - offset

start_utc = parse(input().strip())
end_utc = parse(input().strip())

duration = int((end_utc - start_utc).total_seconds())
print(duration)