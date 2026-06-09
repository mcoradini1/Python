"""
JSON HANDLING — Python Fundamentals

JSON is a lightweight data format used 5.1 - For APIs, config files, etc.
Python provides the 'json' module to read/write JSON.
"""

import json

# ---------------------------------------------------------
# DICTIONARY → JSON STRING
# ---------------------------------------------------------

person = {"name": "Marlon", "age": 31, "weight": 90}
json_str = json.dumps(person, indent=4)
print(json_str)

# ---------------------------------------------------------
# JSON STRING → DICTIONARY
# ---------------------------------------------------------

loaded = json.loads(json_str)
print(loaded["name"])

# ---------------------------------------------------------
# WRITE JSON TO FILE
# ---------------------------------------------------------

with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

# ---------------------------------------------------------
# READ JSON FROM FILE
# ---------------------------------------------------------

with open("person.json", "r") as f:
    data = json.load(f)
    print(data)
