# Set up benchmarking & other packages
import time
st = time.time()


# Set up generator function to import input
def gen_func(file_path):
    for line in open(file_path, "r"):
        yield line


# Set up initial counters for both parts
input_gen = gen_func(r'./input_4')
fullcont = 0
olap = 0

# Extract data & use set operations
for line in input_gen:
    rang_1, rang_2 = line.strip().split(",")
    a, b = rang_1.split("-")
    c, d = rang_2.split("-")
    set_1 = set(range(int(a), int(b)+1))
    set_2 = set(range(int(c), int(d)+1))
    if set_1 & set_2:
        olap += 1
        if set_1.issubset(set_2) or set_2.issubset(set_1):
            fullcont += 1

# Print results
print("Number of full containment cases: %s" % fullcont)

print("Number of partial overlapping cases: %s" % olap)

print("--- %s seconds ---" % (time.time()-st))
