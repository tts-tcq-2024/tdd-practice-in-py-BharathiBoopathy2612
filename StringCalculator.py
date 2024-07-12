import re

def add(num):
  answer = num.split(',')
  
    def find_numeric_values_with_regex(answer):
      # Use regular expression to find all numeric values
        numeric_values = re.findall(r'\d+', s)
        return numeric_values

    for test_string in answer:
        numeric_values = find_numeric_values_with_regex(test_string)
        print(f"Numeric values in '{test_string}': {numeric_values}")
