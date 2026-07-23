## **What is a Function?**

A **function** is a reusable block of code that performs a specific task.

Think of it like a **machine**:

- You give it **input** (parameters).
- It does some **processing**.
- It may give you **output** (return value).

Why use functions?

- **Reusability** → Write once, use many times.
- **Readability** → Makes code easier to understand.
- **Maintainability** → Change one place instead of multiple spots.

Example:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Mikiyas")
greet("Sara")
```

### **Defining and Calling Functions**

**Syntax:**

```python
def function_name(parameters):
    """Optional docstring explaining the function."""
    # code block
    return value  # optional
```

Steps:

1. Use the `def` keyword.
2. Give your function a **name** (follow snake_case convention).
3. Add parentheses `()` for parameters (or empty if none).
4. Use a **colon** `:`.
5. Indent the function body.
6. Optionally use `return` to send a value back.

Example:

```python
def add(a, b):
    return a + b

result = add(4, 5)  # result = 9
```

### **Function Parameters**

#### **Positional Parameters**

Order matters:

```python
def subtract(a, b):
    return a - b

print(subtract(10, 3))  # 7
```

#### **Default Parameters**

Give parameters default values:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Hello, Guest!
greet("Sara")  # Hello, Sara!
```

💡 Default values are evaluated **only once** at function definition time — be careful with mutable defaults like lists.

- **More on default params**
    
    **The Problem: Persistent State**
    
    In Python, default arguments are evaluated only **once**—at the exact moment the function is defined, not every time it is called. If you use a mutable object as a default, every call to that function will share the **same single object** in memory.
    
    If you modify that default object inside the function, those changes will persist for all subsequent calls.
    
    **Example of the "Trap":**
    
    **python**
    
    ```python
    def add_item(name, items=[]): # items=[] is created ONCE at definition
        items.append(name)
        return items
    
    print(add_item("Apple"))  # Output: ["Apple"]
    print(add_item("Banana")) # Output: ["Apple", "Banana"] (Wait, what?)
    ```
    Instead of starting with a fresh empty list, the second call reused the list that already contained "Apple".
    
    **The Solution: Use `None`**
    
    The standard "Pythonic" way to handle mutable defaults is to use `None` as the default value and then initialize the mutable object inside the function body.
    
    **Correct Implementation:**
    
    **python**
    
    ```python
    def add_item(name, items=None):
        if items is None:
            items = []  # A new list is created every time the function is called
        items.append(name)
        return items
    
    print(add_item("Apple"))  # Output: ["Apple"]
    print(add_item("Banana")) # Output: ["Banana"] (Correct!)
    ```
    
    **When is it actually used?**
    
    While usually avoided, this behavior is sometimes used intentionally to create a **persistent cache** or "static" variable that stays alive between function calls without using a global variable. However, for most beginners and standard applications, this is an anti-pattern that causes hard-to-find errors.
    

### **Keyword Arguments**

Order doesn’t matter when using parameter names:

```python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Mikiyas")
```

---

### **Return Values**

If you don’t specify `return`, Python returns `None`.

```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)  # 12
```

Multiple returns:

```python
def stats(numbers):
    return min(numbers), max(numbers)

low, high = stats([2, 8, 4])
print(low, high)  # 2 8
```

### **Arbitrary Arguments**

When you don’t know how many arguments will be passed:

### **`args` (Positional)**

**What is `args`?**

- `args` allows a function to accept **any number of positional arguments**
- Inside the function, `args` is a **tuple**

```python
def demo(*args):
	print(args)  # (1, 2, 3, 4)
	print(type(args))  # <class 'tuple'>
```

**2.3 Looping Through `args`**

```python
def total(*args):
    result =0
    for num in args:
        result += num
    return result

print(total(1,2,3,4)) # 10

def greet(*args):
    print("Arguments:", args) 
    for name in args:
        print(f"Hello, {name}!")

greet("Mikiyas", "Alex", "Sara")

# Outputs
# Arguments: ('Mikiyas', 'Alex', 'Sara')
# Hello, Mikiyas!
# Hello, Alex!
# Hello, Sara!
```

**2.4 `args` with One or No Arguments**

```python
demo(10)# (10,)
demo()# ()

# ✔ Still a tuple
# ✔ No errors
```

