text = input("Enter a sentence: ")

# Convert to lowercase to count letters consistently (consider the text a list of strings)
text = text.lower()

# Dictionary to store letter counts
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