import math


def get_player_pos() -> tuple[float, float, float]:

    while True:
        try:
            raw_coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            x_raw, y_raw, z_raw = raw_coordinates.split(",")
        except Exception:
            print("Invalid syntax")
            continue

        try:
            x = float(x_raw)
            y = float(y_raw)
            z = float(z_raw)
            return (x, y, z)
        except Exception as e:
            invalid_param = x_raw
            try:
                float(x_raw)
                invalid_param = y_raw
                float(y_raw)
                invalid_param = z_raw
            except Exception:
                pass
            print(f"Error on parameter '{invalid_param}': {e}")


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


def coordinate_system() -> None:

    origin = (0.0, 0.0, 0.0)

    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")

    distance_to_center = calculate(origin, first_pos)
    print(f"Distance to center: {distance_to_center}\n")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance_two_points = calculate(first_pos, second_pos)
    print(f"Distance between the 2 sets of coordinates: {distance_two_points}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    coordinate_system()
