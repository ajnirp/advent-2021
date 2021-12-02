with open('1.txt') as f:
    data = [int(line.strip()) for line in f.readlines()]

# number of window sums that increase from one index to the next
def num_increasing_window_sums(window_len):
    return sum(data[i] > data[i-window_len] for i in range(window_len, len(data))) 

print(num_increasing_window_sums(1))
print(num_increasing_window_sums(3))
