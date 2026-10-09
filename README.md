# Wordle.py

Terminal Wordle clone in Python with colored feedback (green = right spot, yellow = in word, white = not in word). Guesses are checked against the full list of valid Wordle words; the answer is drawn from the official answer list.

```
pip install colorama
python3 wordle.py
```

Built in a day as a Week 6 class project.

## Known issues
- Repeated letters aren't handled like real Wordle (extra copies can show yellow).
- The win check doesn't end the game early.
