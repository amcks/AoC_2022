# Set up benchmarking & other packages
import re
import time
st = time.time()


# Set up generator function to import input
def gen_func(file_path):
    """
    Generator function: reads file_path line-by-line.
    """
    for line in open(file_path, "r"):
        yield line


def vals(x):
    """
    Counts total values in directories and subdirectories
    recursively.
    """
    if isinstance(x, dict):
        result = []
        for v in x.values():
            result.extend(vals(v))
        return result
    else:
        return [x]


def cycle(depth, mode):
    """
    Cycles through directory tree dictionary
    either to scan the total memory, or to find
    appropriately sized directory to delete.
    """
    for d in depth.values():
        if isinstance(d, dict) and mode == "scan":
            global totmem
            if sum(vals(d)) < 100000:
                totmem.extend(vals(d))
                cycle(d, "scan")
            else:
                cycle(d, "scan")
        elif isinstance(d, dict) and mode == "del":
            global todel, delmem
            if sum(vals(d)) > todel:
                delmem.append(sum(vals(d)))
                cycle(d, "del")
            else:
                cycle(d, "del")


# Create generator object & prepare counters
input_gen = gen_func(r'./input_7')
cwd = [next(input_gen).strip().split(" ")[2]]
dir_tree = {}
totmem = []
delmem = []

# Represent directory tree as nested dictionary
for line in input_gen:
    tempdir = dir_tree
    if re.search("[$]", line):
        temp = line.strip().split(" ")
        if temp[1] == "cd" and temp[-1] != "..":
            cwd.append(temp[2])
            for dirs in cwd:
                tempdir = tempdir.setdefault(str(dirs), {})
        elif temp[-1] == "..":
            del cwd[-1]
    elif re.search(r'\d+', line):
        temp = line.strip().split(" ")
        for dirs in cwd:
            tempdir = tempdir.setdefault(str(dirs), {})
        tempdir = tempdir.setdefault(str(temp[1]), int(temp[0]))

# Cycle through generated directory tree to scan & check deletion
cycle(dir_tree, "scan")
todel = -40000000 + sum(vals(dir_tree))
cycle(dir_tree, "del")


# Print result
print("Total memory of directories under 100000: %s" % sum(totmem))
print("Total memory of smallest directory to be deleted: %s" % min(delmem))

print("--- %s seconds ---" % (time.time()-st))
