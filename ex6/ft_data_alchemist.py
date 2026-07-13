import random


PLAYERS = [
    "Alice", "bob", "Charlie", "dylan",
    "Emma", "Gregory", "john", "kevin", "Liam"
]


def data_alchemist(players: list[str]) -> None:
    all_capitalized: list[str] = []
    capitalized_only: list[str] = []
    name_with_score: dict[str, int] = {}

    all_capitalized = [player.capitalize() for player in players]

    capitalized_only = [
        player
        for player in players
        if player == player.capitalize()
    ]

    name_with_score = {
        player: random.randint(0, 1000) for player in all_capitalized
    }

    print(f"Initial list of players: {players}\n")
    print(f"New list with all names capitalized: {all_capitalized}\n")
    print(f"New list of capitalized names only: {capitalized_only}\n")
    print(f"Score dict: {name_with_score}\n")

    scores = name_with_score.values()
    average = sum(scores) / len(scores)

    print(f"Score average is {round(average, 2)}\n")

    higher: dict[str, int] = {}
    higher = {
        player: score
        for player, score in name_with_score.items()
        if score > average
    }
    print(f"High scores: {higher}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    data_alchemist(PLAYERS)
