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

## Lecture 6: Hashing

- reading in n numbers and then printing them out in sorted order. suppose you have access to a balanced dictionary data structure, which supports each of the operations search, nsert, delete, mininum, maximum, succesor and predecessor in log n time.
- explain how you can use this dictionary to sort in n log n time using only the following abstract operations: minimum, successor, insert and search

### Hash tables

- maintain a dictionary with O(1)
- hash function maps keys to integers

#### Collisions

set of keys mapped to the same bucket. if keys are uniformly distributed, each bucket should contain v few keys. short lists are easily searched.

- exemplified by birthday paradox

## Lecture 7: Heapsort/Priority Queues

problem of the day:
take as input a sequence of 2n real numbers. Design an O(n log n) algo that partitions the numbers into n pairs, with the property that the partition minimizes the maximum sum of the a pair.
For example, say we are given the numbers (1,3,5,9). the possible partitions are ((1,3),(5,9)), ((1,5),(3,9)) and ((1,9),(3,5)). the pair sums for these partitions are (4,14), (6,12) and (10,8). Thus the third partition has 10 as its maximum sum, which is the minimum over the three partitions.

### importance of sorting (n lg n)

#### Efficiency

- sorting is important because it makes other problems easy
- application of sorting: searching, eg binary search (lg n), closest pair (n), element uniqueness, mode, median and selection
- convex hull: given n points in two dimensions, find the smallest area polygon which contains them all.
  - once you have the points sorted by x-coordinate, they can be inserted from left to right into the hull, since the rightmost is always on the boundary.

### Selection sort / heapsort

#### selection sort

- scans through the entire array, repeated finding the smallest remaining element. n^2 if use arrays or unsorted linked lists.
- data structure matters. using balanced search trees or heaps, both of these operatoins can be done within lg n, for an n log n selection sort called heapsort.

#### priority queues

provide extra flexibility over sorting

- insert
- find min/max
- delete min/max
- each of these can be supported using heaps or balanced binary trees in O(log n)

#### Heap definition

defined ot be a binary tree with a key in each node such that:

- all elaves are on, at most, two adjacent levels
- all leaves on the lowest level occur to the left, and all levels excpt the lowest one are completed filled
- the key in root is <= all its children, and the left and right subtrees are again binary heaps.
- children of node i = 2i and 2i + 1

## Lecture 8: Mergesort / quicksort

- heap -> priority queue. insert new log n, delete log n, find min in constant time

problem of the day:
give an efficient algorithm to determine whether two sets (of size m and n) are disjoint. Analyze the complexity of your algorithm in terms of m and n. Be sure to consider the case where m is substantially smaller than n. disjoint -> no element in common.

n >= m

- build hash table (n + m) expected time
- build binary search tree
- merge sort

mergesort -> sort half half O(lg n) then merge (n)

- recursive algo are based on reducing large problems into small ones
- nice recursive approach to sorting involves partitioning the lements into two groups, sorting each of the smaller problems recursively, and then interleaving the two sorted lists to totally order the elements.

merging sorted lists -> two pointer technique O(n)

- divide and conquer
  - merging takes less time than solving the two subproblems, we get an efficient algo

Quicksort

-> in practice, the fastest internal sorting algo is quicksort, which uses partitioning as its main idea.
-> pick a pivot, pivot ends up in the correct place

partitioning

- we can partition an array about the pivot in one linear scan, by maintaining three sections, < pivot, > pivot and unexplored.
- as we scan from left to right, we move the left bound to the right when the element is less than the pivot, otherwise we swap it with the rightmost unexplored element and move the right bound one step clsoer to the left. n lg n best case if pivot is median everytime. worst case n^2

## lecture 9. linear sort

- nuts and bolts problem. You are given a collection of n bolts of different widths, and n corresponding nuts. you can test whether a given nut and bolt together, from which you learn whether the nut is too large, too small, or an exact match for the bolt. the differences in size between pair of nuts or bolts can be too small to see by eye, so you cannot rely on comparing the sizes of two nuts or two bolts directly. you are to match each bolt to each nut.

lower bound analysis

since any two different permutations of n elements requires a different sequence of steps to sort, there must be at least n! different paths from the root to leaves in the decision tree. Thus there must be at least n! different leaves in this binary tree.
Since a binary tree of height h has at most 2^h leaves, we know n! <= 2^h, or h >= lg(n!). By inspection n! > (n/2)^(n/2) since the last n/2 terms of the product are each greater than /2.

comparison sort -> n lg n best

Non-comparison based sorting

- initialize data structure, incrementing each bucket as you go along (n+k)

Bucketsort

- suppose we are sorting n numbers from 1 to m, where we know the numbers are approximately uniformly distributed. We can set up n buckets, each responsible for an interval m/n numbers from 1 to m.
- given an input number x, it belongs in bucket [xn/m]
- if we use an array of buckets, each item gets mapped to the right bucket in O(1) time. worst case all same bucket.

non-comparison sorts dont beat the bound.

## Lecture 10: Graph data structures

matching parenthesis -> use stack. left one push, right one pop. check if match.

h-index problem

intro to graphs (nodes and lines / vertices and edges)

- graph G = (V,E) is defined by a set of vertices V, and a set of edges E consisting of ordered or unordered pairs of vertices from V.
- vertex are points where two or more line segments or edges meet

flavors of graph -> learning the language to talk about the graph

### directed vs undirected

- a graph G = (V,E) is undirected if edge (x,y) E implies that (y,x) is also in E.
- road networks between cities are typically undirected (two way)
- street networks within cities are directed because of one way streets

### weighted vs unweighted graphs