Collects extra arguments into a **tuple**:

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
```

### **`**kwargs` (Keyword)**

**What is `*kwargs`?**

- `*kwargs` allows **any number of named arguments**
- Inside the function, `kwargs` is a **dictionary**

```python
def demo(**kwargs):
	print(kwargs)
	print(type(kwargs))

demo(name="Mike", role="QA", experience=2)

# outputs
# {'name': 'Mike', 'role': 'QA', 'experience': 2}
#<class 'dict'>

def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Mikiyas", age=25, country="Israel")

#OUTPUTS
```

**3.3 Accessing Values**

```python
defgreet(**kwargs):
	print("Hello", kwargs["name"])

greet(name="Mike")
```

**3.4 Safe Access (`get()`)**

```python
defgreet(**kwargs):
print("Hello", kwargs.get("name","Guest"))
```

**Collects extra keyword arguments into a dictionary:**

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Mikiyas", age=25, country="Israel")

```

#### **Using Both Together**

You can combine them:

```python
def profile(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

profile("Mikiyas", "QA Engineer", age=25, country="Israel")

# OUTNPUT
# Positional arguments: ('Mikiyas', 'QA Engineer')
# Keyword arguments: {'age': 25, 'country': 'Israel'}
```

#### Argument Unpacking with  and `*`

You can also use them when **calling** a function:

```python
def add(a, b, c):
    return a + b + c

nums = (1, 2, 3)
print(add(*nums))  # 6

params = {"a": 4, "b": 5, "c": 6}
print(add(**params))  # 15

```

#### **Rules of Argument Order**

The order in a function definition must be:

```
1. Normal arguments
2. *args
3. Default arguments
4. **kwargs

```

Example:

```python
def func(a, b, *args, d=10, **kwargs):
    print(a, b, args, d, kwargs)

func(1, 2, 3, 4, 5, d=20, x=100, y=200)

# OUTPUT
# 1 2 (3, 4, 5) 20 {'x': 100, 'y': 200}

```

#### **Real-Life Example**

Imagine a logging function:

```python
def log_message(level, *args, **kwargs):
    print(f"[{level}] -", " ".join(map(str, args)))
    for key, value in kwargs.items():
        print(f"{key} = {value}")

log_message("INFO", "User", "logged", "in", user_id=123, ip="192.168.1.1")

# OUTPUT
# [INFO] - User logged in
# user_id = 123
# ip = 192.168.1.1
```

### **Functions as First-Class Citizens**

Python treats functions like any other object:

- Assign to variables
- Pass as arguments
- Return from other functions
- Store them in data structures (lists, dictionaries, etc.)
- Create them at runtime

Example:

```python
# pass them as an argument
def shout(text):
    return text.upper()

def speak(func, message):
    print(func(message))

speak(shout, "hello")  # HELLO

# Assign them to avariable

def greet():
    print("Hello!")

say_hello = greet

say_hello()

# Return from other functions

def outer():

    def inner():
        print("Inside inner")

    return inner

# Storing them in a list

def add():
    print("Add")

def subtract():
    print("Subtract")

operations = [add, subtract]

operations[0]()
operations[1]()

# Storing them in a dict

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

calculator = {
    "+": add,
    "*": multiply
}

print(calculator["+"](3, 4))
print(calculator["*"](3, 4))

```

---

### **Nested Functions**

Functions inside functions:

```python
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()
```

💡 Inner functions can **access variables** from the outer function (closure).

---

### **Lambda Functions**

Short, anonymous functions:

```python
square = lambda x: x * x
print(square(5))  # 25

```

Best used for small, simple operations (often with `map`, `filter`, `sorted`).

