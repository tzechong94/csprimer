# Luhn algorithm

simple check digit formula used to validate a variety of identification numbers.

## Problem

Write a simple problem to validate credit card numbers with the Luhn formula + its tests

### More about Luhn Algorithm

- not intended to be cryptographically secure hash function; designed to protect against accidental errors, not malicious attacks

### Description --> computing check digit / validating check digit

1. if number contains the check digit, drop that digit to form the 'payload'. Check digit is often the last digit.
2. with payload, start from rightmost digit. Moving left, double the value of every second digit (including the rightmost digit)
3. Sum the values of the resulting digits
4. The check digit is calculated by (10 - (s mod 10)), where s is the sum from step 3. This is the smallest number (possibly zero) that must be added to s to make a multiple of 10. Other valid formulas giving the same value are 9-((s+9)mod 10),(10-s)mod10, and 10[s/10]-s. 1st formula might not work in all environments because of how negative numbers are handled by modulo operation.
5. step 4 is the check digit. step 5 you can check if original check digit = computed check digit

### Strengths and weaknesses

- will detect all single digit errors, but cannot detect transpositino of two digit sequence
- will detect most of possible twin errors

### Plan

Now:

- write a function verify(digits) -> true/false, which validates a string of digit characters according to Luhn algorithm
- the final digit will be check digit: iterate through others in reverse order,
  doubling each second digit (starting from rightmost non-check digit), adding together the resulting digits, combining to compute a total, which should be 10 - checkdigit mod 10
- testing strategy: verify(17893729974) -> True, verify(17893729975) -> False
- stick to simple imperative style (step by step)

Later:

- don't assume input is well formed, add extra tests to cover
- general refactor
- consider functional formulation
- lookup table / pre caching

ls luhn.py | entr -s 'date; python3 luhn.py' -> passes the piped output to entr (Event Notify Test Runner)

other notes:

- enumerate gives index without creating a new list

### A quick tour of iterators in Python

- more efficient if you want to iterate things without storing in memory. use range instead of array
- cannot assign
- being an iterator = having next method.
- iteration as an abstraction without materialising sequencing to memory when you dont need it
- zip creates an iterator without creating the list
- 

### others learnings

array[3] more efficient than dictionary[30] on average although both O(1)

