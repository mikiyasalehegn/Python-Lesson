## **What is a Loop?**

A loop is a programming construct that repeats a block of code until a certain condition is met.

In Python, there are **two main types** of loops:

- **`for` loop** → Iterates over a sequence (list, tuple, string, dictionary, range, etc.) or any iterable object.
- **`while` loop** → Repeats while a condition remains `True`.

---

### **The `for` Loop**

The `for` loop in Python **does not** work like in C or Java (with an index counter).

Instead, it **iterates over items directly** from an iterable.

**Syntax:**

```python
for variable in iterable:
    # code block
```

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit
```

**Key Notes:**

- You can iterate over lists, tuples, sets, dictionaries, strings, ranges, or even custom iterators.
- Dictionaries give **keys** by default:

```python
my_dict = {"a": 1, "b": 2}
for key in my_dict:
    print(key, my_dict[key])
```

- To iterate over keys and values:

```python
for key, value in my_dict.items():
    print(key, value)
```

- To get both index and value, use **`enumerate()`**:

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

- Always ensure the loop modifies variables so the condition can become `False`.

### **Loop Control Statements**

Python has **three** main control statements to manage loops:

1. **`break`** → Stops the loop entirely.

```python
for num in range(1, 6):
    if num == 3:
        break
    print(num)  # Output: 1, 2
```

1. **`continue`** → Skips the rest of the code in the current iteration and moves to the next.

```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)  # Output: 1, 2, 4, 5
```

1. **`pass`** → Does nothing, acts as a placeholder.

```python
for num in range(1, 6):
    if num == 3:
        pass
    print(num)

# output
1
2
3
4
5
```

- **Essential Notes**

    **1. Avoiding Syntax Errors (The Syntactic Requirement)**

    Python relies on indentation to define code blocks. Unlike languages like C++ or Java that can use empty curly braces `{}`, Python **requires** at least one statement in any indented block (after `for`, `while`, `if`, `def`, etc.).

    - If you leave a loop body empty, Python will raise an `IndentationError`.
    - `pass` serves as a valid statement that satisfies this requirement without adding any logic.

    **2. Acting as a Placeholder (Developing & Prototyping)**

    It is common to use `pass` as "scaffolding" while you are still building your code.

    - **Sketching Structure:** You can define a loop structure and use `pass` to keep the code runnable while you figure out the actual logic later.
    - **Minimal Implementation:** It allows you to create "stubs" for loops, functions, or classes that you don't want to implement immediately.

    **Comparison: pass vs. continue vs. break**

    It is important not to confuse `pass` with other loop control keywords:

    | **Statement** | **Effect on the Loop** |
    | --- | --- |
    | **`pass`** | **Does nothing.** The loop continues exactly as if the line weren't there. |
    | **`continue`** | **Skips** the rest of the *current* iteration and jumps back to the top of the loop. |
    | **`break`** | **Stops** the loop entirely and exits to the code following the loop. |

    **Example:**

    **python**

    ```python
    for i in range(3):
        if i == 1:
            pass  # Just a placeholder; it does nothing
        print(i)
    # Output: 0, 1, 2 (The number 1 is still printed because pass did nothing)
    ```

    Use code with caution.

    **Other Common Uses**

    Beyond loops, `pass` is frequently used for:

    - **Empty Exceptions:** Ignoring an error when you don't need to take any action.
    - **Minimal Classes:** Creating a custom exception class: `class MyError(Exception): pass`.
    - **Debug Markers:** Providing a line where you can set a breakpoint in a debugger.

### **`else` with Loops**

Python allows an **`else`** block after loops, which runs **only if the loop completes normally** (no `break`).

**Example:**

```python
for num in range(3):
    print(num)
else:
    print("Loop finished without break")
```

If a `break` occurs, the `else` block **will not run**.

### **Nested Loops**

You can place loops inside loops.

**Example:**

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

**Use case:** Working with 2D lists, matrices, or combinations.

### **Loop with `range()`**

`range(start, stop, step)` generates a sequence of numbers(**Integers**).

**Examples:**

```python
for i in range(5):          # 0 to 4
    print(i)

