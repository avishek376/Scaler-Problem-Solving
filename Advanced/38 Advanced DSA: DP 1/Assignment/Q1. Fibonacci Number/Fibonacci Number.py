def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    dp = [-1 for i in range(A + 1)]

    def fib(num):
        if num == 0 or num == 1:
            return num
        if dp[num] != -1:
            return dp[num]
        a = fib(num - 1)
        b = fib(num - 2)
        dp[num] = a + b
        return a + b

    print(fib(A))

    return 0


if __name__ == '__main__':
    main()