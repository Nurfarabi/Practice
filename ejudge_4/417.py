import math

def find_segment(x1, y1, x2, y2, r):
    dx = x2 - x1
    dy = y2 - y1
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - r*r

    d = b*b - 4*a*c
    length = math.sqrt(a)

    if d < 0:
        if x1*x1 + y1*y1 <= r*r and x2*x2 + y2*y2 <= r*r:
            return length
        return 0.0
    
    sqrtd = math.sqrt(d)
    t1 = (-b - sqrtd)/(2*a)
    t2 = (-b + sqrtd)/(2*a)
    
    t_start = max(0.0, min(t1,t2))
    t_end = min(1.0, max(t1,t2))

    if t_start >= t_end:
        return 0.0
    return length * (t_end - t_start)

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
ans = find_segment(x1, y1, x2, y2, r)
print(f"{ans:.10f}")