for i in range(2, 6):       # 2 to 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)
```

### **Iterating with Comprehensions**

Instead of writing full loops, Python allows **list, set, and dict comprehensions** for concise looping.

**Examples:**

```python
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]             # List comprehension
even_nums = [x for x in nums if x % 2 == 0]
num_square_map = {x: x**2 for x in nums}   # Dict comprehension
```

### **Loop Efficiency Tips**

- Avoid modifying the list you’re iterating over directly — instead, iterate over a copy.
- Use `enumerate()` instead of manually tracking indices.
- Use comprehensions for cleaner and faster loops when building new collections.

### **Loops with `zip()`**

You can loop through multiple sequences **in parallel**.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(name, score)
```

### **Reverse Loops**

You can iterate backward with `reversed()`:

```python
for x in reversed(range(1, 5)):
    print(x)  # 4, 3, 2, 1
```

### **Loops with `any()` / `all()`**

Sometimes you don’t need to write an explicit loop:

```python
nums = [1, 2, 3, 4]
print(any(n > 3 for n in nums))  # True
print(all(n < 5 for n in nums))  # True
```

### **Loop Variable Scope Quirk**

Unlike some languages, **loop variables remain in scope after the loop**.

```python
for i in range(3):
    pass
print(i)  # 2 (last value)
```

This can cause bugs if you expect the variable to disappear after the loop.

## Iterating Over Dictionary

### 1. **Iterate over keys (default)**

When you iterate directly over a dictionary, you get the **keys**.

```python
my_dict = {"name": "Mikiyas", "age": 25, "city": "Tel Aviv"}

for key in my_dict:
    print(key)
```

**Output:**

```
name
age
city
```

---

### 2. **Iterate over values**

If you want just the **values**, use the `.values()` method.

```python
for value in my_dict.values():
    print(value)
```

**Output:**

```
Mikiyas
25
Tel Aviv
```

---

### 3. **Iterate over key-value pairs**

If you want both **key and value**, use `.items()`:

```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

**Output:**

```
name: Mikiyas
age: 25
city: Tel Aviv
```

### 4. **Iterate with index**

Sometimes you want the **index** while iterating. Use `enumerate()`:

```python
for index, (key, value) in enumerate(my_dict.items()):
    print(f"{index}: {key} -> {value}")
```

**Output:**

```
0: name -> Mikiyas
1: age -> 25
2: city -> Tel Aviv
```

### 5. **Comprehensions**

You can also iterate in dictionary comprehensions:

```python
# Example: create a new dict with uppercased keys
new_dict = {key.upper(): value for key, value in my_dict.items()}
print(new_dict)
```

**Output:**

```
{'NAME': 'Mikiyas', 'AGE': 25, 'CITY': 'Tel Aviv'}
```

---

✅ **Summary:**

- `for key in dict:` → iterates keys
- `for value in dict.values():` → iterates values
- `for key, value in dict.items():` → iterates key-value pairs
- `enumerate(dict.items())` → iterates with index

## **What is a `while` loop?**

- Always ensure the loop modifies variables so the condition can become `False`.

A `while` loop repeats a block of code **as long as** a given condition is `True`.

**Basic syntax:**

```python
while condition:
    # code block
```

- The condition is checked **before** each loop iteration.
- If the condition becomes `False`, the loop stops.

### **Basic Example**

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```

**Output:**

```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### **Infinite `while` loop**

If the condition **never becomes False**, you get an **infinite loop**.

```python
while True:
    print("This will run forever!")
```

Stop with **Ctrl + C** in the terminal.

### **`break` statement**

You can exit a loop early with `break`.

```python
n = 1
while True:
    print(n)
    if n == 5:
        break
    n += 1
```

### **`continue` statement**

Skips the rest of the loop body and goes to the next iteration.

```python
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue  # skip printing 3
    print(n)
