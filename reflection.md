# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game has two sections. The is a side bar for the settings to set the diffulty, tells us to guess a number between 1 - 100, and the attempts allowed. The main screen displays the name of the game, a brief description, tells us to guess a number from 1 - 100 with the attemps allowed left, a developer debugger info section, an input to enter the guess, and three buttons to submit guess, new game, and to show hints, and lastly a brief footer message. I'm able to enter a number and it shows whether I should guess next a higher or lower number with the number of attempts left.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess 6|   Go higher       |  Go lower       | None                   |
|Guess 90|   Go lower       |  Go higher      | None                   | 
|Guess 10014| Not allowed guess |  Go higher  | None                   |
|Guess -20 | Not allowed guess | Go lower     | None                   |
|Guess 193.2 | Not allowed guess | Go lower   | None                   |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude Code to help generate the refactor and fix for the bugs from app.py to logic_utils.py. And I also fix and created new test cases in test_game_logic.py. I used Chatgpt to help assist me in finding the correct command to run the puytest. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). An example where AI suggestion was correct was where I prompted the AI to tell me where in app.py or logic_utils.py, it is showing me the message to guess higher or lower for my next guess after submitting my current guess. The message is built in check_guess at app.py:32-47: Line 38: returns "📈 Go HIGHER!" when guess > secret (this is the intentional bug — the hint is reversed; if your guess is too high, you should go lower) Line 40: returns "📉 Go LOWER!" when guess < secret (same reversal). I verified what check_guess by temporary changing what to be return with my dummy tuple. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I verified the changes by playing the game again after re running the app with the fixes and ran the pytest and saw that all test pass succesfully. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. All of the original three test cases in test_game_logic did not passed such as the test_guess_too_low function with AssertionError: assert ('Too Low', '📈 Go HIGHER!') == 'Too Low' for. I was then motivated to prompt Claude code to understand what check_guess returned and to fix the unit test afterwards for me. 
- Did AI help you design or understand any tests? How? Yes Claude code told me the following for  test_guess_too_low that "The test expects a bare string but check_guess returns a tuple. I'll update it to unpack the outcome." So this meant when assert result == "Too Low" is computing, result should be the string "Too Low" but check_guess returns a tuple so it had to be unpack first where the first element in the tuple is then to be compare with the string "Too Low".

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
