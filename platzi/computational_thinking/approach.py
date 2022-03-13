def main() -> None:
    goal = int(input("Enter an integer: "))
    epsilon = 0.0001
    step = epsilon**2
    answer = 0.0

    while abs(answer**2 - goal) >= epsilon and answer <= goal:
        print(abs(answer**2 - goal), answer)
        answer += step

    if abs(answer**2 - goal) >= epsilon:
        print(f"Square root not found of {goal}")
    else:
        print(f"The square root of {goal} is {answer}")


if __name__ == "__main__":
    main()
