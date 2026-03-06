# Prompt Testing Examples

## Example 1 – Refactoring Prompt
**Prompt**: You are a senior Python developer. Refactor the following Python function for readability.  

**Input**:
```python
def calc(a,b): return a+b*10
```

**AI Output**:
```python
def calculate_total(a: int, b: int) -> int:
    """Return a plus b times 10."""
    return a + (b * 10)
```

**Feedback**: Output is correct, but docstring could be more descriptive.


## Example 2 – Error Identification Prompt
**Prompt**: You are a Python debugging assistant. Analyze the code and error message to identify the cause of the problem.  

**Input**:
```python
numbers = [1, 2, 3]
print(numbers[3])
```

Error:
IndexError: list index out of range

**AI Output**:

The error occurs because the list contains three elements with indexes 0, 1, and 2.  
Trying to access index 3 is outside the valid range of the list, which causes the IndexError.

**Feedback**: The output clearly explains the cause of the error and identifies the incorrect index access.


## Example 3 – Bug Fixing Prompt
**Prompt**: You are an experienced Python developer. Identify and fix bugs in the following Python code.  

**Input**:
```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```

**AI Output**:
```python
def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

print(divide(10, 0))
```

**Feedback**: The output correctly identifies the problem and adds a check to prevent division by zero.


## Example 4 – Function Documentation Prompt
**Prompt**: You are a software documentation specialist. Generate documentation for the following Python function.  

**Input**:
```python
def multiply(a, b):
    return a * b
```

**AI Output**:

**Function Name**: multiply  
**Description**: Multiplies two numbers and returns the result.  

**Parameters**:
- a (int or float): The first number.  
- b (int or float): The second number.  

**Returns**:
- int or float: The product of a and b.

**Feedback**: The generated documentation clearly explains the function, its parameters, and the return value.


## Example 5 – Unit Test Generation Prompt
**Prompt**: You are a Python testing engineer. Generate unit tests for the following Python function.  

**Input**:
```python
def add(a, b):
    return a + b
```

**AI Output**:
```python
import unittest

class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
```

**Feedback**: The generated tests cover basic scenarios such as positive numbers, negative numbers, and zero, which helps verify the correctness of the function.