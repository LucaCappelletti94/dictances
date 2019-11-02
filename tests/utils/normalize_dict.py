from typing import Dict

def normalize_dict(a: Dict)->Dict:
    total = sum([
        abs(v) for v in a.values()
    ])
    return {
        k:abs(v)/total for k, v in a.items()
    }