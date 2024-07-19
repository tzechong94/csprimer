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
