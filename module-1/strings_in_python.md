### **1. Definition**

A **string** is a sequence of characters (letters, numbers, symbols, spaces) enclosed in quotes. It is an instance of built in class str.

- Unicode means it can store letters, numbers, emojis, and symbols from almost any language.
- In Python, a string is an **immutable** object of the built-in `str` class.

```python
s = "Hello"
print(type(s))  # <class 'str'>
```

### Creating Strings

Strings can be created using:

- Single quotes `'...'`
- Double quotes `"..."` (both work the same)
- Triple quotes `'''...'''` or `"""..."""` for multi-line or docstrings

```python
s1 = 'Hello'
s2 = "Hello"
s3 = '''Multi-line
string example'''
```

### String Immutability

Once created, a string **can not be changed**.

- You **can** create a new string based on an old one, but you **cannot** modify the original in-place.

```python
word = "Python"
# word[0] = "J"  # ❌ Error: 'str' object does not support item assignment
word = "J" + word[1:]  # ✅ Creates new string
print(word)  # "Jython"
```

### Accessing Characters (Indexing)

Strings are like sequences — you can access characters by index.

```python
name = "Alice"
print(name[0])   # 'A' (first character)
print(name[-1])  # 'e' (last character)
```

- Index starts at `0` (first char).
- Negative indexing starts from the end (-`1` = last char).

### Slicing Strings

Slicing syntax: `string[start:end:step]`

- `start` → where to begin (inclusive)
- `end` → where to stop (exclusive)
- `step` → jump between characters

```python
word = "Python"
print(word[0:4])   # 'Pyth'
print(word[:4])    # 'Pyth' (start default = 0)
print(word[2:])    # 'thon' (end default = end of string)
print(word[::2])   # 'Pto' (every 2nd char)
print(word[::-1])  # 'nohtyP' (reversed string)
```

### String Operations

### Concatenation:

```python
a = "Hello"
b = "World"
print(a + " " + b)  # "Hello World"
```

### Repetition:

```python
print("ha" * 3)  # "hahaha"
```

### Membership:

```python
print("Py" in "Python")         # True
print("Java" not in "Python")   # True
```

### Looping Through Strings

```python
for char in "Python":
    print(char)
```

### Common String Methods (Detailed Table)

| Method | Description | Example |
| --- | --- | --- |
| `lower()` | Converts to lowercase | `"Hello".lower()` → `"hello"` |
| `upper()` | Converts to uppercase | `"Hello".upper()` → `"HELLO"` |
| `title()` | Capitalizes each word | `"hello world".title()` → `"Hello World"` |
| `capitalize()` | Capitalizes first char | `"python".capitalize()` → `"Python"` |
| `strip()` | Removes spaces (both sides) | `"  hello  ".strip()` → `"hello"` |
| `lstrip()` / `rstrip()` | Remove spaces from left/right | `"  hi".lstrip()` → `"hi"` |
| `replace(old, new)` | Replace substring | `"I like Java".replace("Java", "Python")` → `"I like Python"` |
| `split(sep)` | Splits into list | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `join(iterable)` | Joins elements into string | `"-".join(["a", "b"])` → `"a-b"` |
| `find(sub)` | First occurrence index (-1 if not found) | `"Python".find("th")` → `2` |
| `index(sub)` | Like find(), but error if not found | `"Python".index("th")` → `2` |
| `count(sub)` | Count occurrences | `"banana".count("a")` → `3` |
| `startswith()` | Checks prefix | `"Python".startswith("Py")` → `True` |
| `endswith()` | Checks suffix | `"Python".endswith("on")` → `True` |
| `isdigit()` | True if all chars are digits | `"123".isdigit()` → `True` |
| `isalpha()` | True if all chars are letters | `"abc".isalpha()` → `True` |
| `isalnum()` | Letters or digits only | `"abc123".isalnum()` → `True` |
| `isspace()` | True if only spaces | `"   ".isspace()` → `True` |
|  |  |  |

**Use** `print(dir(x))` to see all available methods for an object

### String Formatting

#### f-Strings (Python 3.6+):

```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
```

#### `format()` method:

```python
print("My name is {} and I'm {} years old.".format(name, age))
```

#### Old-style formatting:

```python
print("My name is %s and I'm %d years old." % (name, age))

```

### Escape Sequences

| Sequence | Meaning |
| --- | --- |
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

```python
print("Hello\nWorld")

```

### Raw Strings

Raw strings ignore escape sequences.

```python
path = r"C:\Users\Name"
print(path)  # C:\Users\Name

```

### Multi-line Strings

Using triple quotes:

```python
msg = """Line 1
Line 2"""
```

### String Encoding & Bytes

Encoding and decoding are about **converting between text (characters) and bytes**. Strings are Unicode, but you can encode them to bytes:

```python
s = "Python"
b = s.encode("utf-8")
print(b)        # b'Python'
print(b.decode("utf-8"))  # 'Python'
```
**Encoding** converts a **string (`str`)** into **bytes (`bytes`)** using a character set (like UTF-8).

```python
s ="Python"
b = s.encode("utf-8")
print(b)
```

Output:

```python
b'Python'
```

What happened in memory:

```
"P" →80
"y" →121
"t" →116
"h" →104
"o" →111
"n" →110
```

