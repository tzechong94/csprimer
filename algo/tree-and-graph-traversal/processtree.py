"""
write a program that reformats the output 
of ps to display it as a tree, based on parent process id

- read from stdin
- use first line to determine/validate pid, ppid and etc fields
- for each subsequent line
    - tokenize by splitting
    - extract pid, ppid, [etc]
    - create instance of process (effectively a tree node) with "children" attribute
    - recursively check if ppid of this process is pid of any process in our tree
        - if so, add as child
        - else, add this process to root, and check if any root process should be 
        parented under this process
- for each process in root:
    print that process' info, then recursively run this print routine
"""

# class Process:
#     def __init__(self, pid, ppid, args, children):
#         self.pid = pid
#         self.ppid = ppid
#         self.args = args
#         self.children = children


# def processtree(inputlines):
#     headers = inputlines.readline().strip().split()
#     result = {}
#     while True:

#         line = inputlines.readline()
#         if not line:
#             break
#         fields = line.strip().split(None, len(headers) - 1)

#         pid = int(fields[0])
#         ppid = int(fields[1])
#         args = fields[2:]
#         process = Process(pid, ppid, args, [])
#         if ppid in result.keys():
#             result[ppid].children.append(process)
#         else:
#             result[ppid] = process

#     return result

import sys


class Process(object):
    def __init__(self, pid, ppid, info):
        self.pid = pid
        self.ppid = ppid
        self.info = info
        self.children = []


def find(node, test):
    if test(node):
        return

    for child in node.children:
        parent = find(child, test)
        if parent is not None:
            return parent

    return None


def print_processes(processes, depth=0):
    for p in processes:
        print("    " * depth, p.pid, p.info)
        print_processes(p.children, depth + 1)


def main():
    header = sys.stdin.readline().split()
    try:
        pid_idx = header.index("PID")
        ppid_idx = header.index("PPID")
    except ValueError:
        print("Usage: ps -o ppid,ppid,[etc] | python3 pstree.py", file=sys.stderr)
        exit(1)

    root = []  # is this just the children of a root node

    for line in sys.stdin:
        parts = line.split()
        pid = int(parts[pid_idx])
        ppid = int(parts[ppid_idx])
        info = " ".join(x for i, x in enumerate(parts) if i not in {pid_idx, ppid_idx})
        proc = Process(pid, ppid, info)

        for node in root:

            parent = find(node, lambda n: n.pid == ppid)
            if parent is not None:
                parent.children.append(proc)
                break
        else:
            for i, p in enumerate(root):
                if p.ppid == pid:
                    proc.children.append(p)
                    root.pop(i)
                    break
            root.append(proc)

    print_processes(root)


if __name__ == "__main__":
    main()
