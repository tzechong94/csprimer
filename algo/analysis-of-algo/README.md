# Analysis of Algorithms (Fall 2001)

## Lecture 1. Intro to algo

- algo are ideas behind computer programs. solves a general, specified problem. specified by describing the set of instances it must work on, and what desired properties the output must have.

- correct and efficient
- expressing algorithms -> describe the ideas of an algorithm in english or picture, moving to pseudocode to clarify sufficiently tricky details of the algorithm

exhaustive search is slow, closest neighbour is not correct

- traveling salesman problem -> no correct algorithm
- demonstrate incorrectness. search for counter examples is the best way to disprove correctness of a heuristic
  - think about small examples
  - think about examples with ties on your decision criteria
  - think about examples with extremes of big and small

induction and recursion

1. base case
2. general assumption
3. general case

-> correctness requires proof, with no counter examples.

## Lecture 2. Asymptotic Notation

### Problem of the day

knapsack problem: given a set of integers S and a given target number T, find a subset of S which adds up exactly to T. For example, within S = {1,2,5,9,10}, there is a subset which adds up to T = 22 but not T=23.
Find counter examples to each of the following algorithms of the knapsack problem. That is, give an S and T such that the subset is selected using the algorithm does not leave the knapsack completely full, even though such a solution exists.

selecting the right jobs: maximum number of roles such that no jobs require his presense at the same time.

- first job to end: other jobs may well have started before the first to complete, but all must at least partially overlap both x and each other.
- seelct at most one fro mthe group. however selecting anything other than x would block out more opportunities after x.

### RAM model fo computation

- each simple operation takes 1 step (+, -, =, if, call)
- loops and subroutine calls are not simple operations. they depend upon the size of the data and the contents of a subroutine. 'sort' is not a single step operation
- each memory access takes exactly 1 step.
- measure run time of an algo by counting the number of steps.
- useful like flat earth model.

### Worst-case complexity

- defined by the maximum number of steps taken on any instance of size n.
- best, average, worst

## Lecture 2

### Names of bounding functions

- O is upper bound on g(n)
  - f(n) = O(g(n)) -> if there are positive constants n0 and c such that to the right of n0, the value of f(n) always lies on or below c.g(n)
- omega is lower bound on g(n) -> f(n) = omega(g(n)) if there are positive constants n0 and c such that to the right of n0, the value of f(n) always lies on or above c.g(n)
- theta is tight bound by g(n) -> f(n) = theta(g(n)) if there exist positive constants n0, c1, c2 such that to the right of n0, the value of f(n) always lies between c1.g(n) and c2.g(n) inclusive

### Big Oh multiplication

- multiplication by a constant does not change the asymptotics
- when multiplication by a function, both are important.

### Dominance

- adding a lower order term to a function doesnt change its big oh complexity

f(n) dominates g(n) if lim g(n)/f(n) = 0, which is same as saying g(n) = o(f(n)), little oh means grows strictly slower than

#### Dominance rankings

n! >> 2^n >> n^3 >> n^2 >> n log n >> n >> log n >> 1. exponential beats polynomial because exponents remains the same in polynomial.

n! >> c^n >> n^3 >> n^2 >> n^(1+e) >> n log n >> n >> sqrt(n) >> log^2(n) >> log n >> log n / log log n >> log log n >> a(n) >> 1

### Logarithms

a logarithm is simply an inverse exponential function. saying b^x = y is equivalent to saying x = log b y

- reflect how many times we can double something until we get to n, or halve something until we get to 1.
- eg binary tree and binary search. How many times can you double 1 until you get to n? lg n

## Lecture 4

### Base is not asymptotically important

### Elementary Data structures

stacks, queues, lists and heaps.

- abstract operations which it supports
- implementation of these operations

### Contiguous vs linked data structures

- whether they are based on arrays or pointers.
- contiguously allocated structures are composed of single slabs of memory and include arrays, matrices, heaps and hash tables
- linked data structures are composed of multiple distinct chunks of memory bound together by pointers, include lists, trees and graph adjacency lists