Stored as bytes:

```python
b'\x50\x79\x74\x68\x6f\x6e'
```

### What Is Decoding?

**Decoding** converts **bytes back into text**.

```python
b.decode("utf-8")

```

Python:

- reads each byte
- looks it up in UTF-8
- converts it back to characters

Result:

```python
"Python"

```

---

### Why Do We Need Encoding?

Because **computers don’t understand text**, only numbers.

Encoding is needed when:

- 📁 Writing to files
- 🌐 Sending data over the internet
- 🧠 Communicating with databases
- 📡 Using APIs or sockets

Example:

```python
withopen("file.txt","wb")as f:
    f.write("Hello".encode("utf-8"))
```

### Why UTF-8?

**UTF-8 is** **the standard variable-width character encoding used to translate human-readable text (Unicode) into binary data (bytes) that a computer can store and process**

Unicode is NOT an encoding. Unicode is a standard that assigns a unique number to every character in almost every writing system. Think of Unicode as a giant dictionary.

```
Character
     ↓
Unicode
(U+1F60A)
     ↓
UTF-8
(bytes)
```

UTF-8 is:

- Universal
- Backward compatible with ASCII
- Can represent **every character in Unicode**

Example:

```python
"é".encode("utf-8")# b'\xc3\xa9'
"你".encode("utf-8")# b'\xe4\xbd\xa0'

```

Different characters use different numbers of bytes.

Unicode answers:

    What character is this?

UTF-8 answers:

    How do we store it as bytes?

---

### ASCII vs Unicode vs UTF-8

### ASCII (Very Old)

- Uses **7 bits**
- Can represent only **128 characters**
- English letters, digits, symbols

Examples:

```
A →65
a →97
0 →48

```

❌ Problems:

- No emojis
- No accented letters (é, ñ)
- No non-English languages

---

### Unicode (The Big Idea)

Unicode is **not an encoding** — it’s a **global character map**.

It says:

> “Every character in every language gets a unique number.”
> 

Examples:

```
A   → U+0041
é   → U+00E9
你  → U+4F60
😀 → U+1F600

```

Unicode solves the *language problem*, but it doesn’t say **how to store these numbers in bytes**.

That’s where UTF-8 comes in.

---

### UTF-8 (Most Important)

UTF-8 is an **encoding** for Unicode.

It converts Unicode characters into **bytes**.

### Why UTF-8 is special:

- Uses **1 to 4 bytes**
- English letters = **1 byte** (same as ASCII)
- Other languages use more bytes
- Backward compatible with ASCII
- Used almost everywhere (web, Python, Linux)

Example:

```python
"A".encode("utf-8")# b'\x41'
"é".encode("utf-8")# b'\xc3\xa9'
"你".encode("utf-8")# b'\xe4\xbd\xa0'
```

### Encoding & Decoding in Files

### Writing Text to a File (Encoding)

```python
text ="Hello 你"
withopen("file.txt","w", encoding="utf-8")as f:
    f.write(text)

```

What happens:

```
str → encode →bytes → file

```

---

### Reading Text from a File (Decoding)

```python
with open("file.txt","r", encoding="utf-8")as f:
    content = f.read()

```

What happens:

```
file →bytes → decode →str

```

### What Causes Unicode Errors?

### ❌ UnicodeDecodeError

Occurs when Python tries to decode bytes using the **wrong encoding**.

Example:

```python
b ="你好".encode("utf-8")
b.decode("ascii")# ❌ error

```

Why?

- ASCII doesn’t know how to decode Chinese characters

---

### ❌ UnicodeEncodeError

Occurs when Python tries to encode characters into an encoding that **can’t represent them**.

Example:

```python
"你好".encode("ascii")# ❌ error

```

### The Golden Rule 🏆

> Always know the encoding of your data
> 

If data comes from:

- Web → UTF-8 (almost always)
- Files → check encoding
- Databases → usually UTF-8
- APIs / JSON → UTF-8 by default

---

### Bytes vs String (Very Important in Python)

### String (`str`)

- Human-readable
- Unicode characters

```python
s ="Hello"

```

### Bytes (`bytes`)

- Raw binary data
- Used by files, networks

```python
b =b"Hello"

```

❌ You cannot mix them:

```python
"Hello" +b"World"# TypeError

```

✅ Convert explicitly:

```python
"Hello".encode("utf-8") +b"World"

```

---

### Example: Web Request

```
Usertypestext
→ Python string
→ encode (UTF-8)
→ send bytesover internet
→ receive bytes
→ decode (UTF-8)
→ Python string
```

### Visual Summary

```
TEXT (str)
   |
   | encode("utf-8")
   v
BYTES (bytes)
   |
   | decode("utf-8")
   v
TEXT (str)

```

---

### Why Python 3 Is Great

- Strings are **Unicode by default**
- Fewer encoding headaches than Python 2
- UTF-8 is the standard

### Checking Type**

```python
print(isinstance("hello", str))  # True
```

---

✅ **Key Takeaways**:

- Strings are **immutable sequences** of Unicode characters.
- Use **indexing/slicing** to access parts of strings.
- Learn **built-in methods** for text processing.
- Use **f-strings** for modern, readable formatting.