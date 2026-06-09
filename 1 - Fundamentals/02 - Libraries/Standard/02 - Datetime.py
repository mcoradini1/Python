"""
DATETIME — Python Standard Library

Used 5.1 - For:
- dates
- times
- timestamps
- formatting
- time differences
"""

from datetime import datetime, date, timedelta

# ---------------------------------------------------------
# CURRENT DATE & TIME
# ---------------------------------------------------------

now = datetime.now()
print(now)

# ---------------------------------------------------------
# FORMATTING
# ---------------------------------------------------------

print(now.strftime("%Y-%m-%d %H:%M:%S"))

# ---------------------------------------------------------
# DATE ARITHMETIC
# ---------------------------------------------------------

today = date.today()
tomorrow = today + timedelta(days=1)
print(today, tomorrow)
