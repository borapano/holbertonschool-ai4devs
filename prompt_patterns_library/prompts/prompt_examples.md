# Prompt Testing Examples

## Example 1 – Refactoring Prompt
**Prompt**:  
Role: Senior Python Developer  
Task: Refactor the given Python code for better readability and structure.  
Input Placeholder: [PYTHON_FUNCTION]

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

**Feedback**: Output is correct and the code is more readable. A slightly more detailed docstring could improve the documentation.


## Example 2 – Error Identification Prompt
**Prompt**:  
Role: Python Debugging Expert  
Task: Analyze the code and error message to determine the cause of the issue.  
Input Placeholder: [CODE_SNIPPET] + [ERROR_MESSAGE]

**Input**:
```python
numbers = [1, 2, 3]
print(numbers[3])
```

Error:
IndexError: list index out of range

**AI Output**:

The error occurs because the list contains three elements with indexes 0, 1, and 2.  
Attempting to access index 3 exceeds the valid range of the list, which triggers the IndexError.

**Feedback**: The explanation clearly identifies the incorrect index access and explains why the error occurs.


## Example 3 – Bug Fixing Prompt
**Prompt**:  
Role: Experienced Python Software Engineer  
Task: Identify and fix bugs in the provided Python code.  
Input Placeholder: [BUGGY_CODE]

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

**Feedback**: The solution correctly detects the potential division by zero and adds a condition to prevent the runtime error.


## Example 4 – Function Documentation Prompt
**Prompt**:  
Role: Technical Documentation Specialist  
Task: Generate clear documentation for the provided Python function.  
Input Placeholder: [FUNCTION_CODE]

**Input**:
```python
def multiply(a, b):
    return a * b
```

**AI Output**:

Function Name: multiply  

Description: Multiplies two numbers and returns the result.

Parameters:  
- a (int or float): The first number.  
- b (int or float): The second number.

Returns:  
- int or float: The product of a and b.

**Feedback**: The generated documentation clearly explains the purpose of the function, its parameters, and the return value.


## Example 5 – Unit Test Generation Prompt
**Prompt**:  
Role: Python QA Engineer  
Task: Generate unit tests for the given Python function.  
Input Placeholder: [FUNCTION_CODE]

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

**Feedback**: The generated tests cover multiple cases including positive numbers, negative numbers, and zero, helping ensure the correctness of the function.