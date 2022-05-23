def divisors(num: int) -> list[int]:
    try:
        if num < 0:
            raise Exception('The number must be positive')
    except Exception as e:
        print(e)
        return False
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main() -> None:
    try:
        num = int(input('Enter a number: '))
        print(divisors(num))
        print('My program finished')
    except ValueError:
        print('You must enter a number')


if __name__ == '__main__':
    main()
