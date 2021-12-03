with open('3.txt') as f:
    words = [line.strip() for line in f.readlines()]

word_len = len(words[0])
gamma_rate = []
epsilon_rate = []

for i in range(word_len):
    num_zero = sum(word[i] == '0' for word in words)
    if num_zero > len(words) // 2:
        gamma_rate.append('0')
        epsilon_rate.append('1')
    else:
        gamma_rate.append('1')
        epsilon_rate.append('0')

def to_int(bin_arr):
   return int(''.join(bin_arr), 2)

print(to_int(gamma_rate) * to_int(epsilon_rate))


def find_oxy_rating(words):
    words = set(words)
    idx = 0
    while len(words) > 1:
        has_zero = set()
        has_one = set()
        for word in words:
            if word[idx] == '0':
                has_zero.add(word)
            else:
                has_one.add(word)
            if len(has_one) >= len(has_zero):
                words = has_one
            elif len(has_one) < len(has_zero):
                words = has_zero
            else:
                words = has_one
        idx += 1
    return list(words)[0]

def find_co2_rating(words):
    words = set(words)
    idx = 0
    while len(words) > 1:
        has_zero = set()
        has_one = set()
        for word in words:
            if word[idx] == '0':
                has_zero.add(word)
            else:
                has_one.add(word)
            if len(has_one) >= len(has_zero):
                words = has_zero
            elif len(has_one) < len(has_zero):
                words = has_one
        idx += 1
    return list(words)[0]

def copy(arr):
    return [x for x in arr]

oxy_rating = to_int(find_oxy_rating(copy(words)))
co2_rating = to_int(find_co2_rating(copy(words)))

# print(oxy_rating, co2_rating)

print(oxy_rating * co2_rating)
