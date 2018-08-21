def fibonacci(n=10):
    n = int(n)

    if n < 0:
        return 0
    elif n < 2:
        return n

    seq = [1, 1]

    for i in range(2, int(n)):
        seq.append(seq[i - 2] + seq[i - 1])

    return seq


print(fibonacci())
