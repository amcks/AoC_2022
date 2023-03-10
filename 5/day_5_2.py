# Set up benchmarking & other packages
import re
import time
st = time.time()


# Directly set up generator expression
input_gen = (line for line in open(r'./input_5'))

# Create coordinate matrix for box positions
pos_mat = []
for line in input_gen:
    if re.search(r'\d+', line) is None:
        row = []
        for j in range(int(len(line.replace("\n", ""))/4)+1):
            row.append("".join(re.findall(r'\w', line[4*j:4*j+4])))
        pos_mat.append(row)
    else:
        break

# Flush empty line after stack numbers
next(input_gen)

# Transpose coordinate matrix
trans_mat = list(map(list, zip(*pos_mat)))

# Extract & cleanup vectors
box_stack = []
for col in trans_mat:
    col.reverse()
    col = [elem for elem in col if elem != '']
    box_stack.append(col)

# Resume generator function, process operations
for line in input_gen:
    quant, init, fin = re.findall(r'\d+', line)
    q_idx = int(quant)
    for i in range(int(quant)):
        box_stack[int(fin)-1].append(box_stack[int(init)-1][-q_idx])
        del box_stack[int(init)-1][-q_idx]
        q_idx -= 1

# Extract final configuration
fin_conf = ''.join([stack[-1] for stack in box_stack])

# Print result
print("The final configuration of the stack tops is: %s" % fin_conf)

print("--- %s seconds ---" % (time.time()-st))
