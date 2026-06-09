"""
REGULAR EXPRESSIONS — Python Fundamentals

The 're' module allows pattern matching in strings.
Useful 5.1 - For:
- validation
- searching
- replacing
- extracting data
"""

import re

# ---------------------------------------------------------
# BASIC SEARCH
# ---------------------------------------------------------

text = "My phone number is 123-456-7890"
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(match.group())

# ---------------------------------------------------------
# FIND ALL
# ---------------------------------------------------------

emails = "Contact: a@a.com, b@b.com"
found = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}", emails)
print(found)

# ---------------------------------------------------------
# REPLACE
# ---------------------------------------------------------

cleaned = re.sub(r"\d", "*", "Password123")
print(cleaned)

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------

pattern = r"^[A-Z][a-z]+$"
print(bool(re.match(pattern, "Marlon")))
print(bool(re.match(pattern, "marlon")))
