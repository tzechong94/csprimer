from collections import deque


def wordladder(start, end, filename):
    # store all words of the same length
    if len(start) != len(end):
        return False
    if start == end:
        return start

    all_words_set = set()
    queue = deque([start])
    visited = set()

    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            if word:
                all_words_set.add(word)

    while queue:
        for i in range(len(start)):
            for c in "abcdefghijkmnopqrstuvwxyz":
                new_word = start[:i] + c + start[1 + i :]
                if new_word == end:
                    return new_word
                if new_word in all_words_set:
                    queue.append(new_word)
                    print(new_word)
            

        visited.add(start)
        start = queue.popleft()


if __name__ == "__main__":
    print(wordladder("cat", "dog", "words.txt"))
