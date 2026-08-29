## Lists In Python

### 1. 🔹 What is a List?

A **list** in Python is:

- An **ordered collection** of items.
- **Mutable** (you can change it after creating it).
- Can store **heterogeneous data types** (numbers, strings, other lists, etc.).
- Defined using **square brackets `[]`**.
- Lists in Python are actually **instances of the `list` class**.

👉 Example:

```python
my_list = [10, "hello", 3.14, True]
print(my_list)  # [10, 'hello', 3.14, True]

```


### 2. 🔹 Creating Lists

You can create lists in different ways:

```python
# Empty list
empty = []

# With elements
numbers = [1, 2, 3, 4, 5]

# Using list() constructor
letters = list("python")  # ['p', 'y', 't', 'h', 'o', 'n']

# Nested lists (lists inside lists)
nested = [[1, 2], [3, 4], [5, 6]]

```


### 3. 🔹 Accessing Elements

Lists are **indexed** starting from `0`.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple (first item)
print(fruits[-1])  # cherry (last item, using negative index)

```

👉 **Slicing**:

```python
print(fruits[0:2])   # ['apple', 'banana'] (up to index 2, not included)
print(fruits[:2])    # ['apple', 'banana']
print(fruits[1:])    # ['banana', 'cherry']
print(fruits[::-1])  # ['cherry', 'banana', 'apple'] (reverse)

```


### 4. 🔹 Modifying Lists

Since lists are **mutable**, you can change elements:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

```

👉 Adding elements:

```python
fruits.append("orange")   # add at the end
fruits.insert(1, "grape") # add at position 1

```

👉 Removing elements:

```python
fruits.remove("apple")  # removes 'apple'
fruits.pop()            # removes last element
fruits.pop(0)           # removes by index
del fruits[0]           # delete by index
fruits.clear()          # empty the list

```

### 5. 🔹 Useful List Methods

Python lists come with many built-in methods:

```python
numbers = [3, 1, 4, 1, 5, 9]

numbers.sort()        # sort in ascending order
numbers.sort(reverse=True)  # descending
numbers.reverse()     # reverse order

numbers.count(1)      # count occurrences
numbers.index(5)      # find index of value
numbers.copy()        # shallow copy

numbers.extend([2, 6, 7])  # add multiple items

```


### 6. 🔹 Iterating Over Lists

You can loop through lists easily:

```python
fruits = ["apple", "banana", "cherry"]

# For loop
for f in fruits:
    print(f)

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# List comprehension (short way)
uppercased = [f.upper() for f in fruits]
print(uppercased)  # ['APPLE', 'BANANA', 'CHERRY']

```


### 7. 🔹 Checking Existence

```python
if "apple" in fruits:
    print("Yes, apple is in the list")

if "mango" not in fruits:
    print("No mango here")

```


### 8. 🔹 Copying Lists (Important!)

If you do `list2 = list1`, both point to the same object.

To actually copy:

```python
list2 = list1.copy()
list3 = list(list1)
list4 = list1[:]  # slicing

```


### 9. 🔹 Nested Lists

Lists can contain lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6

```

👉 Useful for **2D arrays**.


### 10. 🔹 List Comprehensions

A powerful and concise way to create lists.

```python
# Squares of numbers
squares = [x**2 for x in range(10)]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]

# Nested loop comprehension
pairs = [(x, y) for x in [1,2,3] for y in [4,5,6]]

```


### 11. 🔹 Lists vs Other Collections

- **List** → ordered, mutable, allows duplicates.
- **Tuple** → ordered, immutable.
- **Set** → unordered, no duplicates.
- **Dictionary** → key-value pairs.


### 12. 🔹 Advanced Topics

### a) Aliasing Problem

```python
a = [1, 2, 3]
b = a   # both point to same list
b[0] = 99
print(a)  # [99, 2, 3]

```

### b) Shallow vs Deep Copy

```python
import copy

nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep = copy.deepcopy(nested)

nested[0][0] = 999
print(shallow)  # [[999, 2], [3, 4]] (affected)
print(deep)     # [[1, 2], [3, 4]]   (not affected)

