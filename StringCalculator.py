import re

def add(num):
    answers = num.split(,)
    test_strings = answers
    # Example usage
    test_strings = answers
    return answers
def find_numeric_values_with_regex(s):
     # Use regular expression to find all numeric values
     numeric_values = re.findall(r'\d+', s)
     return numeric_values

for test_string in test_strings:
    numeric_values = find_numeric_values_with_regex(test_string)
    print(f"Numeric values in '{test_string}': {numeric_values}")

