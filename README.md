# Day 01 – Python Basics 🐍

## 📘 Overview
- Introduces core Python concepts required for beginners
- Focuses on syntax, data types, operators, and conditional logic
- Builds a strong foundation for AI and advanced programming

---

## 📝 Comments & Docstrings
- Single-line comments using `#`
- Multi-line comments / docstrings using `""" """`

---

## 🔤 Variables & Naming Conventions
- Pascal Case: `MyName`
- Camel Case: `myName`
- Snake Case (Python standard): `my_name`

---

## 🔢 Data Types
- **Numbers**
  - Integer (`int`)
  - Floating-point (`float`)
  - Complex (`complex`)
- **String (`str`)**
- **Boolean (`bool`)**

---

## 🔡 Unicode Functions
- `ord()` → Converts character to Unicode value
- `chr()` → Converts Unicode value to character

---

## ✂️ String Indexing & Slicing
- Indexing using positive and negative indices
- Slicing using `start : stop : step`

---

## 🔄 Type Conversion
- Explicit type conversion using:
  - `int()`
  - `str()`
  - `float()`
  - `bool()`

---

## ⚖️ Truthy & Falsy Values
- Falsy values include:
  - `0`, `0.0`, `[]`, `()`, `{}`, `""`, `False`
- All other values are truthy

---

## 🧩 Formatted Strings
- Uses f-strings for clean and readable output

---

## ⌨️ Input & Output
- Takes user input using `input()`
- Displays output using `print()`

---

## ➕ Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `//`, `**`
- Assignment and compound assignment operators
- Comparison operators
- Logical operators (`and`, `or`, `not`)
- Python follows **BODMAS**

---

## 🔍 Conditional Statements
- `if` statement
- `if-else` statement
- `if-elif-else` ladder

---

## 🧠 Practice Programs
- Find the largest of two numbers
- Gender-based greeting message
- Check even or odd number
- Voter eligibility check 🗳️
- Leap year validation 📅
- Temperature-based conditions 🌡️

---

## 🎯 Key Takeaways
- Clear understanding of Python basics
- Improved logical thinking
- Strong base for upcoming Python and AI topics 🚀


# 🐍 Python Loops Wonderland ✨🌸
# Day 02 – Python Loops 🐍

Welcome to my Python journey! This repository is dedicated to mastering **Loops**—the superpower of automation! 🚀 From printing tables to cracking prime numbers, it's all here! 🌻😊

---

## 📚 What's Inside? 📖

In Python, we have two main ways to repeat tasks:
1. **The `for` Loop**: Perfect for numbers and sequences! 🔢
2. **The `while` Loop**: Perfect for conditions! ⚙️

### 🌷 The `range()` Magic
The `range(start, stop, step)` function is our best friend! 👫
* 🏁 **Start**: Where we begin (Default: 0)
* 🛑 **Stop**: Where we end (Exclusive!)
* 🪜 **Step**: How many steps we jump (Default: 1)

---

## 🛠️ Logic & Exercises Solved 🧠💡

I've practiced various real-world logic problems here:

* **🔢 Number Crunching**: 
  * Printing natural numbers up to $n$ 📝
  * Generating mathematical tables (e.g., Table of 5, 7, or $n$) ✖️
  * Calculating **Factorials** and **Sum of $n$ terms** ➕

* **💎 Special Numbers**:
  * **Prime Number Check**: Is it divisible only by itself? 🛡️
  * **Perfect Number Check**: Do its factors add up to the number? 🎯
  * **Even/Odd Sums**: Separating and summing numbers in a range ⚖️

* **🔤 String Sorcery**:
  * **Reversing a string**: Turning "Ayushi" into "ihsuyA" 🔄
  * **Palindrome Check**: Checking if it reads the same backward! ↔️
  * **Character Analytics**: Counting letters, digits, and symbols using ASCII (`ord()`) 🔍

---

## 🚀 Key Learning Snippets 💻✨



### 🏃‍♂️ Break vs Continue
* `break`: Stops the loop completely. 🛑
* `continue`: Skips the current turn and jumps to the next! ⏭️

### 📝 Sample Code for Table:

num = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}") 🌸

🐍 PYTHON JOURNEY DAY 3 🚀✨
🌀 THE WHILE LOOP WONDERLAND 🌀
Hello! Today was amazing! 🌸🌷🌻 We mastered the art of the while loop and learned how to flip numbers inside out! 🌈💎

🔍 EXPLORING DATA TYPES 😊🌟
We used these commands to see all the "superpowers" inside Python: 🌻 print(dir(str)) — Everything strings can do! 🧵 🌻 print(dir(int)) — Everything integers can do! 🔢

🔄 WHY THE WHILE LOOP? 🤔💭
We use the while loop when we don't know the exact number of steps, but we have a goal in mind! 🏃‍♀️🎯 We keep going until the condition is satisfied! 🌊✨

🧩 THE CHALLENGES WE CRUSHED 🏆💖
1️⃣ Digit Separator 🔪🔢 We broke numbers apart digit by digit! 🧩

Using % 10 to grab the last piece 🍬

Using // 10 to cut the rest away ✂️

2️⃣ Number Reverser 🔄🙃 We took numbers and flipped them backward! 🤸‍♂️✨ Example: 123 ➡️ 321! 🎊

3️⃣ Palindrome Checker 🪞🦢 We checked if a number is a mirror image! 💖

We used two pointers (i and j) to walk through the number from both sides! 👫✨

If they match all the way, it's a Palindrome! 🦢💎

4️⃣ Random Guessing Game 🎲🎮 The most fun part! 🥳

The computer thinks of a number... 🤖💭

We guess until we hit the bullseye! 🎯💥

Too high? 🎈 Too low? 👇 We found it! 🎉🎈🎊

💡 THE MAGIC TOOLS OF THE DAY 🧪🌸
✨ % (Modulo) — Finds the remainder! 🍭 ✨ // (Floor Division) — Chops the number! 🔪 ✨ random — Adds the element of surprise! 🎁✨

🌈 FEELING LIKE A PRO 😊💻🌷
Today was full of logic, flowers, and smiles! 🌺🌿 Every line of code is a new petal on my Python flower! 🌸✨ Keep coding and keep shining! ☀️🦋🌟