```

### c) Performance Tips

- **Appending** is fast (`O(1)`).
- **Inserting/removing in middle** is slower (`O(n)`).
- Use **list comprehension** instead of loops when possible.
- For large data, sometimes `array` (from `array` module) or `numpy` arrays are better.


### 13. 🔹 Real-Life Use Cases

- **Storing user data** (names, scores, etc.).
- **Queues/Stacks** (FIFO/LIFO) with `append()` and `pop()`.
- **Matrix representation** in 2D lists.
- **Data processing** (filtering, mapping, reducing).
- **Implementing algorithms** (sorting, searching, BFS/DFS).

## More Advanced Python List Concepts



### 14. 🔹 Lists are Objects (Everything is an Object in Python)

Lists in Python are actually **instances of the `list` class**.

```python
nums = [1, 2, 3]
print(type(nums))  # <class 'list'>
print(isinstance(nums, list))  # True
```

This means:

- Lists inherit methods from `list`.
- You can use `dir(list)` to see all available methods.


### 15. 🔹 Memory & Internals of Lists

- Lists in Python are **dynamic arrays** (like vectors in C++).
- When you `append()`, Python sometimes **resizes the array** by allocating more space than needed (to make future appends faster).
- That’s why `append()` is **amortized O(1)** but resizing can be expensive occasionally.

👉 Check memory size:

```python
import sys
nums = []
for i in range(10):
    nums.append(i)
    print(len(nums), sys.getsizeof(nums))

```

You’ll see that memory doesn’t increase one by one, but in chunks.


### 16. 🔹 Iterators and Lists

Lists are **iterable** objects, meaning they can return an iterator.

```python
fruits = ["apple", "banana", "cherry"]
it = iter(fruits)

print(next(it))  # apple
print(next(it))  # banana
print(next(it))  # cherry

```

- **👉 This is why lists work with `for` loops.**
    
    To understand these, think of a **music playlist** vs. a **CD player**.
    
    **1. The Concepts**
    
    - **Iterable (The Playlist):** Any object you can loop over (like a `list`, `str`, or `dict`). It has the **data** but doesn't track its own position. In OOP terms, an iterable must implement the `__iter__` method.
    - **Iterator (The CD Player):** The actual object that performs the traversal. It tracks the **current state** (where it is in the list) and knows how to get the "next" item. It must implement both `__iter__` and `__next__`.
    
    **2. The Functions**
    
    - **`iter()`**: This function takes an **Iterable** and returns an **Iterator**. It’s like putting the "Playlist" into the "Player."
    - **`next()`**: This function takes an **Iterator** and returns the very next item in the sequence. If there are no items left, it raises a StopIteration exception.
    
    **3. Code Execution**
    
    **python**
    
    ```python
    my_list = [10, 20]          # <--- Iterable
    my_player = iter(my_list)   # <--- Iterator
    
    print(next(my_player))      # Output: 10
    print(next(my_player))      # Output: 20
    # print(next(my_player))    # Raises StopIteration
    ```
    
    Use code with caution.
    
    **4. Memory & Efficiency**
    
    The magic of iterators is that they use **Lazy Evaluation**. Unlike a list that stores all elements in memory at once, an iterator can generate items one at a time. This is why you can have an iterator for an infinite sequence (like counting to infinity) without crashing your computer.
    
    **5. How `for` loops work**
    
    When you write `for item in my_list:`, Python silently does this behind the scenes:
    
    1. Calls `it = iter(my_list)` to get an iterator.
    2. Repeatedly calls `next(it)` to get items.
    3. Catches the `StopIteration` error to stop the loop gracefully.
    
    Would you like to see how to create a **Custom Iterator Class** by defining your own `__next__` method?
    
    **Step-by-Step Explanation**
    
    **python**
    
    `fruits = ["apple", "banana", "cherry"]`
    
    Use code with caution.
    
    We define a standard **iterable list** named `fruits`.
    
    **python**
    
    `it = iter(fruits)`
    
    Use code with caution.
    
    We call the `iter()` function on our list. This creates a new **iterator object** (`it`). This object's internal memory now points to the very beginning of the `fruits` list, ready to start iteration.
    
    **python**
    
    `print(next(it))  # apple`
    
    Use code with caution.
    
    We call the `next()` function on the iterator.
    
    - The iterator (`it`) returns the item it is currently pointing to (`"apple"`).
    - It then advances its internal pointer to the next item (`"banana"`).
    
    **python**
    
    `print(next(it))  # banana`
    
    Use code with caution.
    
    We call `next()` again.
    
    - The iterator returns `"banana"` and moves its pointer to `"cherry"`.
    
    **python**
    
    `print(next(it))  # cherry`
    
    Use code with caution.
    
    We call `next()` a third time.
    
    - The iterator returns `"cherry"` and moves its pointer *past* the last item in the list.
    
    **3. What Happens Next?**
    
    If you were to call `print(next(it))` one more time, the iterator has no more items to give. It would stop the program and raise a **`StopIteration`** exception.
    
    This exception is exactly how a standard `for` loop knows when it has reached the end of a list and should stop running.
    

