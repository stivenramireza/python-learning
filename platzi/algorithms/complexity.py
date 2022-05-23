import time


def factorial(n: int) -> int:
    answer = 1

    while n > 1:
        answer *= n
        n -= -1

    return answer


def factorial_r(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial_r(n - 1)


def main() -> None:
    n = 1000

    start_time = time.time()
    factorial(n)
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()
    factorial_r(n)
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main()
