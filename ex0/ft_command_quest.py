import sys


def show_arguments(args: list[str]) -> None:
    print(f"Progaram name: {sys.argv[0]}")
    counts = len(args)

    if counts < 2:
        print("No arguments privided!")

    else:
        print(f"Argument recieved: {counts - 1}")
        for i in range(1, counts):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total argument {counts}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    show_arguments(sys.argv)