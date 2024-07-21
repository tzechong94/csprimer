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

Walrus Operator allows you to assign a value to a variable within an expression.

# doctest

searches for pieces of text that look like interactive python sessions, and then executes those sessions to verify that they work exactly as shown

## Higher order functions

ability to build abstractions by assigning names to common patterns and then work in terms of names directly
there are common programming patterns that recur in code, used with number of different functions, these patterns can be abstracted by giving them names

need to construct functions that can accept other functions as arguments or return functions as values

functions that manipulate functions are called higher order functions

```python
def pi_sum(n):
    total, k = 0,1
    while k <= n:
        total, k = total + 8 / ((4*k-3)*(4*k-1)), k + 1
    return total
```

summation of terms

- takes two arguments the upper bound n together with the function term that computes the kth term

```python
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total = total + term(k)
        k = k +1
    return total
```

```python
def cube(x):
    return x*x*x
```

```python
def sum_cube(n):
    return summation(n, cube)
```

functions as general methods

```python
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y)< tolerance
```

Nested definitions

```python
def average(x,y):
    return (x+y)/2

def sqrt_update(x,a):
    return average(x, a/x)

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_close)
```

## Tic tac toe notes

#

## option 1

- model the state as the state of the board
- eg 3x3 array of arrays with player tokens for each item
- new moves are entered as (x,y) coords
- new moves are valid if array location is empty
- how to computer victory?
- printing the board is basically printing the state
- maybe we also store who is the current player
- would we need to be able to undo a move?
- we wuldnt be able to replay the game? or save partial game in a database and continue

## Option 2

- model the state as the sequence of moves
- derive the layout of the board prior sequence of moves
- computing victory is comparably hard/easy
- a little more work to print the board
- maybe a little more work to validate moves?
- if we want to support replaying a game or undoing moves, this will be straightforward

- state is a sequence of moves in a python list
- each moev will be modeled as an integer between 0 and 8 inclusive
- validation: must be an integer in range that hasn't already been selected
