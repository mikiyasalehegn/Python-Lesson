## Generators In Python

A **Generator Object** is a special type of Python "iterable" (like a list or a tuple) that produces its values one at a time, **only when you ask for them**.

In most cases, when you create a list, Python stores every single item in your computer's memory immediately. A generator, however, stores the **instructions** for how to create the items, but it doesn't create them until you actually loop over it.
To sumup generator is an object produces values one at a time, remember where it stops, and continue when asked again.

#### How a Generator Object is Created

A generator object is created by a function that contains at least one **`yield`** statement.

#### How a Generator Object is Created

A generator object is created by a function that contains at least one **`yield`** statement.

```python
def simple_generator():
    print("Step 1")
    yield "First Value"
    
    print("Step 2")
    yield "Second Value"

# This DOES NOT run the code inside the function yet!
# It just creates the "Generator Object"
my_gen = simple_generator()

print(my_gen) # Output: <generator object simple_generator at 0x...>
```

#### How to "Use" the Object

Because it is a "lazy" object, you have to trigger it to get the values. You can do this in two ways:

**A. Using a `for` loop (The most common way)**
```python
for value in my_gen:
    print(value)

# **OUTPUT**
# Step 1
# First Value
# Step 2
# Second Value
```

**B. Using the `next()` function**

This is where the "Pause" and "Resume" magic happens.

1. When you call `next(my_gen)`, it runs the code until it hits `yield`, gives you the value, and **pauses**.
2. When you call `next()` again, it wakes up at the exact spot it left off and continues.

```python
def sample_gen():
    print('step 1')
    yield 1

    print('step 2')
    yield 2

steps = sample_gen()
next(steps) # step 1 and yield 1
next(steps) # # step 2 and yield 2

```
**C. Generator Expressions**

If your generator logic fits on a single line, you can write a generator expression. They look exactly like list comprehensions but use parentheses () instead of square brackets [].
```python
# List comprehension (Saves everything in memory immediately)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (Computes each number only when asked)
squares_gen = (x**2 for x in range(1000000))

print(next(squares_gen))  # Outputs: 0
print(next(squares_gen))  # Outputs: 1
```

### Example

Imagine the API returns:

``` python
[
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]
```

Instead of returning the whole list, we can create a generator.

```python
import requests

def get_users():
    response = requests.get("https://example.com/api/users")
    users = response.json()

    for user in users:
        yield user

# Now use it:

for user in get_users():
    print(user["name"])

# Output:
# Alice
# Bob
# Charlie
```


## What is an iterator?

An iterator is an object that allows you to get elements from a collection one at a time.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```
where Python already has the whole list in memory, an iterator gives values one by one.

### Iterables vs. Iterators

It is easy to confuse these two terms, but they have distinct definitions in Python:

- **Iterable:** An object that has a `__iter__()` method which returns an *iterator*, or supports sequence behavior (like `__getitem__()`). Examples: `list`, `tuple`, `str`, `dict`, `set`.
- **Iterator:** An object that has a `__next__()` method, which returns the *next* item in the stream, and raises a `StopIteration` exception when there are no more items left. An iterator also remembers its state (where it currently is in the sequence).

> **Rule of Thumb:** Every iterator is also an iterable (because it implements `__iter__`), but not every iterable is an iterator (a `list` is an iterable, but calling `next()` directly on a list will fail).

### The Iterator Protocol

Under the hood, Python uses the **Iterator Protocol** whenever you run a `for` loop, unpack variables, or use functions like `max()` or `sum()`.

When you loop over an iterable:

1. Python calls `iter()` on the object to get an **iterator**.
2. Python repeatedly calls `next()` on that iterator to get the next item.
3. When `next()` raises a `StopIteration` exception, the loop terminates automatically.

```python
my_list = [10, 20, 30]

# 1. Get an iterator from the iterable
my_iterator = iter(my_list)

# 2. Fetch items one by one using next()
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30

# 3. Calling next() again raises StopIteration
print(next(my_iterator))  # Raises StopIteration:
```
### Why Use Iterators? (Benefits)

- **Memory Efficiency (Lazy Evaluation):** Standard lists load all their elements into memory at once. Iterators compute or fetch elements *on demand* (lazily). This is essential when working with massive datasets or infinite streams where holding everything in memory would crash your program.
- **One-Way Traffic:** Iterators can only move forward. You cannot reset an iterator or go backward. Once exhausted, you must create a new iterator object.

## Creating a Custom Iterator

To create a custom iterator, you need to define a class with two special methods:

1. `__iter__()`: Returns the iterator object itself (`self`).
2. `__next__()`: Returns the next value and raises `StopIteration` when the sequence ends.

#### Example: Custom Countdown Iterator
```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Using the custom iterator
counter = Countdown(3)

