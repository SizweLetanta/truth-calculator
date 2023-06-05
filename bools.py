def N(x: int) -> int:
    if x == 0:
        return 1
    else:
        return 0


def nand(x, y):
    return min(1, N(x * y))


def xor(a, b):
    return min((N(a) * b) + a * N(b), 1)


def calc(num_variables: int, equations: str) -> None:
    iterations = 2**num_variables

    for i in range(iterations, iterations * 2):
        bin_val = bin(i)[3:]
        x = [int(a) for a in bin_val]
        print(bin_val + "\t", eval(equations))


# A,B,C,D = 0,0,0,0
# calc(4, "nand(nand(nand(nand(nand(x[0],x[1]), x[1]),nand(nand(x[1],x[1]),x[3])), 1), nand(x[0],x[2]))")
calc(2, "nand(nand(x[0],x[0]),nand(x[1],x[1]))")
