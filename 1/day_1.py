# Set up benchmarking
import time
st = time.time()

# Prepare list
chnk = [0]

# Import input with context manager
with open(r'./input_1', "r") as f:
    for line in f:
        if line == '\n':
            chnk.append(0)
        else:
            chnk[-1] += int(line)

# Answer to Part 1
print("Initial max calories: %i" % max(chnk))

# ---------------
# Set up lists & iteration indices
i = 0
top_i = 3
chnk_top = 0

# Iteratively sample max w/o replacement
while i < top_i:
    chnk_top += max(chnk)
    chnk.remove(max(chnk))
    i += 1

print("Calories from top 3 elves: %i" % chnk_top)

print("--- %s seconds ---" % (time.time()-st))
