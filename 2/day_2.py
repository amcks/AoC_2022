# Set up benchmarking
import time
st = time.time()

# Prepare strategy dictionary
strat = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
        }

# Extract total strategy
raw = list(line.replace('\n', '') for line in open(r'./input_2'))
raw.remove('')

# Prepare total score & refer to dictionary
tot_score = 0
for i in raw:
    tot_score += strat[i]

# Print result
print("This strategy would have given me %s points" % tot_score)

# ------------
# Part 2
# Redefine dictionary with the correct strategy
true_strat = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
        }

# Recalculate new score
new_score = 0
for j in raw:
    new_score += true_strat[j]

# Print result
print("The correct strategy would have given me %s points" % new_score)

print("--- %s seconds ---" % (time.time()-st))