```

### **`else` with while**

The `else` block runs if the loop ends **naturally** (not with `break`).

```python
n = 1
while n <= 3:
    print(n)
    n += 1
else:
    print("Loop finished without break.")
```

### **Common Use Cases**

- **Counting**

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

- **Waiting for a condition**

```python
import time

ready = False
while not ready:
    print("Waiting...")
    time.sleep(1)
    ready = True
print("Ready!")
```

- **Processing until empty**

```python
tasks = ["task1", "task2", "task3"]

while tasks:
    task = tasks.pop(0)
    print("Processing:", task)
```

- **Menu systems**

```python
while True:
    choice = input("Enter 'q' to quit: ")
    if choice.lower() == "q":
        break
```

### **Important Tips**

- Always make sure your `while` loop **will eventually stop**; otherwise, it runs forever.
- Be careful with **modifying variables** inside the loop that affect the condition.
- Use `while True` + `break` when you need an **infinite loop with controlled exit points**.

### **`else` block weirdness**

The `else` runs **only if the loop is not broken with `break`**.

```python
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("No break, so else runs")
```

```python
n = 0
while n < 3:
    print(n)
    if n == 1:
        break
    n += 1
else:
    print("This will NOT run")
```

### **`while` with `try/except`**

You can handle exceptions inside a `while` loop without stopping the loop.

```python
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("That’s not a number, try again.")
```

### **Mutating data in a `while` loop**

Since `while` doesn’t use indexing directly, it’s often paired with `.pop()` or `.popleft()` for processing items until empty.

```python
tasks = ["a", "b", "c"]

while tasks:
    print("Processing:", tasks.pop())
```

### **Dangerous infinite loops**

Sometimes a `while` condition looks fine but **never changes**.

```python
python
CopyEdit
x = 5
while x > 0:
    print("Still going...")
    # forgot to change x → infinite loop

```

Always make sure the loop variable **moves toward the exit condition**.

### **Rare but possible: `while` inside comprehensions**

It’s unusual, but you *can* use it in generator expressions:

```python
# This generates numbers until condition fails
def numbers():
    n = 0
    while n < 3:
        yield n
        n += 1

for num in numbers():
    print(num)
```

## **What is a nested loop?**

A **nested loop** means **one loop runs inside another loop**.

The **inner loop** runs completely **every time** the outer loop runs once.

**Example:**

```python
for i in range(3):       # Outer loop
    for j in range(2):   # Inner loop
        print(i, j)
```

**Output:**

```
0 0
0 1
1 0
1 1
2 0
2 1
```

- Outer loop (`i`) runs 3 times.
- For **each** `i`, inner loop (`j`) runs 2 times → **total = 3 × 2 = 6 iterations**.

---

### **Nested `while` loops**

```python
i = 0
while i < 3:            # Outer while
    j = 0
    while j < 2:        # Inner while
        print(i, j)
        j += 1
    i += 1
```

Same output as above.

---

### **Mixing `for` and `while`**

You can mix types of loops:

```python
for i in range(3):
    j = 0
    while j < 2:
        print(i, j)
        j += 1
```

### **Common use cases**

- **Working with 2D lists (matrices)**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
```

Output:

```
1 2 3 4 5 6 7 8 9
```

- **Generating combinations**

```python
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(color, size)
```

Output:

```
red S
red M
red L
blue S
blue M
blue L
```

### **Breaking out of nested loops**

`break` only stops **the innermost loop** unless you use extra logic:

```python
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break
        print(i, j)
```

Here, only the inner loop stops when `i == 1 and j == 1`.

To stop **both loops**:

```python
stop_all = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            stop_all = True
            break
        print(i, j)
    if stop_all:
        break
```

### **Efficiency warning**

Nested loops multiply work:

- Outer loop = `n` times
- Inner loop = `m` times
- Total iterations = `n × m`

    So avoid unnecessary nesting for large datasets.