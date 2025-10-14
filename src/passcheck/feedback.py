from typing import List, Dict

def make_feedback(pw: str, flags: Dict[str, bool], classes: Dict[str, int]) -> List[str]:
    tips = []
    L = len(pw)
    if L < 12:
        tips.append("Use at least 12 characters; more is better (16+).")
    if classes.get("upper",0) == 0 or classes.get("lower",0) == 0:
        tips.append("Mix uppercase and lowercase letters.")
    if classes.get("digit",0) == 0:
        tips.append("Add a number that is not a sequence or a year.")
    if classes.get("symbol",0) == 0:
        tips.append("Include a symbol (e.g., ! ? % #) in the middle, not only at the end.")
    if flags.get("is_common"):
        tips.append("Avoid common passwords and obvious patterns.")
    if flags.get("has_dictionary"):
        tips.append("Avoid dictionary words or common phrases—even with l33t substitutions.")
    if flags.get("has_sequence"):
        tips.append("Avoid sequences like 'abcd', '1234', or keyboard runs like 'qwerty'.")
    if flags.get("has_repeats"):
        tips.append("Avoid repeated characters like 'aaaa' or '1111'.")
    if flags.get("looks_like_date"):
        tips.append("Don’t use dates or years (e.g., 1998, 12-05-2001).")
    if not tips:
        tips.append("Looks good—consider using a password manager to generate and store strong secrets.")
    return tips
