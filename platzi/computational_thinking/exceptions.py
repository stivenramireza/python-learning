from typing import List


def divide_elements(my_list: List[int], divisor: int) -> List[int]:
    try:
        return [i / divisor for i in my_list]
    except ZeroDivisionError as e:
        print(e)
        return my_list
    

def main() -> None:
    my_list = list(range(10))
    divisor = 0

    print(divide_elements(my_list, divisor))


if __name__ == "__main__":
    main()
