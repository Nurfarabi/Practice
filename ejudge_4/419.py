import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def dist(x, y):
    return math.hypot(x, y)

def dist2(x1, y1, x2, y2):
    return math.hypot(x2-x1, y2-y1)


def dist_point_to_segment():
    ABx = x2 - x1
    ABy = y2 - y1
    AOx = -x1
    AOy = -y1

    ab2 = ABx*ABx + ABy*ABy
    t = (AOx*ABx + AOy*ABy) / ab2

    if t < 0:
        return dist(x1, y1)
    if t > 1:
        return dist(x2, y2)

    px = x1 + t*ABx
    py = y1 + t*ABy
    return dist(px, py)

AB = dist2(x1, y1, x2, y2)
h = dist_point_to_segment()


if h >= R:
    print(f"{AB:.10f}")
    exit()


dA = dist(x1, y1)
dB = dist(x2, y2)

tA = math.sqrt(dA*dA - R*R)
tB = math.sqrt(dB*dB - R*R)

dot = x1*x2 + y1*y2
theta = math.acos(dot / (dA * dB))

alpha = math.acos(R / dA)
beta = math.acos(R / dB)

arc = R * (theta - alpha - beta)

print(f"{tA + tB + arc:.10f}")