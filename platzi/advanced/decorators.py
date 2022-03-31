from datetime import datetime


def execution_time(func: object) -> object:
    def wrapper(*args, **kwargs) -> object:
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"It tooked {time_elapsed.total_seconds()} seconds")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b


@execution_time
def greeting(name: str = "Cesar"):
    print(f"Hello {name}")


def main() -> None:
    random_func()
    sum(5, 5)
    greeting("Stiven")


if __name__ == "__main__":
    main()
