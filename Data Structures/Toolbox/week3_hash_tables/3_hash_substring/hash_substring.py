# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return find_patterns(text, pattern)

def poly_hash(input_str, x, p):
    hash_val = 0
    for s in reversed(input_str):
        hash_val = (hash_val * x + ord(s)) % p

    return hash_val

def precompute_hashes(text, pattern_len, x, p):
    num_substrings = len(text) - pattern_len + 1
    H = [0] * num_substrings
    H[num_substrings-1] = poly_hash(text[num_substrings-1:], x, p)
    y = 1
    for i in range(pattern_len):
        y = (y*x) % p
    for i in range(num_substrings - 2, -1, -1):
        H[i] = (x*H[i+1] + ord(text[i]) - y * ord(text[i+pattern_len]) + p) % p

    return H

def find_patterns(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    if pattern_len > text_len:
        return []

    p = 1000000007
    x = random.randint(1, p-1)
    positions = []
    pattern_hash = poly_hash(pattern, x, p)
    H = precompute_hashes(text, pattern_len, x, p)

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == H[i]:
            if text[i:i+pattern_len] == pattern:
                positions.append(i)

    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

