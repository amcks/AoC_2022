# Set up benchmarking & other packages
import string
import time
st = time.time()

# Set up pseudo-dictionary auto-generation
prio_dict = list(string.ascii_letters)


# Input import generator function
def gen_read(file_path):
    for line in open(file_path, "r"):
        yield line


input_gen = gen_read(r'./input_3')
prio_list = []
sub_gen = []
i = 0

# Chunking in threes shifted to outside generator
for line in input_gen:
    if i % 3 == 0 and i != 0:
        prio_list.append(''.join(set.intersection(
            set(sub_gen[0].strip()),
            set(sub_gen[1].strip()),
            set(sub_gen[2].strip())
            )))

        sub_gen = []
        sub_gen.append(line)
        i += 1

    else:
        sub_gen.append(line)
        i += 1


# Check score with pseudo-dictionary
prio_score = [prio_dict.index(prio_list[i]) for i in range(len(prio_list))]

# Current dictionary uses python indexing
# Additional index shift required
true_score = [prio+1 for prio in prio_score]

# Print result
print("Total badge priority: %s" % sum(true_score))

print("--- %s seconds ---" % (time.time()-st))