- each edge of G is assigned a numerical value or weight
- edges of a road network graph might be weighted with their length, drive time or speed limit
- in unweighted graphs, there is no cost distinction between various edges and vertices

### Simple vs non-simple

- self loop is an edge (x,x) involving only one vertex
- an edge (x,y) is a multi-edge if it occurs more than once in the graph. -> more than one way to get from A to B. More than 1 road / multiple ways you know someone.
- any graph which avoids these structures is called simple / graph with these structures is called non-simple

### Sparse vs dense

- sparse when only a small fraction of the possible number of vertex pairs have edges defined between them
- graphs are usually sparse due to application-specific constraints. Road networks must be sparse because of road junctions.
- typically dense graphs have a quadratic number of edges while sparse graphs are linear in size.

### Data structures for graph

adjacency matrix
adjacency lists -> n x 1 array of pointers, where the ith element points to a linked list of the edges incident on vertex i.

- to test if edge (i,j) is in the graph we search the ith list for j, which takes O(di), where di is the degree of the ith vertex.

faster to test if (x,y) exists? matrix
faster to find vertex degree? lists
less memory on small graphs? lists (m + n) vs n^2
less memory on big graphs? matrices (small win)
edge insertion or deletion? matrics O(1)
faster to traverse the graph? lists m+n vs n^2
better for most problems? lists

## Lecture 11: Graph traversal

edges in adjacency lists

```c
typedef struct edgenode {
    int y;
    int weight;
    struct edgenode \*next;
} edgenode;
```

graph representation

```c
typedef struct graph{
    edgenode *edges[MAXV+1];
    int degree[MAXV+i];
    int nvertices;
    int nedges;
    int directed;
} graph
```

1. convert from an adjacency matrix to adjacency lists

for i from 1 to n, for j from 1 to m, if m[i,j] = 1, add edge (i,j) to adjacency list. n^2 to search, constant time to add.

2. list to matrix -> n + 2m. for undirected.

traversing a graph

- for efficiency we must make sure we visit each edge at most twice
- for correctness, we must do the traversal in a systematic way so that we don't miss anything
- since a maze is just a graph, such an algo must be powerful enough to enable us to get out of an arbitrary maze.

marking vertices 

- mark each vertex when we first visit it, and keep track of what have not yet been completely explored
- each vertex will always be in one of the following three states:
  - undiscovered - initial virgin state
  - discovered - after we have encountered it, but before we have checked out its incident edges
  - processed - vertex after we have visited all its incident edges

to do list

- we must maintain a structure containing all the vertices we have discovered but not yet completely explored
- initially only a single start vertex is considered to be discovered
- to completely explore a vertex, we look at each edge going out of it. for each edge which goes to an undiscovered vertex, we mark is discovered and add it to the list of work to do.
- regardless of what order we fetch the next vertex to explore, each edge is considered exactly twice, when each of its endpoints are explored.

correctness of graph traversal

- every edge and vertex in the connected component is eventually visited.
- suppose not, i.e there exists a vertex which was unvisited whose neighbour was visited. this neighbour will eventually be explored so we would visit it.

### Bread-first traversal

- visit every vertex and every edge exactly once in some well defined order. appropriate in shortest paths on unweighted graphs
- data structures:
  - use two boolean arrays
    - a vertex is discovered the first time we visit it
    - a vertex is considered processed after we have traversed all outgoing edges
    - once a vertex is discovered, it is placed on a FIFO queue. Thus oldest vertices/closest to the root are expanded first.
    - keep track of parent too
 
 n+2m too

finding paths

- parent array set within bfs() is very useful for finding interesting paths through a graph. the vertex which discovered vertex i is defined as parent[i]. the parent relation defines a tree of discovery with the initial search node as the root of the tree.

shortest paths and bfs

- in bfs, vertices are discovered in order of increasing distance from the root, so this tree has a very important property.
- unique tree path from root to any node uses the smallest number of edges possible on any root to x path in the graph.

recusion and path finding

- reconstruct this path by following chain of ancestors from x to the root. work backwards. cannot find path from root to x since that does not follow the direction of parent pointers. we must find the path from x to the root.

connected components.

- separate pieces of the graph such that there is no connection between the pieces.
- loop through all vertex, in case there are separate components, do a bfs for each vertex
- O(n(n+m))

## Lecture 12: Depth first traversal

- bipartite graph -> vertex colornig problem seeks to assign a label to each vertex of a graph such that no edge links any two vertices of the same colour. bipartite if it can be colored without conflicts while using only two colors. 
- consider graph of students and the courses they are registered for. no edges go btween student pairs or course pairs.

- finding a two coloring
  - we can augment bread-first search so that whenver we disocver a new vertex, we color it the opposite of its parent.

problem of the day

- prove that in a breadth first search on an undirected graph G, every edge in G is either a tree edge or a cross edge, where a cross edge (x,y) is an edge where x is neither an ancestor or descendent of y.

depth first search has a neat recursive implementation which eliminates the need to explicitly use a stack.

- tree edge, forward edge, back and cross edges
- Dfs: tree edges and back edges only
- bfs: tree or cross only

articulation vertex -> connected graph

- iff v is not a leaf and some subtree of v has no back edge incident until a proper ancestor of v
- topological sorting
- a directed, acyclic graph has no directed cycles
- ordering on the vertices so that all edges go from left to right.
- DAGs has at least one topological sort
- a directed graph is a dag iff no back edges are encountered during a depth first search
- labeling each of the vertices in the reverse order that they are marked processed finds a topological sort of a DAG.
- push each vertex on a stack soon as we have evaluated all outgoing edges, the top vertex on the stack always has no incoming edges from any vertex on the stack, repeatedly popping them off yields a topological ordering