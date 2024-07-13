import re


    
def find_numeric_values_with_regex(s):
    numeric_values = re.findall(r'\d+', s)
    return numeric_values

def add(num):
    for test_string in num:
        numeric_values = find_numeric_values_with_regex(test_string)
        print(f"Numeric values in '{test_string}': {numeric_values}")
