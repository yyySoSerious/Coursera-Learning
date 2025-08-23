# python3

def compute_operations2(n):
    dp_table = [float("inf")] * (n+1)
    dp_table[1] = 0

    for integer in range(2, n+1):
        op_add_1 = dp_table[integer - 1]
        op_multiply_by_2 = dp_table[integer//2] if integer % 2 == 0 else float("inf")
        op_multiply_by_3 = dp_table[integer//3] if integer % 3 == 0 else float("inf")
        dp_table[integer] = 1 + min(op_add_1, op_multiply_by_2, op_multiply_by_3)

    sequence = [n]
    integer = n
    while integer > 1:
        target_prev_op = dp_table[integer] - 1
        op_add_1 = dp_table[integer - 1]
        op_multiply_by_2 = dp_table[integer // 2] if integer % 2 == 0 else float("inf")
        op_multiply_by_3 = dp_table[integer // 3] if integer % 3 == 0 else float("inf")

        if target_prev_op == op_multiply_by_3:
            integer = integer //3
        elif target_prev_op == op_multiply_by_2:
            integer = integer //2
        elif target_prev_op == op_add_1:
            integer -= 1
        else:
            raise(f'Error: Cannot create path at integer {integer}'
                  f'previous minimum number of operations should be {target_prev_op}')
        sequence.append(integer)

    sequence.reverse()
    return sequence


def compute_operations(n):
    dp_table = [[float("inf"), []]] * (n+1)
    dp_table[1] = [0, [1]]

    for integer in range(2, n+1):
        op_1 = integer - 1
        op_2 = integer  // 2
        op_3 = integer //3

        do_op2 = not(integer % 2)
        do_op3 = not(integer % 3)
        dp_table[integer] = [dp_table[op_1][0],
                             dp_table[op_1][1] + [integer]]
        if op_2 >=0 and do_op2 and dp_table[op_2][0] < dp_table[integer][0]:
            dp_table[integer] = [dp_table[op_2][0],
                             dp_table[op_2][1] + [integer]]
        if op_3 >=0 and do_op3 and dp_table[op_3][0] < dp_table[integer][0]:
            dp_table[integer] = [dp_table[op_3][0],
                             dp_table[op_3][1] + [integer]]
        dp_table[integer][0] += 1
    return dp_table[n][1]



if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
