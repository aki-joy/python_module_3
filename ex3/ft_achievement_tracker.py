import random


ACHIEVEMENTS = [
    "First Steps", "Rookie Adventurer", "Treasure Hunter",
    "Master Explorer", "Hidden Path Finder", "Boss Slayer",
    "Dragon Vanquisher", "Monster Hunter", "Dungeon Conqueror",
    "World Savior", "Speed Runner", "Untouchable", "Unstoppable",
    "Perfect Victory", "Last Stand", "Survivor", "Sharp Mind",
    "Strategist", "Puzzle Master", "Silent Assassin",
    "Crafting Genius", "Master Blacksmith", "Potion Expert",
    "Collector Supreme", "Rare Item Finder", "Legendary Collector",
    "Gold Hoarder", "Millionaire Hero", "Arena Champion",
    "Battle Veteran", "Combo Master", "Critical Striker",
    "Flawless Defender", "Team Leader", "Loyal Companion",
    "Quest Specialist", "Side Quest Hero", "Map Completionist",
    "Secret Unlocker", "Legend Awakened"
    ]


def gen_player_achievements(achievements: list[str]) -> None:
    Alice = set()
    Bob = set()
    Charlie = set()
    Dylan = set()

    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = [Alice, Bob, Charlie, Dylan]

    for i in range(len(players)):

        players[i] = set(random.sample(achievements, random.randint(7, 15)))
        print(f"Player {names[i]}: {players[i]}\n")

    all_distinct = Alice.union(Bob, Charlie, Dylan)
    print(f"All distinct achievements: {all_distinct}\n")

    common = Alice.intersection(Bob, Charlie, Dylan)
    print(f"Common achievements: {common}\n")

    for i in range(len(players)):

        others = []

        for j in range(len(players)):

            if j != i:
                others.append(players[j])
                only = players[i].difference(*others)

        print(f"Only {names[i]} has: {only}\n")

    for i in range(len(players)):

        missing = set(ACHIEVEMENTS).difference(players[i])
        print(f"{names[i]} is missing: {missing}\n")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    gen_player_achievements(ACHIEVEMENTS)