---

### 17. 🔹 Enumerate with Lists

Instead of using indexes manually, Python has `enumerate()`.

```python
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

```

Output:

```
0 apple
1 banana
2 cherry

```

---

### 18. 🔹 Zip with Lists

You can combine multiple lists together using `zip()`.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(name, "scored", score)

```

---

### 19. 🔹 Unpacking Lists

Python allows **unpacking** lists directly into variables.

```python
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3

```

👉 With `*` (extended unpacking):

```python
nums = [1, 2, 3, 4, 5]
a, *b, c = nums
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

```

---

### 20. 🔹 Using  to Merge Lists

```python
a = [1, 2]
b = [3, 4]
merged = [*a, *b]
print(merged)  # [1, 2, 3, 4]

```

---

### 21. 🔹 Any, All, and List Conditions

You can check conditions across a list with `any()` and `all()`.

```python
nums = [1, 2, 3, 0]

print(any(nums))  # True (at least one truthy value)
print(all(nums))  # False (because 0 is falsy)

```

---

### 22. 🔹 `min`, `max`, `sum` with Lists

```python
nums = [3, 7, 2, 9]

print(min(nums))  # 2
print(max(nums))  # 9
print(sum(nums))  # 21

```

---

### 23. 🔹 Sorting Lists in Custom Ways

You can use `sorted()` or `.sort()` with a **key function**.

```python
words = ["banana", "apple", "cherry", "kiwi"]

# Sort alphabetically
print(sorted(words))

# Sort by length
print(sorted(words, key=len))

# Sort in reverse
print(sorted(words, reverse=True))

```

---

### 24. 🔹 List as a Stack & Queue

- **Stack (LIFO)** → use `append()` and `pop()`.
- **Queue (FIFO)** → lists are slow, so use `collections.deque`.

```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2

```

---

### 25. 🔹 Flattening Nested Lists

Sometimes you have nested lists and want a single list.

```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

```

## How List Comprehension Works

The general form of a **nested list comprehension** is:

```python
[new_item for outer_item in outer_list for inner_item in outer_item]

```

It’s equivalent to:

```python
result = []
for outer_item in outer_list:
    for inner_item in outer_item:
        result.append(inner_item)

```

### 26. 🔹 Filtering with `filter()`

Instead of comprehension:

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

```

---

### 27. 🔹 Mapping with `map()`

```python
nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9]

```

---

### 28. 🔹 Reducing with `functools.reduce()`

```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

```

---

### 29. 🔹 Converting Other Types to Lists

```python
s = "hello"
chars = list(s)  # ['h', 'e', 'l', 'l', 'o']

set_data = {1, 2, 3}
list_data = list(set_data)  # [1, 2, 3]

```

---

### 30. 🔹 List vs Generator Expressions

```python
nums = [x**2 for x in range(10)]      # list comprehension
nums_gen = (x**2 for x in range(10))  # generator expression

print(nums)         # builds full list
print(list(nums_gen))  # builds on-demand

```

👉 Use generator when you don’t need all values at once (saves memory).

---

### 31. 🔹 Advanced Tricks

### Swapping Elements

```python
nums = [1, 2, 3]
nums[0], nums[2] = nums[2], nums[0]
print(nums)  # [3, 2, 1]

```

### Multiplying Lists

```python
print([0] * 5)  # [0, 0, 0, 0, 0]

```

⚠️ But be careful with nested:

```python
bad = [[0] * 3] * 3
bad[0][0] = 1
print(bad)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  (because they share the same reference!)

```

