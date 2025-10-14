from passcheck import evaluate_password, classify_score

def test_common_password_is_weak():
    r = evaluate_password("password")
    assert r["score"] < 30
    assert r["flags"]["is_common"]

def test_strong_passphrase():
    r = evaluate_password("Cloud-bat! river 9 Maple@harbor")
    assert r["score"] >= 70

def test_feedback_present():
    r = evaluate_password("123456")
    assert len(r["feedback"]) >= 1

def test_classify():
    assert classify_score(10) == "Very weak"
    assert classify_score(55) == "Fair"
    assert classify_score(90) == "Excellent"
