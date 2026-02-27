from datetime import datetime, timedelta
import calendar
import math

def parse_to_utc(dt_str):
    date_p, u_p = dt_str.split()
    date = datetime.strptime(date_p, "%Y-%m-%d")
    
    sign = 1 if u_p[3] == "+" else -1
    hours = int(u_p[4:6])
    minutes = int(u_p[7:9])

    offset = timedelta(hours=hours, minutes=minutes) * sign
    return date - offset

def build_dr_utc(year, dr_month, dr_day, dr_offset):
    if dr_month == 2 and dr_day == 29 and not calendar.isleap(year):
        dr_day = 28
    
    dr_local = datetime(year, dr_month, dr_day, 0, 0, 0)
    dr_utc = dr_local - dr_offset
    return dr_utc

birth_str = input().strip()
current_str = input().strip()

current_utc = parse_to_utc(current_str)

date_p, u_p = birth_str.split()
_, dr_month, dr_day = map(int, date_p.split("-"))

sign = 1 if u_p[3] == "+" else -1
hours = int(u_p[4:6])
minutes = int(u_p[7:9])
dr_offset = timedelta(hours=hours, minutes=minutes) * sign

year = current_utc.year
dr_utc = build_dr_utc(year, dr_month, dr_day, dr_offset)

if dr_utc < current_utc:
    dr_utc = build_dr_utc(year+1, dr_month, dr_day, dr_offset)

delta_seconds = (dr_utc - current_utc).total_seconds()

if delta_seconds<0:
    print(0)
else:
    print(math.ceil(delta_seconds/86400))