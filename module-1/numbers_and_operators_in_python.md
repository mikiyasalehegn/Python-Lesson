### **int** — Integers

- Whole numbers, positive or negative, without decimals.
- In Python 3, `int` can be arbitrarily large (limited only by your computer’s memory).
- Examples:
    
    ```python
    a = 42
    b = -100
    c = 999999999999999999999  # works fine in Python 3
    ```

### **float** — Floating-Point Numbers

- Numbers with a decimal point, stored using **IEEE 754 double precision** (about 15–17 digits of precision).
- Examples:
    
    ```python
    x = 3.14
    y = -0.001
    z = 1.0
    ```
    
- Be careful: floating-point math is **not exact** because of binary representation.
    
    ```python
    0.1 + 0.2  # 0.30000000000000004
    ```

### Complex Numbers

- Have a real and an imaginary part.
- Written as `a + bj` where `j` is the imaginary unit.
- Examples:
    
    ```python
    c1 = 2 + 3j
    c2 = 5 - 4j
    print(c1.real)  # 2.0
    print(c1.imag)  # 3.0
    ```

### **Type Conversion**

You can convert between number types:

```python
int(3.9)     # 3
float(5)     # 5.0
complex(2)   # (2+0j)
```

### **Boolean Relationship**

- In Python, `bool` is a subclass of `int`:
    
    ```python
    python
    
    True == 1  # True
    False == 0 # True
    
    ```
    
- But `True is 1` → **False** (different types, different objects).

### **General Built-in Functions for Numbers**

These work with `int`, `float`, and sometimes `complex`.

| Function | Description | Example |
| --- | --- | --- |
| `abs(x)` | Absolute value (distance from zero) | `abs(-7) → 7` |
| `round(x, ndigits)` | Rounds to the nearest integer or to `ndigits` decimal places | `round(3.14159, 2) → 3.14` |
| `pow(x, y)` | Raises `x` to the power of `y` (same as `x ** y`) | `pow(2, 3) → 8` |
| `min(a, b, …)` | Returns the smallest value | `min(3, 1, 4) → 1` |
| `max(a, b, …)` | Returns the largest value | `max(3, 1, 4) → 4` |
| `sum(iterable)` | Sums all numbers in an iterable | `sum([1, 2, 3]) → 6` |
| `divmod(a, b)` | Returns `(quotient, remainder)` | `divmod(7, 3) → (2, 1)` |

### **2. Type Conversion Functions**

| Function | Description | Example |
| --- | --- | --- |
| `int(x)` | Converts to integer (truncates float) | `int(3.9) → 3` |
| `float(x)` | Converts to floating point | `float(5) → 5.0` |
| `complex(real, imag)` | Creates a complex number | `complex(2, 3) → (2+3j)` |

### **3. Number Checking Functions**

These check a number’s properties.

| Function | Description | Example |
| --- | --- | --- |
| `isinstance(x, int)` | Checks if `x` is an integer | `isinstance(5, int) → True` |
| `isinstance(x, float)` | Checks if `x` is a float | `isinstance(3.14, float) → True` |
| `isinstance(x, complex)` | Checks if `x` is complex | `isinstance(2+3j, complex) → True` |

### **4. Math Module (Extra Tools)**

You need to `import math` to use these.

| Function | Description | Example |
| --- | --- | --- |
| `math.ceil(x)` | Rounds up | `math.ceil(3.1) → 4` |
| `math.floor(x)` | Rounds down | `math.floor(3.9) → 3` |
| `math.sqrt(x)` | Square root | `math.sqrt(16) → 4.0` |
| `math.factorial(x)` | Factorial | `math.factorial(5) → 120` |
| `math.gcd(a, b)` | Greatest common divisor | `math.gcd(8, 12) → 4` |
| `math.lcm(a, b)` | Least common multiple | `math.lcm(8, 12) → 24` |
| `math.isfinite(x)` | Checks if finite | `math.isfinite(5.0) → True` |
| `math.isinf(x)` | Checks if infinite | `math.isinf(float('inf')) → True` |
| `math.isnan(x)` | Checks if NaN | `math.isnan(float('nan')) → True` |

