"""
build graph, bfs from start to end words
each word in our dict is a vertex, edges are defined by 
pairs of words that differ only by 1 letter

dev goals:
- build graph itself
- perform any kind of traversal
- perform bfs
track/print the path

options: 
- not build graph, just o(n) scan to expand each vertex
- build graph by brute force: for each word, consider if each other word is a neighbour
- scan words, and group tgt sets that match each pattern

plan
- consider templates/placeholdes? ?OUR, F?UR, and add the word to a dict where keys are templates, values are matching words
- build graph where keys are words, values are sets of connected words, as defined by each pair of words in each template bucket
- search this graph bfs

def bfs(graph, start, goal):
    q = [start]
    visited = set()
    while q is not empty:
        x = q.next()
        if x is goal:
            return x
        for neighbour in x.neighbours:
            if neighbour not in visited:
                q.add(neighbour)
                visited.add(x)
    return None
"""

from collections import defaultdict


def build_graph(words):
    buckets = defaultdict(list)
    for w in words:
        for i in range(len(w)):
            template = "".join(ch if i != j else "?" for j, ch in enumerate(w))
            buckets[template].append(w)
    graph = defaultdict(list)
    for bucket in buckets.values():
        for x in bucket:
            for y in bucket:
                if x != y:
                    graph[x].append(y)

    return graph


def ladder(graph, start, goal):
    q = [(start, [start])]  # TODO use actual queue data structure
    visited = set()
    while q:
        x, path = q.pop(0)
        if x == goal:
            return path
        for y in graph[x]:
            if y not in visited:
                q.append((y, path + [y]))
                visited.add(y)
    return None


if __name__ == "__main__":
    with open("words.txt", "r") as f:
        graph = build_graph(w.strip().lower() for w in f.readlines())
    print(graph["big"])
    print(ladder(graph, "pig", "sty"))
    print(ladder(graph, "pig", "pit"))
    print(ladder(graph, "pig", "pig"))
    print(ladder(graph, "pig", "piggy"))
    print(ladder(graph, "black", "white"))
