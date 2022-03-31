import time


class FiboIter:

    def __init__(self, max: int = 0) -> None:
        assert max >= 0, "max must be a positive number"
        self.max = max

    def __iter__(self) -> object:
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self) -> int:
        match self.counter:
            case 0:
                self.counter +=1
                return self.n1
            case 1:
                self.counter +=1
                return self.n2
            case _:
                self.aux = self.n1 + self.n2
                if self.max in [0, 1] or self.aux > self.max:
                    raise StopIteration
                self.n1, self.n2 = self.n2, self.aux
                self.counter +=1
                return self.aux



def main():
    fibonacci = FiboIter(1000)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == "__main__":
    main()
