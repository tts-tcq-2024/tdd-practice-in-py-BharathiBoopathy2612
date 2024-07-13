import re

def sum_numeric_values_with_limit_regex(s, limit=1000):
    # Use regular expression to find all numeric values
    numeric_values = re.findall(r'\d+', s)
    numeric_sum = 0

    # Convert numeric strings to integers and sum them with a limit
    for value in numeric_values:
        num = int(value)
        if numeric_sum + num > limit:
            break
        numeric_sum += num

    return numeric_sum

def add(num):
    numeric_sum = sum_numeric_values_with_limit_regex(num)
    return numeric_sum
        
