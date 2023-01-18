# Set up benchmarking & other packages
import string
import time
st = time.time()

# Set up pseudo-dictionary auto-generation
prio_dict = list(string.ascii_letters)


# Input import generator function
# Because operations are on chunks of 3 rucksacks
def gen_read(file_path):
    f = open(file_path, "r")
    temp = f.readlines()
    gen_idx = len(temp)
    i = 0
    while i < gen_idx-3:
        yield temp[i:i+3]
        i += 3


# Process data from generator function
input_gen = gen_read(r'./input_3')
prio_list = []
for sub_gen in input_gen:
    prio_list.append(''.join(set.intersection(
        set(sub_gen[0].strip()),
        set(sub_gen[1].strip()),
        set(sub_gen[2].strip())
        )))

# Check score with pseudo-dictionary
prio_score = [prio_dict.index(prio_list[i]) for i in range(len(prio_list))]

# Current dictionary uses python indexing
# Additional index shift required
true_score = [prio+1 for prio in prio_score]

# Print result
print("Total badge priority: %s" % sum(true_score))

print("--- %s seconds ---" % (time.time()-st))
