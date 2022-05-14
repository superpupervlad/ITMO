import json

def input(filepath):
    return json.loads(str(open(filepath, 'r').read()))