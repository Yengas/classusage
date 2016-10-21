import json

def canSerialize(obj):
    try:
        json.dumps(obj)
    except TypeError:
        return False
    return True

def dictify(obj):
    if isinstance(obj, list):
        return [dictify(x) for x in obj]

    result = {}

    for key, value in obj.__dict__.items():
        if not value or value is None:
            pass
        elif not canSerialize(value):
            result[key] = dictify(value)
        else:
            result[key] = value

    return result

def deepSerialize(obj):
    return json.dumps(dictify(obj))
