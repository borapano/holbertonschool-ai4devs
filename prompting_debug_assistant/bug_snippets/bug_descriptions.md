## Bug 1 – bug1.py

**Intended Behavior**: Calculate and print the average score of students in a list.
**Issue Type**: Syntax error.
**Notes**: The program is missing : after the if condition, causing a syntax failure before execution.

## Bug 2 – bug2.js

**Intended Behavior**: Apply a discount based on membership status and print final prices.
**Issue Type**: Logical error.
**Notes**: The condition uses the assignment operator = instead of a comparison operator, making the discount always apply.

## Bug 3 – bug3.java

**Intended Behavior**: Populate an array with grades and calculate the average.
**Issue Type**: Runtime exception.
**Notes**: The loop uses <= instead of <, which causes an ArrayIndexOutOfBoundsException.

## Bug 4 – bug4.cpp

**Intended Behavior**: Find and print the maximum number in an array.
**Issue Type**: Off-by-one error.
**Notes**: The loop does not check the last element of the array, which may skip the actual maximum value.

## Bug 5 – bug5.cs

**Intended Behavior**: Sum numeric digits from a string input and print the total.
**Issue Type**: Misuse of data types or libraries.
**Notes**: The code attempts to add a string directly to an integer, causing a type mismatch error.