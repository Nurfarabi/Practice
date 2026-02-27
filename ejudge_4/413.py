import json
import re

NOT_FOUND = object()  

def resolve(data, query):
    cur = data
    parts = re.findall(r'[^\.\[\]]+|\[\d+\]', query)

    for part in parts:
        if part.startswith('['):
            if not isinstance(cur, list):
                return NOT_FOUND
            idx = int(part[1:-1])
            if idx < 0 or idx >= len(cur):
                return NOT_FOUND
            cur = cur[idx]
        else:
            if not isinstance(cur, dict) or part not in cur:
                return NOT_FOUND
            cur = cur[part]

    return cur


data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input().strip()
    res = resolve(data, query)

    if res is NOT_FOUND:
        print("NOT_FOUND")
    else:
        print(json.dumps(res, separators=(',', ':')))

