import math, string
SYMBOLS = string.punctuation

def character_pool_size(pw: str) -> int:
    pool = 0
    if any(c.islower() for c in pw): pool += 26
    if any(c.isupper() for c in pw): pool += 26
    if any(c.isdigit() for c in pw): pool += 10
    if any(c in SYMBOLS for c in pw): pool += len(SYMBOLS)
    if any(c.isspace() for c in pw): pool += 1
    if any(ord(c) > 127 for c in pw): pool += 50  # crude unicode bonus
    return max(pool, 1)

def naive_entropy_bits(pw: str) -> float:
    pool = character_pool_size(pw)
    return len(pw) * (math.log2(pool) if pool > 1 else 0.0)
