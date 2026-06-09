# ======================================================================================================================
# CHALLENGE 120: Dice to Store letters
# ======================================================================================================================

"""
Challenge: 11.3 - Dice to Store letters (120)
Category: 11 - Mini-Projects
Concepts Used:
    - .lower()
    - if()
    - sum()
    - sorted()
    - isalpha()
    - in
    -.get()
    - .items()
    - end = ''

Tags: .lower(), if(), sum(), sorted(), isalpha(), in, .get(), .items(), end = ''
Status: ✔️ Completed
"""


text = input("Enter a sentence: ")

# Convert to lowercase to count letters consistently (consider the text a list of strings)
text = text.lower()

# 6.3 - Dictionary to store letter counts
letter_counts = {}

# Count only alphabetic characters
for char in text:
    if char.isalpha():
        letter_counts[char] = letter_counts.get(char, 0) + 1

# Total number of letters
total_letters = sum(letter_counts.values())

print(f"\nTotal letters: {total_letters}")
print("Frequency of each letter:")

for letter, count in sorted(letter_counts.items()):
    print(f"{letter}: {count}", end=' | ')