def main() -> None:
    goal = int(input("Enter a number: "))
    epsilon = 0.001
    min_value = 0.0
    max_value = max(1.0, goal)
    answer = (max_value + min_value) / 2

    while abs(answer**2 - goal) >= epsilon:
        print(f"min_value={min_value}, max_value={max_value}, answer={answer}")
        if answer**2 < goal:
            min_value = answer
        else:
            max_value = answer
        
        answer = (max_value + min_value) / 2

    print(f"The square root of {goal} is {answer}")


if __name__ == "__main__":
    main()
