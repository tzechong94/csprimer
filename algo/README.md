# Algo and data structures

## How to solve it by Polya

1. understand the problem
   1. heuristics
      1. draw a figure
      2. be systematic
      3. is this similar to a solved problem
      4. induction -> generalise from specific cases
      5. decomposing/recomposing
      6. sovle an easier problem (auxilliary problem)
      7. definition
2. devise a plan
3. implement the plan
4. reflect/revise

Benefits and pitfalls of asymptotic analysis

hazards:

- constant factors may matter
- n is often small
- maintenance cost
- space is time

pros:

- system agnostic understanding of algo

## Building an intuition for common running times

1. constant ish -> perfect
2. linear ish -> straightforward
3. polynomial ish -> doable, maybe tricky
   1. n^2 more than 10000 is very huge.
4. exponential ish -> impossible
   1. 100 and above is impossible.

2^100 can't be computed. too huge

## Hazards of using linked list

linked lists use has diminished as the cost of accessing RAM has increased relative to the time taken to do computing. RAM latency improved, but much less than CPU speeds, so it may take order of 100x longer to follow a pointer to the next node in a linked list, than to access the next value in an array, assuming the array values tend to reside in cache where linked list nodes do not.

1. performance
   1. nodes are far apart, next pointer might point too far away
   2. taking multiple trips to ram, instaed of using arrays where there will be more cache hits
   3. pre allocate nodes so they will be closer together

2. linked list implemented with pointers cannot be serialized (to store or send over the network) as the addresses are only meaningful in the context of a running process. They can be implemented in a relocatable manner instead, with relative references, but this requires some extra care in programming or a costly serialization process.

## What is an abstract data type?

- use other data structures to simulate others.

- discourage use of linkedlist, but it gives a good intro to graphs and trees
- linkedlist is like a special tree. if multiple children -> tree. if multiple parents, graph.

## Stacks and queues

any recursive problem can be reformulated as one that uses a stack, and in doing so we are replicating the role of the function call stack (perhaps in a way that improves performance, or that increases code reuse)

able to use same logic for breadth first or depth first traversal of a hierarchy depending on whether we use a queue or stack respectively to remember the paths that remain to search.

## Divide and conquer intuition, and convex hull problem

convex hull

- points can only be at 1 end of the line
-  