### **5. Random Numbers (random module)**

If you want random numbers:

```python
import random
random.randint(1, 10)   # Random int between 1 and 10
random.random()         # Random float 0.0 to 1.0
random.uniform(1, 5)    # Random float between 1 and 5
```

### **What are Operators?**

Operators are **symbols or keywords** in Python that perform operations on values (operands).

Example:

```python
x = 5 + 3  # "+" is an operator, 5 and 3 are operands
```

#### **1. Arithmetic Operators**

These are for math operations, but Python’s arithmetic operators are more flexible than in some languages because they work with **integers, floats, complex numbers**, and even **custom classes** (via operator overloading).

| Operator | Name | Works With | Example | Output |
| --- | --- | --- | --- | --- |
| `+` | Addition | numbers, strings, lists, tuples | `5 + 3` → `8` ; `"a" + "b"` → `"ab"` |  |
| `-` | Subtraction | numbers | `5 - 2` → `3` |  |
| `*` | Multiplication | numbers, sequence repetition | `5 * 2` → `10` ; `"hi"*3` → `"hihihi"` |  |
| `/` | Division (always float) | numbers | `5 / 2` → `2.5` |  |
| `//` | Floor division | numbers | `5 // 2` → `2` |  |
| `%` | Modulus (remainder) | numbers, can be negative | `5 % 2` → `1` ; `-5 % 2` → `1` |  |
| `**` | Exponentiation | numbers | `2 ** 3` → `8` ; `9 ** 0.5` → `3.0` |  |

💡 **Special notes:**

- `/` always returns a **float**, even if divisible: `4 / 2 → 2.0`
- `//` **rounds toward negative infinity**:
    
    ```python
    5 // 2  # 2
    -5 // 2 # -3 (not -2!)
    ```
    

---

#### **🔹 2. Assignment Operators**

These let you **assign** and also **modify variables** in place.

| Operator | Example | Meaning |
| --- | --- | --- |
| `=` | `x = 5` | Assign value |
| `+=` | `x += 3` | Add and assign |
| `-=` | `x -= 3` | Subtract and assign |
| `*=` | `x *= 3` | Multiply and assign |
| `/=` | `x /= 3` | Divide and assign |
| `//=` | `x //= 3` | Floor divide and assign |
| `%=` | `x %= 3` | Modulus and assign |
| `**=` | `x **= 3` | Exponentiate and assign |
| `&=` | `x &= y` | Bitwise AND assign |
| `^=` | `x ^= y` | Bitwise XOR assign |
| `>>=` | `x >>= y` | Right shift assign |
| `<<=` | `x <<= y` | Left shift assign |
| `:=` | `if (n := len(lst)) > 5:` | Walrus operator (assign inside expressions) |

💡 **Special notes:**

- Compound operators (`+=`, `=`) behave differently for mutable and immutable types:
    
    ```python
    lst = [1, 2]
    lst += [3]   # modifies in place
    num = 5
    num += 3     # creates new int object
    ```
    

#### **🔹 3. Comparison Operators**

Return a **boolean** (`True` or `False`), but Python allows **chained comparisons**.

| Operator | Example | Result |
| --- | --- | --- |
| `==` | `5 == 5` | True |
| `!=` | `5 != 3` | True |
| `>` | `5 > 3` | True |
| `<` | `5 < 3` | False |
| `>=` | `5 >= 5` | True |
| `<=` | `5 <= 3` | False |


```python
3 < 5 < 8  # True (like: 3 < 5 and 5 < 8)
```
**Object comparison rules:**

- Different types can be compared only if supported (e.g., numbers).
- Strings are compared **lexicographically**:

```python
"abc" < "abd"  # True
```

**How Character Comparison Works**

