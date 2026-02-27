import json

def diff(js1, js2, path=""):
    res = []

    if isinstance(js1, dict) and isinstance(js2, dict):
        for k in set(js1) | set(js2):
            p = f"{path}.{k}" if path else k
            res += diff(js1.get(k, "<missing>"), js2.get(k, "<missing>"), p)
    
    else:
        if js1 != js2:
            old = json.dumps(js1, separators=(",", ":")) if js1 != "<missing>" else "<missing>"
            new = json.dumps(js2, separators=(",", ":")) if js2 != "<missing>" else "<missing>"
            res.append(f"{path} : {old} -> {new}")

    return res

js1 = json.loads(input())
js2 = json.loads(input())

ans = diff(js1, js2)
if not ans:
    print("No differences")
else:
    for line in sorted(ans):
        print(line)
