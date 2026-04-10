# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculate and print the average score of students in a list.
- **Current Issue**: Missing `:` after the `if` condition causes a syntax error.
- **Fix Hint**: Add `:` at the end of the `if` statement.

## bug2.js
- **Intended Behavior**: Apply a discount based on membership status and print final prices.
- **Current Issue**: Uses assignment operator `=` instead of comparison (`===`), so the condition is always true.
- **Fix Hint**: Replace `=` with `===` in the `if` condition.

## bug3.java
- **Intended Behavior**: Populate an array with grades and calculate the average.
- **Current Issue**: Loop uses `<=` instead of `<`, causing an ArrayIndexOutOfBoundsException.
- **Fix Hint**: Change loop condition to `i < grades.length`.

## bug4.cpp
- **Intended Behavior**: Find and print the maximum number in an array.
- **Current Issue**: Loop stops at index 4 instead of checking all 6 elements.
- **Fix Hint**: Change loop condition to iterate until `i < 6`.

## bug5.cs
- **Intended Behavior**: Sum numeric digits from a string input and print the total.
- **Current Issue**: Attempts to add a string directly to an integer.
- **Fix Hint**: Convert each character to an integer using parsing (e.g., `input[i] - '0'`).