1. **Character-by-Character:** It starts with the first character of each string. If they are identical, it moves to the second, then the third, and so on.
2. **Unicode Values (Code Points):** Instead of using a standard alphabet (A-Z), Python uses each character's **Unicode code point** (a unique number) to determine its value. You can see this value using the `ord()` function.
3. **Determining the Winner:** The first time a pair of characters differ, the string with the smaller Unicode value is considered "less than" the other.
4. **Short vs. Long:** If one string is a prefix of another (e.g., "apple" vs. "apples"), the **shorter string** is always considered smaller.

**Key Rules and Gotchas**

- **Case Sensitivity:** Uppercase letters have **smaller** Unicode values than lowercase letters.
    - `"Apple" < "apple"` is **True** because 'A' (65) is less than 'a' (97).
- **Numeric Strings:** Numbers are compared as text, not as mathematical values.
    - `"2" > "10"` is **True** because the character "2" has a higher Unicode value than "1".
- **Non-Alphabetical Characters:** Symbols and emojis are also part of this order. For example, a space has a lower value than letters.

**Examples**

| **Comparison** | **Result** | **Why?** |
| --- | --- | --- |
| `"apple" < "banana"` | `True` | 'a' comes before 'b'. |
| `"bat" < "batch"` | `True` | Shorter strings (prefixes) come first. |
| `"apple" > "Apple"` | `True` | Lowercase 'a' (97) is greater than uppercase 'A' (65). |
| `"2" < "12"` | `False` | '2' is greater than '1' in the first position. |

#### **🔹 4. Logical Operators**

Work with truth values.

| Operator | Meaning | Example |
| --- | --- | --- |
| `and` | True if both are True | `(5 > 3) and (2 < 4)` → True |
| `or` | True if at least one is True | `(5 > 3) or (2 > 4)` → True |
| `not` | Invert truth value | `not True` → False |

💡 **Short-circuiting:**

```python
x = 0
x != 0 and (10 / x)  # Second part not evaluated
```

---

Check **memory location**, not just equality.

| Operator | Meaning | Example |
| --- | --- | --- |
| `is` | Same object | `a is b` |
| `is not` | Different objects | `a is not b` |

💡 **Example:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True  (same values)
a is b  # False (different memory)
```

In Python, even if two lists have the same values, they are created as distinct objects in memory because **lists are mutable**.

**1. The Mutability Factor**

A list is "mutable," meaning its contents can be changed after it is created (e.g., you can `append` or `pop` items). If Python pointed both `a` and `b` to the same memory address, changing `a` would accidentally change `b` as well.

- **Example of the problem:** If `a` and `b` shared memory, running `a.append(4)` would make `b` become `[1, 2, 3, 4]` too.
- To prevent this "side effect," Python ensures every new list literal `[]` creates a **unique instance** in memory.

**2. No "Interning" for Lists**

Python uses a technique called **interning** for some immutable objects like small integers (typically -5 to 256) and certain strings to save memory.

- Because these objects can not be changed, it is safe for multiple variables to point to the same one.
- Since lists can change, they are **never interned** by the Python interpreter.

**3. Equality vs. Identity**

You can verify this behavior using two different operators:

- **`==` (Equality):** Checks if the **values** are the same. `a == b` will be `True`.
- **`is` (Identity):** Checks if they are the exact same **object in memory**. `a is b` will be `False`.

**How to share memory (if intended)**

If you actually *want* both variables to point to the same memory, you must assign one to the other:

```python
a = [1, 2, 3]
b = a  # b now points to the same memory address as a
print(a is b)  # Result: True
```

### **🔹 6. Membership Operators**

Test for element existence.

| Operator | Meaning | Example |
| --- | --- | --- |
| `in` | True if found | `3 in [1, 2, 3]` |
| `not in` | True if not found | `"x" not in "cat"` |

### **🔹 7. Bitwise Operators**

Work on bits (integers only).

| Operator | Name | Example (5=0101, 3=0011) | Result |
| --- | --- | --- | --- |
| `&` | AND | `5 & 3` | `1` (0001) |
| ` | ` | OR | `5 |
| `^` | XOR | `5 ^ 3` | `6` (0110) |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

