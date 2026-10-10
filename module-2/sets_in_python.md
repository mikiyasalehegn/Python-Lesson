## 🔹 What is a Set in Python?

A **set** is an **unordered collection of unique elements**.

- **Unordered** → elements don’t have a fixed position (no indexing like lists).
- **Unique** → duplicates are automatically removed.
- **Mutable** → you can add or remove items.
- **Set elements must be immutable (hashable)** → you can store numbers, strings, tuples (but not lists, dicts, or other sets).

Think of a set like a mathematical set.

---

### 🔹 Creating a Set

```python
# Empty set (must use set(), not {} because {} makes a dict)
s = set()

# Creating from a list
s1 = set([1, 2, 3, 4, 4])   # duplicates removed → {1, 2, 3, 4}

# Creating directly
s2 = {1, 2, 3, "hello"}

# Creating from a string
s3 = set("banana")   # {'b', 'a', 'n'}  (unique letters)

```

⚠️ Note: `{}` → creates an empty **dictionary**, not a set. Always use `set()`.

---

### 🔹 Properties of Sets

1. **Unordered** → no fixed order.
2. **Unindexed** → can’t access items with `[index]`.
3. **Unique elements** → duplicates are removed automatically.
4. **Mutable** → you can add/remove elements.
5. **Elements must be immutable** (hashable). Example:
    - ✅ Numbers, strings, tuples → allowed.
    - ❌ Lists, dicts, set → not allowed.

---

### 🔹 Basic Operations

### Adding elements

```python
s = {1, 2, 3}
s.add(4)      # {1, 2, 3, 4}
s.add(2)      # {1, 2, 3, 4} (2 already exists, no change)

```

### Removing elements

```python
s = {1, 2, 3}
s.remove(2)   # {1, 3}
# s.remove(5) → KeyError if element not found

s.discard(5)  # No error if element not found
s.pop()       # Removes and returns a random element
s.clear()     # Removes all elements → set()

```

---

### 🔹 Set Operations (like Math!)

Python sets support union, intersection, difference, etc.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (combine all elements)
print(A | B)       # {1, 2, 3, 4, 5, 6}
print(A.union(B))  # same

# Intersection (common elements)
print(A & B)       # {3, 4}
print(A.intersection(B))

# Difference (elements in A but not in B)
print(A - B)       # {1, 2}
print(A.difference(B))

# Symmetric Difference (elements in A or B but not both)
print(A ^ B)       # {1, 2, 5, 6}
print(A.symmetric_difference(B))

```

---

### 🔹 Membership Testing

Checking if an element exists:

```python
s = {1, 2, 3}
print(2 in s)    # True
print(5 in s)    # False

```

---

### 🔹 Set Functions & Methods

Some useful ones:

```python
s = {10, 20, 30}

len(s)          # 3
max(s)          # 30
min(s)          # 10
sum(s)          # 60

# Copy
s2 = s.copy()   # {10, 20, 30}

# Update with another set
s.update({40, 50})   # {10, 20, 30, 40, 50}

```

---

### 🔹 Frozen Sets (Immutable Sets)

- A **frozenset** is like a set, but immutable (can not add/remove elements).
- Useful when you want to use a set as a dictionary key or store inside another set.

```python
fs = frozenset([1, 2, 3])
# fs.add(4) ❌ → Error (not allowed)

```

---

### 🔹 When to Use Sets?

✅ Removing duplicates from a list.

✅ Fast membership testing (`in` with sets is faster than lists).

✅ Performing mathematical set operations.

✅ Representing collections of unique items.

Example:

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)   # {1, 2, 3, 4, 5}

```

### 🔹 All Important Set Methods in Python

---

### 1. `union()` ( `|` operator )

Returns a new set with all elements from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))   # {1, 2, 3, 4, 5}
print(A | B)        # {1, 2, 3, 4, 5}

```

---

### 2. `intersection()` ( `&` operator )

Returns common elements.

```python
A = {1, 2, 3}
B = {2, 3, 4}
print(A.intersection(B))   # {2, 3}
print(A & B)               # {2, 3}

```

---

### 3. `difference()` (  operator )

Elements in one set but not in the other.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5}
print(A.difference(B))   # {1, 2}
print(A - B)             # {1, 2}

```

---

### 4. `symmetric_difference()` ( `^` operator )

Elements in either set, but not both.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))   # {1, 2, 4, 5}
print(A ^ B)                       # {1, 2, 4, 5}

```

---

### 5. `update()`

Updates (adds) elements from another set or iterable.

```python
A = {1, 2}
A.update([2, 3, 4])
print(A)   # {1, 2, 3, 4}

```

---

### 6. `intersection_update()`

Keeps only elements found in both sets.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5}
A.intersection_update(B)
print(A)   # {3, 4}

```

---

### 7. `difference_update()`

Removes elements found in another set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5}
A.difference_update(B)
print(A)   # {1, 2}

```

---

### 8. `symmetric_difference_update()`

Keeps only elements that are in either set, not both.

```python
A = {1, 2, 3}
B = {3, 4}
A.symmetric_difference_update(B)
print(A)   # {1, 2, 4}

```

---

### 9. `issubset()`

Checks if all elements of a set are contained in another.

```python
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))   # True
print(B.issubset(A))   # False

```

---

### 10. `issuperset()`

Checks if a set contains all elements of another set.

```python
A = {1, 2, 3, 4}
B = {2, 3}
print(A.issuperset(B))   # True
print(B.issuperset(A))   # False

```

---

### 11. `isdisjoint()`

Returns `True` if two sets have no elements in common.

```python
A = {1, 2, 3}
B = {4, 5}
C = {3, 6}
print(A.isdisjoint(B))   # True (no overlap)
print(A.isdisjoint(C))   # False (3 is common)

```

---

### 12. `copy()`

Returns a shallow copy of the set.

```python
A = {1, 2, 3}
B = A.copy()
print(B)       # {1, 2, 3}
print(A is B)  # False (different objects)

```

---

### 13. `clear()`

Removes all elements from a set.

```python
A = {1, 2, 3}
A.clear()
print(A)   # set()

```

---

### 🔹 Quick Summary Table

| Method | Description |
| --- | --- |
| `add(x)` | Add element `x` |
| `remove(x)` | Remove `x`, error if not found |
| `discard(x)` | Remove `x`, no error if not found |
| `pop()` | Remove & return random element |
| `clear()` | Remove all elements |
| `union()` / ` | ` |
| `intersection()` / `&` | Common elements |
| `difference()` / `-` | Elements in A not in B |
| `symmetric_difference()` / `^` | Elements in A or B, not both |
| `update()` | Add all elements from another set |
| `intersection_update()` | Keep only common elements |
| `difference_update()` | Remove common elements |
| `symmetric_difference_update()` | Keep only non-common elements |
| `issubset()` | Checks if A is subset of B |
| `issuperset()` | Checks if A is superset of B |
| `isdisjoint()` | Checks if sets have no common elements |
| `copy()` | Returns shallow copy |