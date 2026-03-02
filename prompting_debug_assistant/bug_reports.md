## Bug Report – bug1.py

- **Summary**: Syntax error in the if statement prevented the program from executing.
- **Root Cause**: Missing colon : after the condition if len(students) > 0, which is required in Python syntax.
- **Resolution**: AI identified the missing colon and corrected the line to if len(students) > 0:. No manual edits were needed.
- **Lesson Learned**: Even small syntax elements like a missing colon can stop execution entirely; always check control structure syntax carefully.

## Bug Report – bug2.js

- **Summary**: Logical error caused discount to always be applied as if the user were a member.
- **Root Cause**: The condition if (isMember = true) used the assignment operator = instead of a comparison operator, which forced isMember to always become true.
- **Resolution**: AI corrected the condition to if (isMember === true) (alternative simplification: if (isMember)). No manual edits were needed.
- **Lesson Learned**: Confusing assignment (=) with comparison (== or ===) is a common logical bug in JavaScript; always use strict comparison to avoid unintended behavior.

## Bug Report – bug3.java

- **Summary**: Runtime exception occurred while populating the grades array.
- **Root Cause**: The loop condition i <= grades.length attempted to access an index equal to the array length, causing an ArrayIndexOutOfBoundsException.
- **Resolution**: AI corrected the loop condition to i < grades.length to ensure valid indexing. No manual edits were needed.
- **Lesson Learned**: When iterating through arrays in Java, always use < length instead of <= length to avoid out-of-bounds errors.

## Bug Report – bug4.cpp

- **Summary**: Off-by-one error caused the last element of the array to be excluded from the maximum value check.
- **Root Cause**: The loop condition i < 5 stopped iteration before reaching the final index (numbers[5]), potentially missing the true maximum value.
- **Resolution**: AI updated the loop condition to i < 6 to ensure all elements are evaluated. No manual edits were needed.
- **Lesson Learned**: Off-by-one errors are common in loop boundaries; always verify that iteration covers the full intended range of elements.

## Bug Report – bug5.cs

- **Summary**: Compilation error due to incorrect addition of a string to an integer.
- **Root Cause**: The statement total += input; attempted to add a string directly to an int, which is not allowed in C#.
- **Resolution**: AI replaced the line with total += input[i] - '0'; to correctly convert each character digit to its numeric value before addition. No manual edits were needed.
- **Lesson Learned**: Always ensure proper type conversion when working with characters and numeric values; implicit type mismatches can cause compilation failures.