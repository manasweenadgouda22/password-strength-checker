import math
from typing import Dict, Any
from .entropy import naive_entropy_bits
from .checks import (
    is_common_password, has_dictionary_word, has_sequence,
    has_repeats, looks_like_date, class_counts,
)
from .feedback import make_feedback

def clamp(v, lo, hi): 
    return max(lo, min(hi, v))

def adjusted_entropy(pw: str) -> float:
    bits = naive_entropy_bits(pw)
    penalties = 0.0
    if is_common_password(pw): penalties += 28.0
    if has_dictionary_word(pw): penalties += 10.0
    if has_sequence(pw): penalties += 10.0
    if has_repeats(pw): penalties += 8.0
    if looks_like_date(pw): penalties += 6.0
    return max(bits - penalties, 0.0)

def score_from_entropy(bits: float, pw: str) -> int:
    normalized = 100 * (1 - math.exp(-bits / 40.0))
    classes = class_counts(pw)
    diversity = sum(1 for k in ["lower","upper","digit","symbol"] if classes[k] > 0)
    normalized += (diversity - 1) * 3
    normalized += max(0, len(pw) - 12) * 1.5
    return int(clamp(normalized, 0, 100))

def classify_score(score: int) -> str:
    if score < 25: return "Very weak"
    if score < 50: return "Weak"
    if score < 70: return "Fair"
    if score < 85: return "Strong"
    return "Excellent"

def evaluate_password(pw: str) -> Dict[str, Any]:
    classes = class_counts(pw)
    flags = {
        "is_common": is_common_password(pw),
        "has_dictionary": has_dictionary_word(pw),
        "has_sequence": has_sequence(pw),
        "has_repeats": has_repeats(pw),
        "looks_like_date": looks_like_date(pw),
    }
    bits_adj = adjusted_entropy(pw)
    score = score_from_entropy(bits_adj, pw)
    out = {
        "password_length": len(pw),
        "classes": classes,
        "flags": flags,
        "entropy_bits_adjusted": bits_adj,
        "score": score,
        "strength": classify_score(score),
        "feedback": make_feedback(pw, flags, classes),
    }
    return out
