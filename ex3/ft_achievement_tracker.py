import random


ACHIEVEMENTS = [
    "First Steps", "Rookie Adventurer", "Treasure Hunter",
    "Master Explorer", "Hidden Path Finder", "Boss Slayer",
    "Dragon Vanquisher", "Monster Hunter", "Dungeon Conqueror",
    "World Savior", "Speed Runner", "Untouchable", "Unstoppable",
    "Perfect Victory", "Last Stand", "Survivor", "Sharp Mind",
    "Strategist", "Puzzle Master", "Silent Assassin"
    ]


def gen_player_achievements(achievements: list[str]) -> set[str]:

    amount = random.randint(7, 15)
    return set(random.sample(achievements, amount))


def achievement_tracker() -> None:

    alice = gen_player_achievements(ACHIEVEMENTS)
    bob = gen_player_achievements(ACHIEVEMENTS)
    charlie = gen_player_achievements(ACHIEVEMENTS)
    dylan = gen_player_achievements(ACHIEVEMENTS)

    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}\n")

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}\n")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}\n")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}\n")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")

    all_achievements = set(ACHIEVEMENTS)
    print(f"Alice is missing: {all_achievements.difference(alice)}\n")
    print(f"Bob is missing: {all_achievements.difference(bob)}\n")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}\n")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}\n")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achievement_tracker()
