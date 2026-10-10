# Arrays in Python

### 1. **Lists as Arrays**

In Python, an **array** is a **data structure** that stores a collection of elements, typically of the **same type**, in a contiguous block of memory. Arrays allow efficient storage, indexing, and manipulation of data, especially numerical data.

```python
nums = [1, 2, 3, 4, 5]
print(nums[0])     # 1
nums.append(6)
print(nums)        # [1, 2, 3, 4, 5, 6]

```

- Lists are flexible: they can store **mixed types** (numbers, strings, objects).
- But they’re **not memory efficient** if you need millions of numbers.

---

### 2. **The `array` Module** (from Python Standard Library)

Python has a built-in module called **`array`** that provides a more **compact, memory-efficient array** than a list.

- Unlike lists, arrays must contain **elements of the same type**.

```python
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)       # array('i', [1, 2, 3, 4, 5])

arr.append(6)
print(arr)       # array('i', [1, 2, 3, 4, 5, 6])

arr[0] = 100
print(arr)       # array('i', [100, 2, 3, 4, 5, 6])

```

- The first argument (`'i'`) is the **type code**:
    - `'i'` → integer
    - `'f'` → float
    - `'u'` → Unicode char
    - etc.

### Example of operations:

```python
arr = array.array('i', [1, 2, 3])
arr.extend([4, 5])
print(arr)       # array('i', [1, 2, 3, 4, 5])

arr.insert(2, 99)
print(arr)       # array('i', [1, 2, 99, 3, 4, 5])

arr.pop()
print(arr)       # array('i', [1, 2, 99, 3, 4])

```

---

you can not store multiple **strings** inside a single object from the built-in `array` module.

The `array.array` type is strictly **homogeneous** and designed for basic machine values. It does not have a "type code" that represents a string as a single element.

**How it treats text data**

While it cannot store a "list of strings," it can store **individual characters**:

- **Characters, not Strings:** If you use the type codes `'u'` or `'w'`, the array treats the input as a single sequence of **Unicode characters**.
- **Storage Behavior:** If you pass a string like `"hello"` to an array with type code `'w'`, it creates an array of 5 elements, where each element is one character (`'h'`, `'e'`, etc.). You cannot store a second string like `"world"` as a single next element.

```python
import array

# Storing Integers ('i' type code)
numbers = array.array('i', [10,20,30])
numbers.append(40)
print(numbers)# array('i', [10, 20, 30, 40])

# Storing Characters ('w' type code for Unicode)
# Note: This stores characters individually, not as full strings.
char_array = array.array('w',"Hello")
print(char_array[0])# Output: 'H'
```

### 3. **NumPy Arrays** (Most Popular)

For scientific computing, machine learning, and large datasets, **NumPy** is the go-to library.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)         # [1 2 3 4 5]
print(arr * 2)     # [ 2  4  6  8 10]

# INCORRECT way (will result in an error or unexpected behavior)
# array.array('i', ["Apple", "Banana"])  # TypeError: integer required
```

### Why NumPy arrays?

- Much **faster** than lists or `array.array` (implemented in C).
- Support **vectorized operations** (do math on the whole array without loops).
- Multi-dimensional arrays (**matrices, tensors**) supported.

Example:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix.shape)  # (2, 3)
print(matrix[1][2])  # 6

```

---

### 4. **When to Use What?**

- ✅ **List** → general-purpose, flexible, everyday coding.
- ✅ **array.array** → if you need a memory-efficient typed array (but still pure Python).
- ✅ **NumPy array** → when performance, math, or multi-dimensional data is needed.

---

### 5. **Example Comparison**

```python
import array, numpy as np

lst = [1, 2, 3, 4, 5]              # list
arr = array.array('i', [1, 2, 3])  # array module
np_arr = np.array([1, 2, 3])       # numpy array

print(type(lst))     # <class 'list'>
print(type(arr))     # <class 'array.array'>
print(type(np_arr))  # <class 'numpy.ndarray'>

```

---

✅ So in Python, “array” can mean:

1. Just a **list** (common for beginners).
2. A **typed array** using `array` module.
3. A **NumPy ndarray** (used in data science, ML, numerical computing).