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

### String Encoding & Decoding
- **Encoding (String $\rightarrow$ Bytes):** Taking human-readable text (Unicode strings) and translating it into a sequence of raw bytes (`0`s and `1`s) using an encoding scheme like UTF-8. You do this when **saving to a file** or **sending data over a network**.  
- **Decoding (Bytes $\rightarrow$ String):** Taking raw bytes from a file or network and translating them back into a human-readable Unicode string using that same encoding scheme.  

In modern Python (Python 3), strings are natively managed as Unicode, and text data can be explicitly encoded and decoded:  
**A. Encoding (.encode('utf-8'))**
When you take a string and convert it to bytes:

```python
text = "Hello, 🚀"

# Encode the string into UTF-8 bytes
byte_data = text.encode('utf-8')

print(byte_data)
# Output: b'Hello, \xf0\x9f\x9a\x80'
```
Notice the b'' prefix indicating a bytes object. The standard English characters remain readable, but the rocket emoji 🚀 is translated into a sequence of 4 raw bytes (\xf0\x9f\x9a\x80).

#### Why Do We Need Encoding?

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

**B. Decoding (.decode('utf-8'))**
When you receive raw bytes (e.g., downloaded from an API or read from a binary file) and turn them back into readable text:

```python
encoded_bytes = b'Hello, \xf0\x9f\x9a\x80'

# Decode the bytes back into a Unicode string
original_text = encoded_bytes.decode('utf-8')

print(original_text)
# Output: Hello, 🚀
```

### The Core Analogy: The Universal Dictionary vs. Transmission

Imagine you want to send a secret message to a friend in another country.

• **Unicode is like a Universal Character Dictionary:** It contains every letter, symbol, and emoji from every human language (past and present), and assigns each one a unique ID number (called a **Code Point**). For example, the dictionary says the letter `A` is code point `65`, and the smiley face emoji `😀` is code point `128512`.

• **UTF-8 is like a Translation Rulebook (Encoding):** Computers don't understand "code points" directly; they only understand raw binary bytes (`0`s and `1`s). UTF-8 specifies *how* to translate Unicode’s code points into actual bytes so they can be saved on a hard drive or sent across the internet.

#### Unicode: The Blueprint
Before Unicode (created in the early 1990s), the world used fragmented systems like ASCII (which only supported English characters, numbers, and basic symbols using values 0 to 127). If a computer in Japan tried to open a file written in Cyrillic, it would show absolute gibberish because the character maps didn't match.
**Unicode solved this by creating a single global standard.**
• Every character gets a unique hexadecimal ID prefixed with `U+`. 

Examples:
- `A` $\rightarrow$ `U+0041`
- `ñ` $\rightarrow$ `U+00F1`
- `á` $\rightarrow$ `U+00E9`
- `🚀` $\rightarrow$ `U+1F680`

Crucially, **Unicode is just an abstract concept/catalog**. It does not define how those numbers are stored in computer memory. That is where encoding comes in.

#### UTF-8: The Encoding Rulebook

There are several ways to encode Unicode numbers into bytes (like UTF-32, UTF-16, and **UTF-8** became the absolute dominant standard on the web (used by over 98% of websites) because of one brilliant feature: **it is variable-length and backward-compatible with ASCII.**  
How UTF-8 allocates bytes based on the size of the Unicode code point:
• **1 Byte (8 bits):** Used for standard English letters and numbers (ASCII). Code points `U+0000` to `U+007F`. (e.g., `A` takes up just 1 byte).
• **2 Bytes:** Used for Latin-extended, Greek, Cyrillic, Hebrew, Arabic characters.
• **3 Bytes:** Used for complex scripts like Chinese, Japanese, and Korean (CJK) characters.
• **4 Bytes:** Used for rare historic scripts and **Emojis** (`🚀`).
Because of this smart design, if your text is purely English, UTF-8 files take up half the space they would in a fixed 16-bit or 32-bit encoding format.

#### Encoding & Decoding in Files

**writing Text to a File (Encoding)**

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

#### What Causes Unicode Errors?

#### ❌ UnicodeDecodeError

Occurs when Python tries to decode bytes using the **wrong encoding**.

Example:

```python
b ="你好".encode("utf-8")
b.decode("ascii")# ❌ error

```

Why?

- ASCII doesn’t know how to decode Chinese characters

---

#### ❌ UnicodeEncodeError

Occurs when Python tries to encode characters into an encoding that **can’t represent them**.

Example:

```python
"你好".encode("ascii")# ❌ error

```

#### The Golden Rule 🏆

> Always know the encoding of your data
> 

If data comes from:

- Web → UTF-8 (almost always)
- Files → check encoding
- Databases → usually UTF-8
- APIs / JSON → UTF-8 by default

---

#### Bytes vs String (Very Important in Python)

#### String (`str`)

- Human-readable
- Unicode characters

```python
s ="Hello"

```

#### Bytes (`bytes`)

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

#### Example: Web Request

```
Usertypestext
→ Python string
→ encode (UTF-8)
→ send bytesover internet
→ receive bytes
→ decode (UTF-8)
→ Python string
```

#### Visual Summary

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

#### Why Python 3 Is Great

- Strings are **Unicode by default**
- Fewer encoding headaches than Python 2
- UTF-8 is the standard

#### Checking Type**

```python
print(isinstance("hello", str))  # True
```

---

✅ **Key Takeaways**:

- Strings are **immutable sequences** of Unicode characters.
- Use **indexing/slicing** to access parts of strings.
- Learn **built-in methods** for text processing.
- Use **f-strings** for modern, readable formatting.