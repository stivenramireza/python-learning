from typing import Callable

PASSWORD = '12345'


def password_required(func: Callable) -> Callable:
    def wrapper() -> Callable:
        password = input('What is your password? ')
        if password == PASSWORD:
            return func()
        else:
            print('The password is invalid')

    return wrapper


@password_required
def needs_password() -> None:
    print('The password is correct')


def upper(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@upper
def say_my_name(name: str) -> str:
    return 'Hello, {}'.format(name)


def main() -> None:
    # needs_password()
    print(say_my_name('Stiven'))


if __name__ == '__main__':
    main()
