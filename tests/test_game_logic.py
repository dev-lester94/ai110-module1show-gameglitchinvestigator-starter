from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_low_returns_go_higher():
    # Secret is 50, guess is 40 — guess is too low, hint should direct player higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_too_high_returns_go_lower():
    # Secret is 40, guess is 50 — guess is too high, hint should direct player lower
    outcome, message = check_guess(50, 40)
    assert outcome == "Too High"
    assert "LOWER" in message
