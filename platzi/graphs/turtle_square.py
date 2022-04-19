import turtle


def main() -> None:
    window = turtle.Screen()
    t = turtle.Turtle()

    for i in range(0, 4):
        t.forward(100)
        t.right(90)

    window.mainloop()


if __name__ == "__main__":
    main()
