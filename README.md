# Paper Loom

Weaves a university-style question paper from a BCA question bank. It does not shuffle. It threads units so every unit appears, no two neighbouring questions come from the same unit, and the difficulty rises, peaks, then lands.

Open `index.html`, pick a paper length, and weave again. Each weave is a different legal paper.

## What is unusual about it

The loom keeps three constraints at once:

1. **Quota.** Each unit must appear at least once before a unit can repeat.
2. **No back-to-back.** Adjacent questions cannot share a unit.
3. **Arc.** Early questions stay in the easy band, the middle holds the hard question, the close returns to medium.

If a candidate violates a constraint it is rejected and the next legal question is taken. The thread map shows which units are tight and which are still short.

Questions are original short prompts for Data Structures, DBMS, Operating Systems, and Computer Networks. They are starters, not a leaked paper.

## Run the Python core

```bash
python3 loom.py
```

## Stack

HTML, CSS, and JavaScript for the examination-sheet layout. Python 3 for the same weaver.
