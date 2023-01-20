# Set up benchmarking & other packages
import time
st = time.time()
cnt = 0
brk_flg = False
carr_len = int(input("Length of data string with unique characters:"))


# Function to evaluate each text carriage
def car_scan(carr):
    global cnt, brk_flg, carr_len
    temp_cnt = []
    temp_cnt = [carr.count(i) for i in carr]
    for i in range(carr_len):
        if temp_cnt[i] > 1:
            return
    brk_flg = True


# Read file in shifting buffer chunks
# Buffer chunk size (in bytes) defined by user
with open(r'./input_6', "r") as f:
    carr = [*f.read(carr_len)]
    car_scan(carr)
    cnt = carr_len
    if brk_flg is False:
        while brk_flg is False:
            cnt += 1
            carr.append(f.read(1))
            carr.pop(0)
            car_scan(carr)

# Print result
print("The start-of-packet is at character %s" % cnt)

# Timestamp is obsolete as it includes user time
# But included nonetheless
print("--- %s seconds ---" % (time.time()-st))