- **More on Lambda function**
    
    **a lambda function is a small, anonymous function that can be defined in a single line**. It is called "anonymous" because it is often used without a name.
    
    **1. Syntax**
    
    The syntax is straightforward but strict:
    
    **python**
    
    `lambda arguments: expression`
    
  - **`lambda`**: The keyword that starts the function.
  - **`arguments`**: The inputs (comma-separated, just like normal functions).
  - **`expression`**: A single piece of logic that is evaluated and automatically **returned**. You can not use multiple lines or statements (like `pass` or `assert`) inside a lambda.
    
  **2. Basic Example**
    
  Here is a comparison between a standard function and a lambda:
    
  **Standard Function:**
    
  ```python
  def square(x):
    return x * x
  ```
    
  **Lambda Version:**
    
  ```python
  square = lambda x: x * x
    
  print(square(5)) # Output: 25
  ```
    
  **3. When should you use them?**
    
  Lambdas are best used as **"throwaway" functions**—small pieces of code that you only need for a moment, usually as an argument to another function.
    
  **A. Sorting with a Key**
    
  This is the most common use case. For example, sorting a list of tuples by the second value:
    
  **python**
    
  ```python
  students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
  # Sort by age (the index 1 of each tuple)
  students.sort(key=lambda student: student[1])
    
  print(students) # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
  ```
    
  Use code with caution.
    
  **B. Using with `map()` and `filter()`**
    
  - **`filter`**: Keep items that meet a condition.
        
    **python**
        
    ```python
    nums = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4, 6]
    ```
        
    Use code with caution.
        
  - **`map`**: Transform every item in a list.
        
    **python**
        
    ```python
    doubled = list(map(lambda x: x * 2, nums)) # [2, 4, 6, 8, 10, 12]
    ```
        
    **4. Important Limitations**
    
    While powerful, lambdas have drawbacks:
    
    1. **Readability:** Complex lambdas are harder to read than named functions. If the logic is more than a simple calculation, use `def`.
    2. **No Multiple Expressions:** You can only do one thing. You can not have a lambda that performs an `if/else` block with multiple print statements, for example.
    3. **Debugging:** Because they don't have a name, error messages (tracebacks) will simply say `<lambda>`, making it harder to find which one failed in complex code.
    
    **Summary**
    
    Think of **`def`** as a permanent tool in your toolbox and a **`lambda`** as a piece of tape you use once to fix a specific, small problem and then throw away.
    

### **Docstrings**

For documenting your function:

```python
def greet(name):
    """This function greets the person whose name is passed."""
    print(f"Hello, {name}!")

print(greet.__doc__)
```

💡 Docstrings help tools like Sphinx or IDEs show function descriptions.

---

### **Recursion**

A function calling itself — useful for problems that break into smaller subproblems.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

⚠️ Be careful — recursion needs a **base case** to stop, otherwise it causes infinite recursion.

