# 🔹 What is a Dictionary in Python?

- A **dictionary** is a collection of **key-value pairs**.
- Keys must be **unique** and **hashable** (immutable like strings, numbers, tuples).
- Values can be **any type** (mutable or immutable).
- Dictionaries are **unordered** before Python 3.7, but from Python 3.7+, they maintain **insertion order**.
- Fast for lookups, insertions, and deletions.

Think of it like a **real dictionary**: word = key, meaning = value.

---

### 🔹 Creating Dictionaries

```python
# Empty dictionary
d1 = {}

# Using dict() function
d2 = dict()

# With values
d3 = {"name": "Alice", "age": 25, "city": "Paris"}

# Using dict() with keyword arguments
d4 = dict(name="Bob", age=30)

# From list of tuples
d5 = dict([("name", "Charlie"), ("age", 28)])

```

---

### 🔹 Accessing Values

```python
person = {"name": "Alice", "age": 25, "city": "Paris"}

print(person["name"])   # Alice
# print(person["country"]) ❌ → KeyError

# Using get() avoids error
print(person.get("country", "Not Found"))  # Not Found
```

---

### 🔹 Adding / Updating Items

```python
person = {"name": "Alice", "age": 25}

person["city"] = "Paris"    # Add new key-value
person["age"] = 26          # Update existing key
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'Paris'}
```

---

### 🔹 Removing Items

```python
person = {"name": "Alice", "age": 25, "city": "Paris"}

person.pop("age")       # Removes key "age" → 25
person.popitem()        # Removes last inserted item (city: Paris)
del person["name"]      # Deletes "name"
person.clear()          # Empty dictionary {}

```

---

### 🔹Get the key with the maximum value

Often, you want to know **who** has the highest score.

```
top_student=max(scores,key=scores.get)

print(top_student)
```

Output:

```
David
```

#### How it works

For each key:

```
scores.get("Alice")# 85
scores.get("Bob")# 92
scores.get("Charlie")# 78
scores.get("David")# 95
```

`max()` compares these values and returns the key associated with the largest one.

### 🔹 Dictionary Methods

Here are the most important ones:

```python
student = {"name": "Eden", "age": 22, "grade": "A"}

# Keys, values, items
print(student.keys())     # dict_keys(['name', 'age', 'grade'])
print(student.values())   # dict_values(['Eden', 22, 'A'])
print(student.items())    # dict_items([('name', 'Eden'), ('age', 22), ('grade', 'A')])

# Copy
copy_student = student.copy()

# Update (merge dictionaries)
student.update({"age": 23, "city": "Tel Aviv"})
print(student)

# fromkeys() – create dict with default values
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)   # {'a': 0, 'b': 0, 'c': 0}

```

---

### 🔹 Looping Through a Dictionary

```python
student = {"name": "Eden", "age": 22, "grade": "A"}

# Keys
for k in student:
    print(k)

# Values
for v in student.values():
    print(v)

# Keys and values
for k, v in student.items():
    print(k, ":", v)

```

---

### 🔹 Nested Dictionaries

Dictionaries can contain other dictionaries (like JSON).

```python
students = {
    "s1": {"name": "Alice", "age": 20},
    "s2": {"name": "Bob", "age": 22}
}

print(students["s1"]["name"])  # Alice

```

---

### 🔹 Dictionary Comprehension

Like list comprehensions, but for dictionaries:

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```

---

### 🔹 When to Use Dictionaries?

✅ When you need **key-value mapping** (like IDs → users).

✅ When order doesn’t matter (or when insertion order matters in Python 3.7+).

✅ For fast lookups (much faster than searching in lists).

✅ To represent structured data (like JSON from APIs).

## Advanced Things About Dictionaries

### 1. **Dictionary is mutable but keys must be immutable (hashable)**

- Keys can only be:
    - ✅ Strings, numbers, tuples (if they only contain immutable objects).
    - ❌ Lists, dicts, or sets (since they are mutable).

```python
d = { (1, 2): "point" }  # valid
# d = { [1, 2]: "list" } ❌ → TypeError: unhashable type: 'list'

```

---

### 2. **Insertion order is preserved (Python 3.7+)**

Before Python 3.7, dictionaries were unordered.

Now, the order you insert keys is remembered:

```python
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d)  # {'a': 1, 'b': 2, 'c': 3}

```

---

### 3. **Default values with `setdefault()`**

If a key doesn’t exist, you can set a default value:

```python
person = {"name": "Alice"}
age = person.setdefault("age", 25)
print(person)  # {'name': 'Alice', 'age': 25}

```

---

### 4. **Using `get()` vs direct access**

- `get()` is safer than direct access:

```python
person = {"name": "Alice"}
print(person.get("age", "Not Found"))  # Not Found
# print(person["age"]) ❌ → KeyError

```

---

### 5. **Merging dictionaries (Python 3.9+)**

You can merge two dicts easily:

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

```

Equivalent to:

```python
d1.update(d2)

```

---

### 6. **Dictionary Views (`keys()`, `values()`, `items()`) are dynamic**

They update automatically when the dictionary changes:

```python
d = {"a": 1, "b": 2}
keys = d.keys()
print(keys)  # dict_keys(['a', 'b'])

d["c"] = 3
print(keys)  # dict_keys(['a', 'b', 'c']) (auto-updated)

```

---

### 7. **Deleting with `popitem()`**

- `popitem()` removes the **last inserted** item (since Python 3.7+).

```python
d = {"a": 1, "b": 2, "c": 3}
print(d.popitem())  # ('c', 3)

```

---

### 8. **Dictionary comprehension with conditions**

```python
squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(squares)  # {0: 0, 2: 4, 4: 16}

```

---

### 9. **Nested dictionaries are very common in JSON / APIs**

Dictionaries are the backbone of JSON parsing:

```python
user = {
    "id": 101,
    "name": "Alice",
    "address": {"city": "Paris", "zip": "75001"}
}
print(user["address"]["city"])  # Paris

```

---

### 10. **Performance of dictionaries**

- Dictionaries use **hash tables**, so lookups, insertions, and deletions are on average **O(1)** (very fast).
- That’s why they’re often used instead of searching lists.

---

### 11. **Specialized dictionary classes**

Python provides advanced versions of dictionaries in the `collections` module:

- `defaultdict` → dictionary with default values.
- `OrderedDict` → dictionary that remembers order (not so needed since 3.7).
- `Counter` → counts occurrences of items.
- `ChainMap` → combine multiple dictionaries.

Example:

```python
from collections import defaultdict

dd = defaultdict(int)
dd["a"] += 1
print(dd)  # defaultdict(<class 'int'>, {'a': 1})

```

---

### 🔹 Summary of Things I Didn’t Mention Earlier

✅ Keys must be immutable (hashable).

✅ Dictionaries preserve insertion order (3.7+).

✅ `setdefault()` for safe default values.

✅ Merge using `|` operator (Python 3.9+).

✅ Dictionary views (`keys()`, `items()`, `values()`) are dynamic.

✅ `popitem()` removes last inserted item.

✅ Dictionary comprehensions with conditions.

✅ Dictionaries = JSON in Python.

✅ Very fast thanks to hash tables.

✅ Advanced versions: `defaultdict`, `Counter`, `OrderedDict`.