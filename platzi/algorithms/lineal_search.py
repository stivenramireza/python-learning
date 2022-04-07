import random


def linear_search(elements: list[int], goal: int) -> bool:
    match = False

    for element in elements:  # O(n)
        if element == goal:
            match = True
            break

    return match


def main() -> None:
    n = int(input("What's the list lenght? "))
    goal = int(input("What number do you want to find? "))

    elements = [random.randint(0, 100) for i in range(n)]

    is_found = linear_search(elements, goal)

    print(elements)
    print(f"The element {goal} {'is' if is_found else 'is not'} in the list")


if __name__ == "__main__":
    main()
