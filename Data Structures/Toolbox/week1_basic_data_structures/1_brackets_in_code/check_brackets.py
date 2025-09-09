# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i+1))

        elif next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            prev, _ = opening_brackets_stack.pop()
            if not are_matching(prev, next):
                return i + 1

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[0][1]

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
