import re, string
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

def _load_common_list():
    p = DATA_DIR / "common_weak_passwords.txt"
    if not p.exists():
        return set()
    return set(line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip())

COMMON = _load_common_list()
KEYBOARD_ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]
LEET_MAP = {"0":"o","1":"l","!":"i","3":"e","4":"a","@":"a","5":"s","$":"s","7":"t","+":"t","8":"b"}

def normalize_leet(s: str) -> str:
    return "".join(LEET_MAP.get(c.lower(), c.lower()) for c in s)

def is_common_password(pw: str) -> bool:
    return pw.lower() in COMMON or normalize_leet(pw) in COMMON

def has_dictionary_word(pw: str, min_len: int = 4) -> bool:
    low = normalize_leet(pw)
    for w in COMMON:
        if len(w) >= min_len and w in low:
            return True
    return False

def has_sequence(pw: str, min_run: int = 4) -> bool:
    low = pw.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    for i in range(len(alpha) - min_run + 1):
        if alpha[i:i+min_run] in low:
            return True
    for i in range(len(digits) - min_run + 1):
        if digits[i:i+min_run] in low:
            return True
    for row in KEYBOARD_ROWS:
        for i in range(len(row) - min_run + 1):
            if row[i:i+min_run] in low:
                return True
    return False

def has_repeats(pw: str, min_repeat: int = 3) -> bool:
    return re.search(rf"(.)\1{{{min_repeat-1},}}", pw) is not None

def looks_like_date(pw: str) -> bool:
    patterns = [
        r"(19|20)\d{2}",
        r"\d{2}[/-]\d{2}[/-](19|20)\d{2}",
        r"(19|20)\d{2}[/-]\d{2}[/-]\d{2}",
        r"\d{6}$",
        r"\d{8}$"
    ]
    return any(re.search(p, pw) for p in patterns)

def class_counts(pw: str):
    return {
        "lower": sum(c.islower() for c in pw),
        "upper": sum(c.isupper() for c in pw),
        "digit": sum(c.isdigit() for c in pw),
        "symbol": sum(c in string.punctuation for c in pw),
        "space": sum(c.isspace() for c in pw),
    }
