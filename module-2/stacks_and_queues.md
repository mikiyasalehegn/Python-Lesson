# Stacks in Python

### 1. 🔹 What is a Stack?

A **stack** is a linear data structure that follows the principle:

👉 **LIFO (Last In, First Out)**

- The **last** element you put in (push) is the **first** one you take out (pop).

Think of a stack of plates:

- You put plates on top.
- You take plates from the top.

In Python, a **Stack is a logic (a data structure principle)** rather than a specific, built-in "data type" like an integer or a string.

Here is the breakdown to make it crystal clear:

**1. It is an "Abstract Data Type"**

In computer science, a Stack is a **conceptual rulebook**. The rulebook says: *"You can only add and remove items from the very top (LIFO)."*

Python does not have a specific keyword called `stack`. Instead, we **use** existing data types (like Lists) and **restrict ourselves** to only using certain methods to follow that rulebook.

**2. The Comparison**

Think of a **List** like a **Swiss Army Knife**. It can do many things:

- Add to the end (`append`)
- Add to the middle (`insert`)
- Remove from the front (`pop(0)`)
- Remove from the end (`pop()`)

A **Stack** is like that same knife, but you **choose to only use two blades**:

- `append()` (The "Push" blade)
- `pop()` (The "Pop" blade)

If you use `insert(0, item)` on a list, you are no longer using it as a Stack; you are using it as a standard List or a Queue.

**3. A Visual Analogy**

Imagine a **bucket**.

- **The Bucket (The Data Type):** This is the physical object (In Python, this is the `list`).
- **The Stack (The Principle):** This is the **rule** that you cannot reach the bottom of the bucket without taking out everything on top first.



### 2. 🔹 Common Stack Operations

1. **Push** → Add an item to the top.
2. **Pop** → Remove the top item.
3. **Peek/Top** → Look at the top item without removing it.
4. **isEmpty** → Check if the stack is empty.
5. **Size** → Get how many items are in the stack.

**Core Operations & Efficiency**

All primary stack operations typically occur at one end, known as the **top**.

| **Operation** | **Description** | **Python Method (List)** | **Time Complexity** |
| --- | --- | --- | --- |
| **Push** | Adds an item to the top. | `.append()` | **O(1)** |
| **Pop** | Removes and returns the top item. | `.pop()` | **O(1)** |
| **Peek/Top** | Returns the top item without removing it. | `stack[-1]` | **O(1)** |
| **is_empty** | Checks if the stack has no elements. | `if not stack:` | **O(1)** |
| **Size** | Returns the number of elements. | `len(stack)` | **O(1)** |
|  |  |  |  |

**Summary**

- **Is it a Data Type?** No, it's an **Abstract Data Type** (a concept).
- **Is it a Principle?** Yes. It is the **LIFO principle** applied to a collection of data.
- **What is the actual Python type?** Usually a `list` or a `collections.deque`.

### 3. 🔹 Implementing a Stack in Python

### Method 1: Using a List

Python’s built-in list works well as a stack.

```python
stack = []

# Push (append)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)  # [10, 20, 30]

# Pop (remove last)
top = stack.pop()
print("Popped:", top)   # 30
print("Stack after pop:", stack)  # [10, 20]

# Peek (last element)
print("Top element:", stack[-1])  # 20

# Check empty
print("Is empty?", len(stack) == 0)  # False

```

⚠️ Note: `.append()` and `.pop()` (without index) are both **O(1)** operations → efficient for stacks.


### Method 2: Using `collections.deque`

`deque` (double-ended queue) from `collections` is **faster and more efficient** for stacks than lists.

```python
from collections import deque

stack = deque()

# Push
stack.append("a")
stack.append("b")
stack.append("c")
print("Stack:", stack)  # deque(['a', 'b', 'c'])

# Pop
print("Popped:", stack.pop())  # c
print("Stack after pop:", stack)  # deque(['a', 'b'])

```


### Method 3: Custom Stack Class

We can also define our own **Stack class** for clarity.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # or raise exception

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())   # 3
print(s.pop())    # 3
print(s.size())   # 2

```

### Method 4: **Using `queue.LifoQueue` (The Thread-Safe Way)**

If you are working with multiple **threads** (parallel processing), use `LifoQueue` to prevent data corruption.

**python**

```python
from queue import LifoQueue
stack = LifoQueue()

