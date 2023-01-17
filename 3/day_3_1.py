# Set up benchmarking & other packages
import string
import time
st = time.time()

# Set up pseudo-dictionary auto-generation
prio_dict = list(string.ascii_letters)

# Import input with context manager & split
str_a = []
str_b = []
with open(r'./input_3', "r") as f:
    for line in f:
        llen = len(line)
        str_a.append(line[0:llen//2])
        str_b.append(line[llen//2:].strip())

# Clean up trailing line break
del str_a[-1]
del str_b[-1]

# Extract identical character via set operations
miscat = [''.join(set(str_a[i]) & set(str_b[i])) for i in range(len(str_a))]
prio_score = [prio_dict.index(miscat[i]) for i in range(len(miscat))]

# Current dictionary uses python indexing
# Additional index shift required
true_score = [prio+1 for prio in prio_score]

# Print result
print("Total miscategorized priority: %s" % sum(true_score))

print("--- %s seconds ---" % (time.time()-st))
