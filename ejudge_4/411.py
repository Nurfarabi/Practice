import json

def patch(source, patch_obj):
    for k, v in patch_obj.items():
        if v is None:
            source.pop(k, None)
        elif k in source and isinstance(source[k], dict) and isinstance(v, dict):
            patch(source[k], v)
        else:
            source[k] = v
    return source

source = json.loads(input())
patch_obj = json.loads(input())
print(json.dumps(
    patch(source, patch_obj),
      separators=(",", ":"),
      sort_keys = True
    ))