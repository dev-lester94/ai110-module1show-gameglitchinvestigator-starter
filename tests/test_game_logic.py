from logic_utils import check_guess, parse_guess

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


# --- parse_guess tests ---

def test_parse_guess_valid_integer():
    # Normal whole number within Normal difficulty range
    ok, value, err = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_decimal_rejected():
    # Decimal input is not allowed — must be a whole number
    ok, value, err = parse_guess("7.9", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Please enter a whole number."

def test_parse_guess_boundary_low():
    # Lowest valid guess for the given range
    ok, value, err = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1
    assert err is None

def test_parse_guess_boundary_high():
    # Highest valid guess for the given range
    ok, value, err = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100
    assert err is None

def test_parse_guess_easy_range_valid():
    # Easy mode only goes to 20 — 15 should be valid
    ok, value, err = parse_guess("15", 1, 20)
    assert ok is True
    assert value == 15
    assert err is None

def test_parse_guess_easy_range_out_of_range():
    # Easy mode only goes to 20 — 50 should be rejected
    ok, value, err = parse_guess("50", 1, 20)
    assert ok is False
    assert value is None
    assert err == "Please enter a number between 1 and 20."

def test_parse_guess_hard_range_out_of_range():
    # Hard mode only goes to 50 — 75 should be rejected
    ok, value, err = parse_guess("75", 1, 50)
    assert ok is False
    assert value is None
    assert err == "Please enter a number between 1 and 50."

def test_parse_guess_zero_out_of_range():
    # 0 is below any valid range
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Please enter a number between 1 and 100."

def test_parse_guess_negative_out_of_range():
    # Negative numbers are out of range
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Please enter a number between 1 and 100."

def test_parse_guess_above_max():
    # Numbers above the max are out of range
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Please enter a number between 1 and 100."

def test_parse_guess_empty_string():
    # Empty input should fail with an error message
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    # None input should fail with an error message
    ok, value, err = parse_guess(None, 1, 100)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_letters():
    # Alphabetic input should fail with a number error
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_mixed_alphanumeric():
    # Mixed input like "12abc" should not parse as a number
    ok, value, err = parse_guess("12abc", 1, 100)
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_whitespace_only():
    # A string of spaces is not a valid number
    ok, value, err = parse_guess("   ", 1, 100)
    assert ok is False
    assert value is None
    assert err == "That is not a number."
