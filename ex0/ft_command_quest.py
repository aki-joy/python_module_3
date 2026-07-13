import sys


def show_arguments(args: list[str]) -> None:
    print(f"Program name: {sys.argv[0]}")
    counts = len(args)

    if counts < 2:
        print("No arguments provided!")

    else:
        print(f"Arguments received: {counts - 1}")
        i = 1
        while i < counts:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {counts}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    show_arguments(sys.argv)
