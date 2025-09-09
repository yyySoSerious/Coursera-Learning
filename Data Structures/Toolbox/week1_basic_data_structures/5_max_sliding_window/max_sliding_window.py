# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.__max_stack or a >=self.__max_stack[-1]:
            self.__max_stack.append(a)
        else:
            self.__max_stack.append(self.__max_stack[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__max_stack.pop()
        return self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__max_stack[-1]

    def empty(self):
        return not self.__stack

class CustomQueue():
    def __init__(self):
        self.stack1 = StackWithMax()
        self.stack2 = StackWithMax()

    def enqueue(self, a):
        self.stack1.Push(a)

    def dequeue(self):
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.Push(self.stack1.Pop())

        return self.stack2.Pop()

    def max(self):
        if not self.stack1.empty() and not self.stack2.empty():
            return max(self.stack1.Max(), self.stack2.Max())
        elif not self.stack1.empty():
            return self.stack1.Max()
        elif not self.stack2.empty():
            return self.stack2.Max()
        else:
            raise IndexError("Cannot get max from an empty queue")

    def empty(self):
        return not self.stack1 and not self.stack2

def max_sliding_window_stacks(sequence, m):
    stack = CustomQueue()
    maximums = []
    for i in range(len(sequence)):
        stack.enqueue(sequence[i])
        if i >= m-1:
            maximums.append(stack.max())
            stack.dequeue()

    return maximums

def max_sliding_window_deque(sequence, m):
    maximums = []
    seq_indices = deque()

    for i in range(len(sequence)):
        while seq_indices and sequence[seq_indices[-1]] <= sequence[i]:
            seq_indices.pop()

        seq_indices.append(i)
        if seq_indices[0] <= i -m:
            seq_indices.popleft()

        if i >= m-1:
            maximums.append(sequence[seq_indices[0]])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_deque(input_sequence, window_size))

