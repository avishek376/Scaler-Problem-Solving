import sys

sys.setrecursionlimit(10 ** 6)


def reverse(A, s, e):
    if e <= s:
        return A[s]
    print(A[e], end="")
    return reverse(A, s, e - 1)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = input()
    l = len(A)
    s = 0
    e = l - 1
    print(reverse(A, s, e))

    return 0


if __name__ == '__main__':
    main()

