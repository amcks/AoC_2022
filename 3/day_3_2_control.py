# Set up benchmarking & other packages
import string
import time
st = time.time()

# Set up pseudo-dictionary auto-generation
prio_dict = list(string.ascii_letters)

# Import input without generator function
with open(r'./input_3', "r") as f:
    input = f.readlines()

prio_list = []
i = 0
while i < len(input)-3:
    prio_list.append(''.join(set.intersection(
        set(input[i].strip()),
        set(input[i+1].strip()),
        set(input[i+2].strip())
        )))

    i += 3

prio_score = [prio_dict.index(prio_list[i]) for i in range(len(prio_list))]

# Current dictionary uses python indexing
# Additional index shift required
true_score = [prio+1 for prio in prio_score]

# Print result
print("Total badge priority: %s" % sum(true_score))

print("--- %s seconds ---" % (time.time()-st))