stack.put("Data1") # Push
print(stack.get()) # Pop -> Output: Data1
```


### 4. 🔹 Real-Life Use Cases of Stacks

Stacks are used in any scenario where you need to track a history of actions and reverse them in the exact opposite order they occurred (**LIFO**).

**1. Browser Navigation (Back/Forward Buttons)**

Web browsers use stacks to manage your surfing history.

- **The "Back" Stack:** Every time you visit a new URL, it is **pushed** onto this stack.
- **Back Button:** When you click "Back," the current page is **popped** from the Back stack and pushed onto a separate **"Forward" stack**.
- **Forward Button:** Clicking "Forward" pops from the Forward stack and pushes back into the Back stack.

**2. Undo/Redo in Software**

Applications like VS Code, Microsoft Word, and Photoshop rely on stacks to revert user mistakes.

- **Undo Stack:** Every action (typing a word, deleting a line) is stored as a "state" in a stack.
- **Reversing:** When you hit `Ctrl+Z`, the software **pops** the most recent action and reverses it.
- **Redo:** Most professional tools use a second **Redo stack** to store those popped actions, allowing you to "un-undo" them.

**3. Backtracking Algorithms (Solving Puzzles)**

Stacks are the engine for **Backtracking**, a technique used in AI and game development to explore all possible solutions to a problem.

- **Solving a Maze:** The algorithm stores its current path in a stack.
- **Dead Ends:** If the algorithm hits a wall, it **pops** the stack to "backtrack" to the last intersection and try a different path.
- **Other Examples:** Sudoku solvers, the N-Queens problem, and chess-playing engines use this stack-based exploration.

**4. Code Syntax Validation**

Compilers and IDEs (like GitHub's editor) use stacks to ensure your code is correctly formatted.

- **Bracket Matching:** When a programmer types an opening brace `{`, it is **pushed** onto a stack.
- **Validation:** When a closing brace `}` appears, the editor **pops** the stack. If the popped item isn't the matching `{`, the editor highlights a syntax error.

**5. Memory Management (The Call Stack)**

This is the most critical technical use of a stack. Every modern programming language uses a **Call Stack** to manage function execution.

- **Nested Calls:** When `Function A` calls `Function B`, all of A's variables are **pushed** onto the stack so the computer can remember where to return when B finishes.
- **Recursion:** Stacks are what allow functions to call themselves safely by keeping each call's data in its own independent "frame" on the stack.

# What is a Queue?

- **A Queue is an abstract data structure that works on the FIFO (First In, First Out) principle.**
    
    Just like the **Stack**, a **Queue** is primarily an **Abstract Data Type (ADT)**—which is a fancy computer science way of saying it is a **logical principle**, not a physical storage type.
    
    **1. The Logic (The "What")**
    
    The **principle** is the set of rules (FIFO). It defines how data *should* behave:
    
    - Entry is only at the **Rear**.
    - Exit is only at the **Front**.
    - The first one in **must** be the first one out.
    
    **2. The Implementation (The "How")**
    
    To make a Queue work in Python, you have to use a physical **Data Type** (the container). You can build a Queue using several different actual types:
    
    - **Using a List:** You use the `list` type but restrict yourself to `append()` and `pop(0)`.
    - **Using a Deque:** You use the `collections.deque` type but only use `append()` and `popleft()`.
    - **Using a Linked List:** You manually connect objects together to form a chain.
    
    **3. The "Restaurant" Analogy**
    
    To understand the difference between the **Principle** and the **Type**:
    
    - **The Principle (Queue):** This is the "Waiting Line" at a restaurant. It is a set of social rules: "No cutting in line, first person here gets the first table."
    - **The Data Type (Container):** This is the physical space where the line forms. The line could form in a narrow hallway (a **List**), a big open lobby (a **Deque**), or even outside on the sidewalk (a **Linked List**).
- Think of it like a **line at a supermarket**: the first person to join is the first person to leave.

---

### 📌 Queue vs Stack

- **Stack** → LIFO (Last In, First Out).
- **Queue** → FIFO (First In, First Out).

👉 Both can be implemented using **lists** or `collections.deque` in Python.

---

### 🛠 Queue Operations

Just like stacks, queues have specific operations:

1. **Enqueue** → Add element to the **rear**.
2. **Dequeue** → Remove element from the **front**.
3. **Peek/Front** → See the first element without removing.
4. **isEmpty** → Check if queue is empty.
5. **Size** → Number of elements.

---

### ✅ Implementing Queue with Python List

```python
queue = []

# Enqueue (add to rear)
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueue:", queue)  # [10, 20, 30]

# Dequeue (remove from front)
front = queue.pop(0)  # removes 10
print("Dequeued:", front)
print("Queue after dequeue:", queue)  # [20, 30]

# Peek (front element)
print("Front element (peek):", queue[0])  # 20

# Size
print("Size of queue:", len(queue))  # 2

# isEmpty
print("Is queue empty?", len(queue) == 0)  # False

```

⚠️ Problem: `pop(0)` is **O(n)** because it shifts all elements left.

That’s inefficient for large queues.

---

### 🚀 Better: Using `collections.deque`

`deque` (double-ended queue) is optimized for fast appends and pops from both ends.

```python
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueue:", queue)  # deque([10, 20, 30])

# Dequeue
print("Dequeued:", queue.popleft())  # 10
print("Queue after dequeue:", queue)  # deque([20, 30])

# Peek
print("Front element (peek):", queue[0])  # 20

# Size
print("Size:", len(queue))  # 2

# isEmpty
print("Is empty?", len(queue) == 0)  # False

```

---

### 🎯 Summary

- **Stack** → LIFO (Last in, First out).
- **Queue** → FIFO (First in, First out).
- Python **list** can implement both, but inefficient for queues if using `pop(0)`.
- `collections.deque` is the **best choice** for queues (and even stacks).

- **Sample exercse to practice these principles**
    
    To practice these principles, you can build two small simulations: a **Browser Navigation System** (Stack) and a **Customer Support Ticket System** (Queue).
    
    **Exercise 1: The Stack Challenge (Browser History)**
    
    **Problem:** Build a system that tracks your web browsing history so you can go "Back" to previous pages.
    
    - **The Goal:** Use a list to store visited URLs.
    - **Operations:**
        1. `visit(url)`: Adds a new page to your history.
        2. `back()`: Removes the current page and returns the previous one.
        3. `show_current()`: Shows the page you are currently on.
    
    **Practice Script:**
    
    ```python
    history = []
    
    def visit(url):
        history.append(url)  # PUSH onto stack
        print(f"Visiting: {url}")
    
    def back():
        if len(history) > 1:
            history.pop()    # POP from stack
            print(f"Went back to: {history[-1]}")
        else:
            print("Cannot go back. This is your first page.")
    
    # TRY THIS:
    visit("google.com")
    visit("github.com")
    visit("openai.com")
    back()  # Should take you back to github.com
    ```
    
    Use code with caution.
    
    ---
    
    **Exercise 2: The Queue Challenge (Support Desk)**
    
    **Problem:** Create a system for a customer service desk where customers are served in the order they arrive.
    
    - **The Goal:** Use `collections.deque` for high performance.
    - **Operations:**
        1. `add_customer(name)`: Adds a person to the end of the line.
        2. `serve_customer()`: Removes the first person from the line and serves them.
    
    **Practice Script:**
    
    ```python
    from collections import deque
    
    service_line = deque()
    
    def add_customer(name):
        service_line.append(name) # ENQUEUE at back
        print(f"{name} joined the line.")
    
    def serve_customer():
        if service_line:
            served = service_line.popleft() # DEQUEUE from front
            print(f"Now serving: {served}")
        else:
            print("No customers in line.")
    
    # TRY THIS:
    add_customer("Alice")
    add_customer("Bob")
    serve_customer() # Should serve Alice first
    add_customer("Charlie")
    serve_customer() # Should serve Bob next
    ```
    
    Use code with caution.
    
    **Bonus Challenge: The "Palindrome Checker"**
    
    Use both together!
    
    1. Take a word (e.g., `"racecar"`).
    2. **Push** every letter into a **Stack** and **Enqueue** every letter into a **Queue**.
    3. **Pop** and **Dequeue** them one by one.
    4. If they match every single time, the word is a palindrome because a Stack reverses the order while a Queue preserves it.