- **Attention!**
    
    **Why did this happen?**
    
    This is a classic Python "gotcha." When you use the `*` operator on a list containing a mutable object (like another list), Python does **not** create separate, independent copies of that object. Instead, it creates multiple **references** to the exact same object in memory.
    
    1. **`[0] * 3`**: This creates a single list object: `[0, 0, 0]`.
    2. **`[[0] * 3] * 3`**: This creates an outer list and populates it with three "name tags" (references), all pointing to the **one** list created in step 1.
    3. **`bad[0][0] = 1`**: When you modify the first element of the first inner list, you are modifying the single list object that all three rows share. Because all three rows "point" to the same memory location, the change appears in every row.
    
    **The Correct Way (2025 Standard)**
    
    To create a grid where each row is an independent object, use a **list comprehension**. This forces Python to evaluate the inner list creation multiple times, producing new, unique list objects for each row:
    
    **Memory Visualization:**
    
    **text**
    
               `Row Index           Memory Location (Object)
              +----------+        +-----------------------+
    bad[0] -->| Reference|------->|                       |
              +----------+        |       [ 0, 0, 0 ]     |
    bad[1] -->| Reference|------->|                       |
              +----------+        | (Single Object in RAM)|
    bad[2] -->| Reference|------->|                       |
              +----------+        +-----------------------+
                                              ^`
    
    Use code with caution.
    
    |Setting bad[0][0] = 1 ---------------+changes the ONLY list that exists.
    
    `**Result:** Because all rows point to the **same box**, changing the box through one row makes it look like every row changed.
    
    ---
    
    ### 2. The "Good" Method (Independent Objects)
    When you use a List Comprehension `good = [[0] * 3 for _ in range(3)]`, Python runs the code `[0] * 3` three separate times, creating three **distinct** boxes in memory.
    
    **Memory Visualization:**
    ```text
               Row Index           Memory Locations (Objects)
              +----------+        +-----------------------+
    good[0] -->| Reference|------->|    List Object A      |
              +----------+        |      [ 1, 0, 0 ]      |
                                  +-----------------------+
              +----------+        +-----------------------+
    good[1] -->| Reference|------->|    List Object B      |
              +----------+        |      [ 0, 0, 0 ]      |
                                  +-----------------------+
              +----------+        +-----------------------+
    good[2] -->| Reference|------->|    List Object C      |
              +----------+        |      [ 0, 0, 0 ]      |
                                  +-----------------------+
    
        Setting good[0][0] = 1 ONLY 
        affects List Object A.`
  
### List Methods

| Method | Description | Example |
| --- | --- | --- |
| `append(x)` | Add `x` to end | `[1].append(2) → [1, 2]` |
| `extend(iter)` | Add all items from iterable | `[1].extend([2,3]) → [1,2,3]` |
| `insert(i,x)` | Insert `x` at index `i` | `[1,3].insert(1,2) → [1,2,3]` |
| `remove(x)` | Remove first `x` | `[1,2,2].remove(2) → [1,2]` |
| `pop(i)` | Remove & return element at `i` (default last) | `[1,2,3].pop() → 3` |
| `clear()` | Remove all items | `[1,2].clear() → []` |
| `index(x[, start[, end]])` | Return index of first `x` | `[10,20,30].index(20) → 1` |
| `count(x)` | Count occurrences of `x` | `[1,2,2].count(2) → 2` |
| `sort(key=None, reverse=False)` | Sort in place | `[3,1].sort() → [1,3]` |
| `reverse()` | Reverse in place | `[1,2].reverse() → [2,1]` |
| `copy()` | Return shallow copy | `[1,2].copy() → [1,2]` |
- **sorted() and sort()**
    
    **1. `list.sort()` (The In-Place Modifier)**
    
    This is a **method** belonging to the **list class**. It rearranges the elements of the *existing* list directly in memory.
    
    - **Return Value:** It returns `None`.
    - **Original Data:** The original order is permanently lost.
    - **Efficiency:** It is generally **faster and more memory-efficient** because it doesn't need to allocate space for a new list.
    
    **2. `sorted()` (The Non-Destructive Creator)**
    
    This is a **built-in function** that can take *any* **iterable** (lists, tuples, strings, etc.) as an argument.
    
    - **Return Value:** It returns a **new list** containing the sorted elements.
    - **Original Data:** The original object remains **unchanged**.
    - **Versatility:** You can use it to sort things that aren't even lists, like a tuple or a dictionary's keys.

**Sorting with lambda function**

```python
items = [
		("product1", 28),
		("product2", 19),
		("product3", 55),
		("product4", 25),
]

items.sort(key=lambda item: item[1])

# output based on the price
[('product2', 19), ('product4', 25), ('product1', 28), ('product3', 55)]
```
