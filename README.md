# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
   Guess the secret number between 1 to X depneding on the game mode.
- [X] Detail which bugs you found.
   Found bug where the message of telling the user to guess higher or lower is incorrect.
   Found bug where user can enter a decimal number and it will truncate it and compare to the secret which
   Found bug where user can enter a number out of the game settings range and it will say to go higher or lower.
   Found bug where the secret can be set outside the game settings range  
- [X] Explain what fixes you applied.
   Fix was to correct tell the user to guess higher or lower depending on the conditional between whether the guess was lower or higher than the secret.
   When user enters a decimal it displays to the user to Please enter a whole number.
   When user enters a number out of the range like 100 where the range is between 1 and 50 it displays Please enter a number between 1 and 50.
   When I change the game setting and hit new game, the secret number should be a number in range of the game setting in the developer mode section.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 40
2. Game returns "Too Low"
3. User enters a guess of 70 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

1. User enters a guess of 7.8
2. Game returns Please enter a whole number.
3. User enters a guess of 50 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

1. User enters a guess of 0
2. Game returns Please enter a number between 1 and 100.
3. User enters a guess of 50 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

1. User enters a guess of 100 when game setting is hard (1 to 50)
2. Game returns Please enter a number between 1 and 50.
3. User enters a guess of 38 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess



**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
#========================================== 20 passed in 0.09s ===========================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
