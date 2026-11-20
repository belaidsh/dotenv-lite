import os

def parse_line(raw: str):
    line = raw.strip()
    if not line or line.startswith('#') or '=' not in line:
        return None, None
    k, v = line.split('=', 1)
    return k.strip(), v.strip().strip('"').strip("'")