#### Arrays

structure of fixed size data records, each element can be efficiently located by its index or address.

- constant time access given index
- purely of data, no space wasted with links or other formatting info
- physical continuity between successive data accesses helps exploit high speed cache memory on modern computer architecture

#### Dynamic arrays

start with an array of size 1, double its size each time we run out of space. log2 n for n elements.

involves recopying of old contents on each expansion.

if half the elements move once ,a quarter of the elements twice, each of n elements move an average of only twic. total work of managing a dynamic array is the same O(n) as a simple array.

#### linked lists

1. overflow on linked structures can never occur unless memory is actually full
2. insertion and deletions are simpler than contiguous lists
3. with large records, moving pointers is easier and faster than moving the items themselves.

#### Stacks and queues

stacks -> last in first out

- push -> insert item x at the top of stack s
- pop -> return and remove the top item on stack s

queue -> first in first out

- enqueue -> insert item x at the back of the queue q
- dequeue -> return and remove the front item of the queue q

stacks more easily represented as an array, with push pop incrementing/decrementing a counter

queues are more easily represented as a linked list, with enqueue and dequeue operating on opposite ends of the list.

All can be done in O(1) with both arrays and lists.

-> depth first and breadth first search

#### Dictionary / dynamic set operations

- search(S, k) -> given a set S and a key value k, returns a pointer x to an element in S such that key[x] = k, or nil if no such element belongs to S
- insert(S, x) -> modifying operation that augments the set S with element x
- delete(S, x) -> given a pointer x to an element in the set S, remove x from S. Given a pointer to an element, not a key value.
- Min(S), Max(S) -> returns the element of the totally ordered set S which ahs the smallest (largest) key
- logical Predecessor(S,x), Successor(S,x) -> given an element x whose key is from a totally ordered set S, returns the next smallest (largest) element in S, or NIL if x is the maximum (mininum) element.

## Lecture 5: Dictionaries

- unsorted arrays
  - search O(n), insert O(1), delete O(1), minmax O(n), successor predecessor O(n)
- sorted
  - search O(logn), insert O(n), delete O(n), minmax O(1), successor predecessor O(1)

### Binary tree

- rooted tree where each node contains at most two children
- each child can be identified as either a left or right child

### Binary search tree

- a binary search tree labels each node x in a binary tree such that all nodes in the left subtree of x have keys < x and all nodes in the right subtree of x have keys > x

```c
typedef struct tree {
    item_type item;
    struct tree *parent;
    struct tree *left;
    struct tree \*right;
} tree;
```

```c
tree *search_tree(tree *l, item_type x) {
    if (l == NULL) {
        return (NULL);
    }
    if (l->item == x) {
        return (l);
    }
    if (x < l->item) {
        return (search_tree(l->left, x));
    } else {
        return (search_tree(l->right, x));
    }
}
```

time complexity of searching in a BST -> log n

min: time complexity -> O(h)

```c
tree *find_minimum(tree *t) {
    tree *min;
    if (t == NULL) {
        return NULL;
    }
    min = t;
    while (min->left != NULL) {
        min = min->left;
    }
    return (min);
}
```

in- order traversal: time complexity -> O(n), needs to traverse all the nodes

```c
void traverse_tree(tree *l) {
    if (l != NULL) {
        traverse_tree(l->left);
        process_item(l->item);
        traverse_tree(l->right);
    }
}
```

tree insertion -> O(h)

```c
void insert_tree(tree **l, item_type x, tree *parent) {

    if (*l == NULL) {
        p = malloc(sizeof(tree));
        p->item = x;
        p->left = p->right = NULL;
        p->parent = parent;
        *l = p;
        return;
    }
    if (x < (*l)->item) {
        insert_tree(&((*l)->left),x, *l);
    } else {
        insert_tree(&((*l)->right),x,*l);
    }
}
```