💡 **Note**: `~x` equals `-(x+1)` because of two’s complement representation.

---

### **🔹 8. Special / Advanced Operators**

- **Walrus operator (`:=`)** — Assigns value as part of an expression.
    - More on walrus
        
        The **Walrus Operator** (`:=`), officially known as the **Assignment Expression**, was introduced in Python 3.8.
        
        It allows you to **assign a value to a variable as part of an expression**. Traditionally, assignment (`=`) is a statement that stands alone; the walrus operator lets you "sneak" an assignment into places like `if` statements or `while` loops.
        
        **1. The Syntax**
        
        The name comes from the operator's resemblance to the eyes and tusks of a walrus lying on its side.
        
        **python**
        
        ```python
        # Standard way
        n = len(data)
        if n > 10:
            print(n)
        
        # Walrus way
        if (n := len(data)) > 10:
            print(n)
        ```
        
        Use code with caution.
        
        **2. Common Use Cases**
        
        - **While Loops:** Great for "read until empty" patterns.
            
            **python**
            
            ```python
            while (block := file.read(256)) != '':
                process(block)
            ```
            
            Use code with caution.
            
        - **List Comprehensions:** Avoiding double-computation of expensive functions.
            
            **python**
            
            ```python
            results = [f(x) for x in data if (f(x) := heavy_computation(x)) > 0] # WRONG - syntax error
            # Correct way:
            results = [y for x in data if (y := heavy_computation(x)) > 0]
            ```
            
            Use code with caution.
            
        - **Regex Matching:** Capturing the match object and checking it simultaneously.
            
            **python**
            
            ```python
            if match := re.search(pattern, text):
                print(match.group(1))
            ```
            
            Use code with caution.
            
- **Overloaded operators** — Classes can define `__add__`, `__eq__`, etc., to change behavior.
- **Matrix multiplication (`@`)** — For NumPy/matrix math.

Example:

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)

a = Money(10)
b = Money(5)
c = a + b
print(c.amount)  # 15
```

### **🔹 Operator Precedence Table (Highest → Lowest)**

1. `()` Parentheses
2. `**` Exponentiation
3. `+x`, `x`, `~x` (Unary ops)
4. , `/`, `//`, `%`
5. `+`, 
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. Comparisons, `is`, `in`, `not in`, `is not`
11. `not`
12. `and`
13. `or`
14. `:=` Walrus operator

## Ternary Operator

In Python, the **ternary operator** is a shorthand way of writing an `if-else` statement **in a single line**.

It’s officially called the **conditional expression**.

**Syntax**

```text
value_if_true if condition else value_if_false
```

- `condition` → expression evaluated as `True` or `False`.
- If `condition` is `True` → result is `value_if_true`.
- If `condition` is `False` → result is `value_if_false`.

**Example**

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

Equivalent to:

```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

### **Nested Ternary Example**

You can nest them, but it can get messy:

```python
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B
```

Readability tip: Avoid too many nested ternary operators; use if-elif-else instead for clarity.

### **With Functions**

```python
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even(5))  # Odd
print(is_even(8))  # Even
```

### **With Lists or Dictionaries**

You can use ternary inside comprehensions:

```python
nums = [1, 2, 3, 4]
labels = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even']
```

```python
age = int(input("Please enter your age: "))

# Ternary Operator

print("You are teenager" if age <= 18 else "You are young" if 18 < age <= 30 else "You are adult" if 30 < age < 50 else "You are old")

# Equivalent if condition
if age <= 18:
    print("You are young")
elif 18 < age <= 30:
    print("You are young")
elif 30 < age < 50:
    print("You are adult")
else:
    print("You are old")

```

✅ **Key Points to Remember**

- Ternary operators return **values**, not statements.
- Always put **condition in the middle** between the two outcomes.
- Good for short, simple decisions; avoid for complex logic.
