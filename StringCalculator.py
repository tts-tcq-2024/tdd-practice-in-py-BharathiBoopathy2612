import re

def find_numeric_values_with_regex(s):
    numeric_values = re.findall(r'\d+', s)
    return numeric_values

def add(num):
  
        numeric_values = find_numeric_values_with_regex(num)
        print(f"Numeric values in '{num}': {numeric_values}")
