import re

def find_numeric_values_with_regex(s):
    # Use regular expression to find all numeric values
    numeric_values = re.findall(r'\d+', s)
    return numeric_values

# Example usage
test_strings = [
    "123abc456def789",     # Mixed case with numbers and non-numeric values
    "42hello23world100",   # Another mixed case
    "12345",               # Only numbers
    "abcdef",              # Only non-numeric values
    "",                    # Empty string
]

for test_string in test_strings:
    numeric_values = find_numeric_values_with_regex(test_string)
    print(f"Numeric values in '{test_string}': {numeric_values}")
