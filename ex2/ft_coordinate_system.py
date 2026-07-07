import math


def get_player_pos() -> tuple[float, float, float]:

    while True:
        try:
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
            if len(coordinates) < 2:
                raise Exception("Invalid syntax")
            x = float(coordinates[0])
            y = float(coordinates[1])
            z = float(coordinates[2])
            return (x, y, z)
        except Exception as e:
            print(f"{e}")


def calculate(
        pos1: tuple[float, float, float],
        pos2: tuple[float, float, float]
        ) -> float:

    distance = math.sqrt(
        (pos1[0] - pos2[0]) ** 2
        + (pos1[1] - pos2[1]) ** 2
        + (pos1[2] - pos2[2]) ** 2
        )
    distance = round(distance, 4)
    return distance


def show(number: str, pos: tuple[float, float, float]) -> None:

    print(f"Get a {number} set of coordinates")
    print(f"Got a {number} tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


def coordinate_system() -> None:

    origin = (0.0, 0.0, 0.0)

    first_pos = get_player_pos()
    show("first", first_pos)

    distance_to_center = calculate(origin, first_pos)
    print(f"Distance to center: {distance_to_center}\n")

    second_pos = get_player_pos()
    show("second", second_pos)

    distance_two_points = calculate(first_pos, second_pos)
    print(f"Distance between the 2 sets of coordinates: {distance_two_points}")


if __name__ == "__main__":
    print("=== Game Coordinates System ===")
    coordinate_system()
