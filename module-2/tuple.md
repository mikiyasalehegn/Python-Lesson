# What is a Tuple?

- A **tuple** is a **collection data type** in Python.
- It is similar to a **list**, but with **two big differences**:
    1. **Immutable** → You cannot change, add, or remove items once the tuple is created.
    2. **Defined with parentheses** `()` instead of square brackets `[]`.
    

```python
tpl1 = tuple(ls1)
print(tpl1)
packing = 1,2,3
print(tpl1 is packing)

#  case two
t1 = [1,2,3]
packing = (1,2,3)
print(t1 is packing)
```

- **what will be the result of this code and why?**
    
    The result of this code in 2026 Python environments is:
    
    1. **`(1, 2, 3)`**
    2. **`False`**
    
    **Why?**
    
    The code demonstrates the difference between **Value Equality** (`==`) and **Reference Identity** (`is`).
    
    **1. `print(tpl1)` Output**
    
    - Assuming `ls1 = [1, 2, 3]`, calling `tuple(ls1)` converts the list into a new tuple object.
    - Python represents tuples using parentheses, resulting in the output `(1, 2, 3)`.
    
    **2. `print(tpl1 is packing)` Output**
    
    - **`packing = 1, 2, 3`**: This uses **Implicit Tuple Packing**, where Python creates a tuple directly from comma-separated values.
    - **The `is` Operator**: This keyword checks if two variables point to the **exact same object in memory** (Identity).
    - **The Result**: Although `tpl1` and `packing` have the same values, they were created through different processes at different times.
        - `tpl1` was built by a constructor from a list.
        - `packing` was created directly by the interpreter.
    - Because they are **two distinct objects** occupying different locations in RAM, `tpl1 is packing` returns **`False`**.

    - Note! For case 2 the result is True!
---

### 📝 Creating Tuples

```python
# Empty tuple
t1 = ()

# Tuple with elements
t2 = (1, 2, 3)

# Tuple with mixed data
t3 = (1, "hello", 3.5, True)

# Nested tuple
t4 = (1, (2, 3), (4, 5))

# Tuple without parentheses (tuple packing)
t5 = 1, 2, 3

# Single-element tuple (must include a comma!)
t6 = (5,)
print(type(t6))  # <class 'tuple'>

```

---

### 🔑 Key Features of Tuples

1. **Immutable** → Elements can not be modified.
    
    ```python
    t = (1, 2, 3)
    # t[0] = 100  ❌ Error: 'tuple' object does not support item assignment
    
    ```
    
2. **Ordered** → Elements maintain insertion order.
3. **Allow duplicates**
    
    ```python
    t = (1, 2, 2, 3, 1)
    print(t)  # (1, 2, 2, 3, 1)
    
    ```
    
4. **Can contain any type** (numbers, strings, lists, other tuples, objects).

---

### 📌 Accessing Tuple Elements

```python
t = (10, 20, 30, 40, 50)

# Indexing
print(t[0])   # 10
print(t[-1])  # 50

# Slicing
print(t[1:4])  # (20, 30, 40)

```

---

### 🛠 Tuple Operations

```python
t = (1, 2, 3)

# Concatenation
print(t + (4, 5))  # (1, 2, 3, 4, 5)

# Repetition
print(t * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
print(2 in t)  # True
print(10 in t) # False

# Length
print(len(t))  # 3

```

---

### ⚙️ Tuple Methods (only 2, since tuples are immutable)

```python
t = (1, 2, 2, 3, 4)

print(t.count(2))   # 2 (number of times 2 appears)
print(t.index(3))   # 3 (first index of 3)

```

---

### 🎯 Why Use Tuples?

- ✅ **Immutability** → Safer when you don’t want data to change.
- ✅ **Performance** → Slightly faster than lists.
- ✅ **Hashable** → Can be used as dictionary keys or elements in a set (lists cannot).
    
    ```python
    my_dict = { (1,2): "point A", (3,4): "point B" }
    print(my_dict[(1,2)])  # point A
    
    ```
    

---

### 🛑 When to Use List vs Tuple?

- Use **list** when data may change (e.g., collection of users, items in cart).
- Use **tuple** when data is **fixed/constant** (e.g., coordinates `(x, y)`, RGB colors, configuration values).

## Methods Available for Tuples

Tuples only have **two built-in methods**:

### 1. `count(value)`

Returns how many times a value appears in the tuple.

```python
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))   # 3
print(t.count(5))   # 0

```

---

### 2. `index(value, start=0, end=len(tuple))`

Returns the first index of a value (raises `ValueError` if not found).

You can also give optional `start` and `end` positions.

```python
t = (1, 2, 3, 2, 4, 2)

print(t.index(2))        # 1 (first occurrence)
print(t.index(2, 2))     # 3 (search from index 2)
# print(t.index(5)) ❌ ValueError

```

---

### 🔹 Functions You Can Use With Tuples

Even though tuples don’t have many methods, many **built-in functions** work with them (since they are sequences, just like lists):

```python
t = (5, 2, 9, 1)

print(len(t))     # 4
print(max(t))     # 9
print(min(t))     # 1
print(sum(t))     # 17
print(sorted(t))  # [1, 2, 5, 9] (returns a list)
print(any(t))     # True  (at least one non-zero)
print(all(t))     # True  (all elements are truthy)

```

### 🔹 Tuple Packing & Unpacking

```python
# Packing
t = 1, 2, 3   # tuple without parentheses
print(t)      # (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)  # 1 2 3

# Extended unpacking
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

```