- **More on Recursion**
    
    The Simple Example: Factorial
    
    This calculates
    
    [](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
    
    n×(n−1)×(n−2)…n cross open paren n minus 1 close paren cross open paren n minus 2 close paren …
    
    𝑛×(𝑛−1)×(𝑛−2)…
    
   ```python
    def factorial(n):
        # 1. Base Case: If n is 1, stop the recursion
        if n <= 1:
            return 1
        
        # 2. Recursive Step: Multiply n by the result of factorial(n-1)
        else:
            return n * factorial(n - 1)
    
    # Usage
    print(factorial(5)) # Output: 120 (5 * 4 * 3 * 2 * 1)
    ```
    
2. The Real-World Example: Searching Folders
    
   Recursion is the gold standard for "tree-like" structures, such as folders on a computer that contain subfolders.
    
   python
    
   ```python
   import os
    
   def find_file(filename, search_path):
       """
       Recursively searches for a file in a directory and its subdirectories.
       """
       for item in os.listdir(search_path):
           full_path = os.path.join(search_path, item)
            
           # Base Case A: We found the file!
           if item == filename:
               print(f"Found at: {full_path}")
               return full_path
            
           # Recursive Step: If it's a directory, search inside it
           if os.path.isdir(full_path):
               found = find_file(filename, full_path)
               if found:
                   return found
    
       return None # Base Case B: File not found in this branch
   ```
    
   1. Visualization: The Call Stack
    
       To understand what happens in memory, imagine the **Stack** for `factorial(3)`:
    
   1. **Call `factorial(3)`**: Computer asks, *"What is 3 * factorial(2)?"* (Wait...)
   2. **Call `factorial(2)`**: Computer asks, *"What is 2 * factorial(1)?"* (Wait...)
   3. **Call `factorial(1)`**: Computer hits the **Base Case** and returns **1**.
   4. **Unwinding**:
       - `factorial(2)` now has the answer: `2 * 1 = 2`.
       - `factorial(3)` now has the answer: `3 * 2 = 6`.
    
   Important Rule for Developers:
    
   If you are writing recursive code in **JavaScript** or **Python**, always ensure your **Base Case** is reachable. Without it, you will trigger a `RecursionError` (Python) or `RangeError: Maximum call stack size exceeded` (JavaScript), commonly known as a **Stack Overflow**.
    

### **Best Practices**

- One function = one responsibility.
- Avoid deeply nested functions unless necessary.
- Use clear names (`calculate_tax` not `ct`).
- Write docstrings for clarity.
- Test your functions with different inputs.

## Advanced Things About Functions in Python

### 1. **Lambda Functions (Anonymous Functions)**

- Functions without a name, usually one line.

```python
square = lambda x: x ** 2
print(square(5))  # 25

```

✅ Good for short, throwaway functions (often used with `map`, `filter`, `sorted`).

---

### 2. **Higher-Order Functions**

- Functions can accept other functions as arguments or return them.

```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x*2, 5))  # 10

```

✅ Example: `map()`, `filter()`, `reduce()` are higher-order functions.

**1. `map(function, iterable)` — The Transformer**

Use `map` when you want to **apply the same change to every item** in a collection. It returns a "map object" (an iterator), so you usually wrap it in `list()` to see the results.

- **Logic:** It "maps" each input to exactly one output.
- **Example:** Squaring every number in a list.
    
    **python**
    
    ```python
    nums = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, nums))
    # Result: [1, 4, 9, 16]
    ```
    
    Use code with caution.
    

**2. `filter(function, iterable)` — The Gatekeeper**

Use `filter` when you want to **extract items** that meet a specific condition. The function you provide must return `True` or `False`.

- **Logic:** Only items that return `True` stay; the rest are discarded.
- **Example:** Keeping only even numbers.
    
    **python**
    
    ```python
    nums = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, nums))
    # Result: [2, 4, 6]
    ```
    
    Use code with caution.
    

**3. `reduce(function, iterable)` — The Summarizer**

Unlike the others, `reduce` is not a built-in; you must import it from the functools module. It **collapses an entire list into a single value**.

- **Logic:** It applies the function to the first two items, takes that result and applies it to the third item, and so on until only one value remains.
- **Example:** Multiplying all numbers together.
    
    **python**
    
    ```python
    from functools import reduce
    
    nums = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, nums)
    # Step-by-step: ((1*2)*3)*4 = 24
    ```
    
    Use code with caution.
    

### 3. **Closures**

- A function can **remember variables** from the enclosing scope.

```python
def outer(multiplier):
    def inner(x):
        return x * multiplier
    return inner

double = outer(2)
print(double(5))  # 10
```

✅ Used in decorators and factory functions.

---

### 4. **Decorators**

- Special functions that **wrap another function** to add extra behavior.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(2, 3))
```

✅ Often used in logging, authentication, caching.

---

### 5. **Recursion**

- A function that calls itself.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
```

✅ Useful for problems like factorial, Fibonacci, tree traversal.


### 6. **Generators (`yield`)**

- Functions that **produce a sequence of values lazily**.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

✅ More memory-efficient than returning a list.

### 7. **Function Annotations (Type Hints)**

- You can specify expected argument and return types.

```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old!"
```

✅ Makes code clearer; helpful for tools like `mypy`.

### 8. **Partial Functions**

- Using `functools.partial`, you can pre-fill some function arguments.

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(5))  # 25
```

### 9. **First-Class Citizens**

- Functions in Python are **first-class objects**:
    - You can assign them to variables
    - Store them in lists/dictionaries
    - Pass them as arguments
    - Return them from other functions

```python
def hello():
    return "Hello"

greet = hello  # assign
print(greet())  # Hello

```

### 10. **Docstrings**

- You can document a function with triple quotes:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(add.__doc__)

```

✅ So yes — there’s still a lot beyond the basics:

- **Lambdas**
- **Higher-order functions**
- **Closures**
- **Decorators**
- **Recursion**
- **Generators (`yield`)**
- **Type hints**
- **Partial functions**
- **Functions as first-class citizens**
- **Docstrings (documentation)**