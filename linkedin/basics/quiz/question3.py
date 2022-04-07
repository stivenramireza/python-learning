class Simple:
    def add(self, x: int, y: int) -> int:
        return x + y


class Advanced(Simple):
    def inverse(self, x, y):
        return 1 / Simple.add(self, x, y)


a = Advanced()
print(a.inverse(2, 3))
