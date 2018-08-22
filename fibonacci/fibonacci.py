def generateFibonacci(length=10):
    n = int(length)

    if n < 0:
        return 0
    elif n < 2:
        return n

    seq = [1, 1]

    for i in range(2, n):
        seq.append(seq[i - 2] + seq[i - 1])

    return seq


def main():
    print(generateFibonacci())
    print(generateFibonacci(20))
    print(generateFibonacci(1))
    print(generateFibonacci(0))
    print(generateFibonacci(-999))


if __name__ == "__main__":
    main()
