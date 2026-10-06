import os
from pathlib import Path
import json

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)
    
def write_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)


