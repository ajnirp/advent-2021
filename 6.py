from collections import Counter

with open('6.txt') as f:
    state = list(map(int, f.read().strip().split(',')))

# key insight: ignore array ordering. Just maintain a counter for each timer level

def init():
    counts = Counter()
    for num in state:
        counts[num] += 1
    return counts

def update(counts):
    new_counts = Counter()
    for i in range(1,9):
        new_counts[i-1] += counts[i]
    new_counts[6] += counts[0]
    new_counts[8] += counts[0]
    return new_counts

counts = init()

for _ in range(80):
    counts = update(counts)

print(sum(counts.values()))

for _ in range(256-80):
    counts = update(counts)

print(sum(counts.values()))