for num in counter:
    print(num)

# Output:
# 3
# 2
# 1
```
### Generators: The Pythonic Way to Create Iterators

Writing a full class with `__iter__` and `__next__` can be tedious. Python provides a much simpler way to create iterators called **generators** using the `yield` keyword instead of `return`.

When a function contains `yield`, Python treats it as a generator function. It automatically implements the iterator protocol for you!

#### Example: Generator Countdown

```python
def countdown_gen(start):
    while start > 0:
        yield start
        start -= 1

# Using the generator
for num in countdown_gen(3):
    print(num)

# Output:
# 3
# 2
# 1
```

### How `for` Loops Work with Iterators

When you write a `for` loop in Python, the loop itself isn't an iterator, but it **uses** the iterator protocol behind the scenes to step through collections.

For example, when you write:
```python
numbers = [1, 2, 3]
for num in numbers:
    print(num)
```

Python executes these steps automatically:

1. Calls `iter(numbers)` to get an **iterator** from the list.
2. Repeatedly calls `next()` on that iterator to get each item.
3. Assigns the returned item to the loop variable (`num`).
4. Catches the `StopIteration` exception and safely exits the loop when the data runs out.

Key takeaway: A for loop is simply a clean, automated wrapper around an iterator.

### Real Life Analogy

To tie everything together, let's look at these concepts through the lens of a **Music Playlist and a Music Player**.

#### 1. The Iterable: The Spotify Playlist

- **Analogy:** A full playlist saved in your library containing 500 songs.
- **What it is:** The complete collection. You can look at the whole list from top to bottom, share the entire thing with a friend, or loop back to the beginning whenever you want.
- **Python equivalent:** A `list`, `tuple`, or `string`.

#### 2. The Iterator: The "Now Playing" Queue & Pointer

- **Analogy:** The active music player app tracking your current listening session.
- **What it is:** When you hit play, the player doesn't dump all 500 songs into your ears at once. It tracks a **single pointer** telling you: *"Song 1 just played, Song 2 is playing right now, and Song 3 is next."* Once you reach the end of the playlist, the player stops. You can't easily go backward without restarting the queue.
- **Python equivalent:** An object created by `iter()` that holds its state and gives you values one-by-one via `next()`.

#### 3. The Generator: A Live DJ / On-the-Fly Composer

- **Analogy:** Instead of downloading a massive 10GB file containing 1,000 pre-recorded songs, you hire a live DJ.
- **What it is:** The DJ doesn't pre-write a giant album. They stand on stage, take a breath, and **invent and play the next song only when you ask for it**. This saves an incredible amount of space because they don't need to store a massive file—they just compute the next track on the spot.
- **Python equivalent:** A function using `yield` that pauses, calculates the next value on demand, and resumes when asked.

## Decorators

A **decorator** is a powerful design pattern in Python that allows you to modify or extend the behavior of a function or method **without permanently changing its source code**.

Think of a decorator like **gift wrapping**: the core gift (the original function) stays exactly the same, but you add a wrapper around it to give it extra flair, security, or functionality before it gets handed to the recipient.

### How Python Views Functions

To understand decorators, you first need to remember that **functions in Python are first-class citizens**. This means functions can:

- Be passed around as arguments.
- Be returned from other functions.
- Be assigned to variables.

A decorator is simply a function that takes *another* function as an argument, adds some code around it, and returns a *new* wrapped function.

#### A Simple Example

Imagine you want to log every time a function is called, without modifying the function's actual code.

### Writing a Decorator
```python
def my_decorator(func):
    def wrapper():
        print("--- Something is happening BEFORE the function runs ---")
        func()  # Call the original function
        print("--- Something is happening AFTER the function runs ---")
    return wrapper
```

**Using the @ Syntactic Sugar:**
Python provides a shortcut for decorators using the @ symbol placed right above the target function definition:

```python
@my_decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()

# Output
# --- Something is happening BEFORE the function runs ---
# Hello, World!
# --- Something is happening AFTER the function runs ---

```
Behind the scenes, writing @my_decorator right above say_hello is just shorthand for writing:
say_hello = my_decorator(say_hello).

## Decorators with Arguments

Often, the functions you want to decorate need to accept arguments (like usernames, numbers, etc.). To handle this, your inner `wrapper` function must accept `*args` and `**kwargs` and pass them along to the original function:

```python
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function finished. Result: {result}")
        return result
    return wrapper

@log_arguments
def add(a, b):
    return a + b

add(5, 10)

# OUTPUT
# Calling function 'add' with arguments: (5, 10), {}
# Function finished. Result: 15
```


