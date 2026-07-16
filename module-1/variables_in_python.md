# Basics Of Python

Python is a **high-level, interpreted programming language** known for its **simplicity, readability, and versatility**.

- **Use cases**:
    - Web development (e.g., Django, Flask)
    - Data science & machine learning (e.g., Pandas, NumPy, TensorFlow)
    - Automation & scripting
    - Game development
    - Desktop apps
    - API development
- **Why it’s popular**:
    - Easy to learn for beginners
    - Massive community & libraries
    - Works across multiple platforms (Windows, macOS, Linux)

**Note:**

**High-level** means the language is **closer to human language** and **abstracted from the computer's hardware details**.

In an **interpreted language**, code is executed **line-by-line** by an **interpreter** (in Python’s case, the Python interpreter).

- No need to compile the entire program into machine code before running it — you just run the file.
- This makes testing and development faster, but can be slower than compiled languages.

💡 **Analogy**:

- **High-level** = Writing a recipe in plain English.
- **Interpreted** = Having a translator read the recipe to the chef **one step at a time** as they cook.
- **Compiled** = Translating the whole recipe into the chef’s language *before* they start cooking.

### **What a Compiler Does**

A **compiler** is a program that takes your **source code** (written in a high-level language like C++ or Java) and **translates it into machine code** (binary instructions: 0s and 1s) that the CPU can execute directly.

Unlike an interpreter, which runs code line-by-line, a compiler **translates the entire program at once** before running it.

### Code Editor Vs IDE

#### **1. Code Editor**

A **code editor** is basically a **text editor made for writing code**. A **code editor** is a software tool where you **write, edit, and manage programming code**.

Think of it like a **specialized text editor** made specifically for programmers — similar to how Google Docs is for writing text, but a code editor is built for writing code

- It highlights syntax (keywords, variables, etc.).
- It might give you some auto-completion.
- It’s lightweight and fast, but you usually need to run code using another tool.

**Examples**:

- Visual Studio Code (VS Code)
- Sublime Text
- Atom

💡 **Think of it as**: A notebook made for coders — you can write code easily, but it won’t cook the meal for you.

---

#### **2. IDE (Integrated Development Environment)**

An **IDE** is like a **full coding workshop** — that helps you **write, run, test, and debug code. I**t includes a code editor **plus** built-in tools for:

- Compiling / running your code
- Debugging (step-by-step error tracing)
- Version control integration (Git)
- Project/file management
- Code refactoring tools
- Built-in terminal/console

**Examples**:

- PyCharm (Python)
- IntelliJ IDEA (Java, Kotlin)
- Eclipse (Java, C++)
- Visual Studio (C#, C++)

💡 **Think of it as**: A full kitchen with all tools — knives, oven, microwave, spices — ready to prepare and serve the dish.

## Variables

### What Is Memory?

Your computer’s **memory (RAM)** is like a huge grid of tiny boxes.

Each box has:

- an **address** (a number)
- a **value** (data stored there)

A **variable** is like a **named container** that stores data in your computer’s memory, so you can use and change that data later.

- The **name** is what you call it in your code.
- The **value** is the actual data it stores.

Example in Python:

```python
python
CopyEdit
age = 25

```

- `age` → variable name
- `25` → value stored in it

Example:

```python
x =10

```

What happens:

- `10` is stored in memory
- `x` is a **label** pointing to where `10` lives

Think of it like:

```
Memory address:0x100→10
Variable name:x→points to 0x100
```

---

### Variables Are References (Most Languages)

In many modern languages, variables **reference** data instead of “holding” it directly.

Example:

```python
a =5
b = a

```

Memory view:

```
a ─┐
   ├──>5
b ─┘

```

Both `a` and `b` point to the **same value**.

---

### Changing a Variable

```python
a =5
a =8

```

What happens:

- `5` stays in memory (temporarily)
- `a` now points to a **new location** with `8`

```
Before: a → 5
After:  a → 8

```

The old `5` will be removed later by **garbage collection** if nothing uses it.

### **Why Use Variables?**

- To store data for reuse.
- To make code **readable** and **maintainable**.
- To work with **dynamic data** (data that changes).

### **How Variables Work in Memory**

When you create a variable:

1. The computer **allocates memory** to store the value.
2. The variable name is like a **label** that points to that memory location.
3. You can change what it points to by assigning a new value.

Example:

```python
python
CopyEdit
x = 10   # x points to a memory location holding 10
x = 20   # now x points to a different location holding 20

```

### **Variable Types**

Different languages handle types differently:

- **Statically typed** (e.g., Java, C++): You must declare the type before use.
    
    ```java
    java
    int age = 25;
    
    ```
    
- **Dynamically typed** (e.g., Python, JavaScript): The type is decided at runtime.
    
    ```python
    age = 25       # integer now
    age = "twenty" # string now, no problem
    ```
    

### **Creating Variables in Python**

In Python, you **don’t** need to declare the type — just assign a value, and Python figures it out:

```python
name = "Alice"   # string
age = 25         # integer
height = 1.75    # float
```

- **Dynamic typing** → You can change the type later:
    
    ```python
    x = 10
    x = "ten"  # now a string
    ```
    

### **Naming Rules (Python-specific)**

- Can use letters, digits, and underscores (`_`).
- Must **start with** a letter or `_`, not a digit.
- Case-sensitive (`Name` ≠ `name`).
- Avoid Python keywords (`if`, `class`, `def`, etc.).


### What Is Variable Scope?

**Scope** defines **where a variable can be accessed** in your code.

In Python, variables live in different “zones”, and each zone has rules.

**Python’s Scope Rule: LEGB**

Python looks for variables in this order:

**L → E → G → B**

| Level | Name | Meaning |
| --- | --- | --- |
| **L** | Local | Inside the current function |
| **E** | Enclosing | Inside outer (non-global) functions |
| **G** | Global | Defined at the top level of the script |
| **B** | Built-in | Python’s built-in names |

---

**1️⃣ Local Scope (L)**

Variables created **inside a function**.

```python
def greet():
    msg ="Hello"
print(msg)

greet()
# print(msg)  ❌ NameError
```

✔ `msg` exists **only inside** `greet()`.

---

**2️⃣ Enclosing Scope (E)**

Occurs with **nested functions**.

```python
def outer():
    x ="outer"
    def inner():
        print(x)
    inner()

outer()
```

✔ `inner()` can access `x` from `outer()`.

---

**3️⃣ Global Scope (G)**

Variables defined **outside all functions**.

```python
count =10

def show():
    print(count)

show()
```

✔ Functions can **read** global variables.

---

**⚠️ Common Mistake with Globals**

```python
x =5

def change():
    x =10 # creates a NEW local variable
    print(x)

change() # 10
print(x) # 5
```

---

**4️⃣ `global` Keyword**

Use `global` to **modify** a global variable inside a function.

```python
x =5

def change():
    global x
    x =10

change()
print(x) #10
```

⚠️ Use sparingly — globals make code harder to maintain.

---

**5️⃣ `nonlocal` Keyword (Enclosing Scope)**

Used for **nested functions** to modify enclosing variables.

```python
def outer():
    x =5
    def inner():
        nonlocal x
        x =10
    inner()
    print(x)

outer() # 10
```

---

**6️⃣ Built-in Scope**

Python provides built-in names like:

```python
print()
len()
sum()
range()
```

Example:

```python
print(len("Python"))# 6
```

⚠️ Avoid overwriting built-ins:

```python
len =10
print(len("abc"))# ❌ TypeError
```

---

**🔄 Scope vs Lifetime**

- **Scope** → where a variable is visible
- **Lifetime** → how long it exists in memory

```python
def func():
    x =10

func()
# x is gone here
```

---

**7️⃣ Loop Scope (Important!)**

Python does **not** create a new scope for loops.

```python
for i in range(3):
    pass

print(i)# 2
```

Same for `if` blocks.

---

**8️⃣ Comprehension Scope (Special Case)**

List, dict, set comprehensions **do create their own scope**.

```python
x =10
lst = [x for x in range(3)]
print(x)# 10
```

---

**9️⃣ Function Parameters Are Local**

```python
def add(a, b):
    return a + b

# a and b exist only inside add()
```

---

**🧠 Common Scope Errors**

❌ UnboundLocalError

```python
x =5

def f():
    print(x)
    x =10

f()
```

Why?

- Python sees `x = 10`
- Treats `x` as local
- But it’s used before assignment

---

✅ Fix

```python
def f():
    global x
    print(x)
    x =10
```

**🔑 Golden Rules to Remember**

✔ Functions create **new scopes**

✔ Loops do **not**

✔ Assignment makes variables **local by default**

✔ Use `global` and `nonlocal` carefully

✔ Python resolves names using **LEGB**

**🧩 Simple Mental Model**

Think of scopes as **nested boxes** 📦

Python looks **from the smallest box outward** until it finds the variable.

### **Constants in Python**

Python has no true constant variables — by convention, we use **ALL_CAPS**:

```python
PI = 3.14159
```

(But technically, you can still reassign it — Python just trusts you not to.)

### **Mutable vs Immutable Variables**

This is a big one in Python 🔥.

- **Immutable types** → Can’t be changed after creation (int, float, str, tuple).
    
    ```python
    x = "hello"
    x.upper()      # returns new string, doesn't change x
    print(x)       # "hello"
    ```
    
- **Mutable types** → Can be changed without creating a new object (list, dict, set).
    
    ```python
    my_list = [1, 2, 3]
    my_list.append(4)  # modifies existing list
    print(my_list)     # [1, 2, 3, 4]
    ```
    

### **Multiple Assignments**

Python lets you assign multiple variables in one line:

```python
a, b, c = 1, 2, 3
```

Or give multiple names the same value:

```python
x = y = z = 0
```
### **Variables Are References in Python**

This trips up beginners.

When you assign a variable, Python stores the **reference** (address in memory) to the object, not the object itself.

Example:

```python
a = [1, 2]
b = a  # both point to the same list
b.append(3)
print(a)  # [1, 2, 3] — a also changed!
```

To avoid this, **copy** the list:

```python
b = a.copy()
```

### **Unpacking in Python**

You can extract values from lists, tuples, and other iterables directly into variables:

```python
name, age, country = ("Alice", 25, "USA")
```

With the `*` operator, you can grab "the rest":

```python

first, *middle, last = [1, 2, 3, 4, 5]
print(middle)  # [2, 3, 4]

*first, last = [1, 2, 3, 4, 5]
print(last) # 5
print(first) # [1, 2, 3, 4]

first, *rest = [1, 2, 3, 4, 5]
print(first) # 1
print(rest) # [2, 3, 4, 5]
```

---

### **Deleting Variables**

You can remove a variable with `del`:

```python
x = 100
del x
# print(x)  # ❌ NameError

```

---

### **Type Hints (Optional)**

Python allows **type annotations** to make code more understandable:

```python
age: int = 25
name: str = "Alice"
```

These hints don’t enforce types at runtime but help tools (like IDEs) check your code.
****


