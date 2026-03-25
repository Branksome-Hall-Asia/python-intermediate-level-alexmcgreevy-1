[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23270270)
# 🚀 Level 2: Intermediate Python - Data & Functions

Now that you can write basic scripts, it's time to learn how to build **Scalable Software**. This level focuses on making your code organized and handling lists of data.

---

## 🛠 THE 12 CHALLENGES

### 1. Scope & Logic
**Concept:** Where do variables live?
- **Task:** Create a variable inside a function and try to print it outside. Fix the error that occurs.
- **Tip:** Variables created inside a "def" block are "Local"—they vanish when the function ends!

### 2. The Multiplier (Basic Functions)
**Concept:** Writing code once, using it many times.
- **Task:** Define a function called `greet_user()`. It should print a fancy welcome message. Call it 3 times.

### 3. The Custom Messenger (Parameters)
**Concept:** Sending information *into* a function.
- **Task:** Update `greet_user(name)` so it takes a name as an argument and says "Hello [name]".

### 4. The Result Maker (Return Values)
**Concept:** Getting information *out* of a function.
- **Task:** Write a function `add_numbers(a, b)` that **returns** the sum instead of printing it.
- **Tip:** Think of `return` as the function handing a physical object back to you.

### 5. The Shopping List (1D Arrays)
**Concept:** Storing multiple items in one variable.
- **Task:** Create a list of 5 grocery items. Print the 1st and last item using their **index**.
- **Tip:** Remember, computers start counting at **0**, not 1!

### 6. List Surgeon (Methods)
**Concept:** Modifying data.
- **Task:** Take your list from Task 5. Add "Chocolate", remove the 2nd item, and sort the list alphabetically.

### 7. The Roll Call (Loops + Lists)
**Concept:** Processing every item.
- **Task:** Use a `for` loop to print every item in a list of names, but add "is present" after each name.

### 8. The Search Engine
**Concept:** Membership testing.
- **Task:** Ask a user for a name. Check if that name exists in your `student_list`. If yes, print "Found!".

### 9. The Crash Proof Code (Validation)
**Concept:** Preventing errors.
- **Task:** Ask the user for a number. Use `try` and `except` to make sure the program doesn't crash if they type a word instead.

### 10. The Dice Dealer (Libraries)
**Concept:** Importing tools.
- **Task:** `import random`. Create a list of 6 outcomes. Make the computer pick one at random.

### 11. Secret Codes (Slicing)
**Concept:** Cutting up data.
- **Task:** Take a long string like "PythonProgramming". Print only the first 6 letters using slicing `[0:6]`.

### 12. The Grid (Nested Logic)
**Concept:** Ifs inside Loops.
- **Task:** Loop through numbers 1-20. Only print the numbers that are **Even**.

---

## 🏆 KEYSTONE PROJECTS

### 🎒 Keystone 1: RPG Inventory Manager
**File:** `keystone_01_inventory.py`
Create a program that acts as a video game inventory.
1. Start with a list: `["Sword", "Shield", "Potion"]`.
2. Create a menu (1. Add, 2. Remove, 3. View, 4. Exit).
3. Use **functions** for each menu option.
4. Prevent the user from adding more than 5 items (Inventory Full!).

### 📊 Keystone 2: The Grade Analyzer
**File:** `keystone_02_gradebook.py`
1. Create a list of 10 random test scores (0-100).
2. Write functions to:
   - Find the **Average** score.
   - Find the **Highest** and **Lowest** score.
   - Count how many students **Failed** (below 50).
