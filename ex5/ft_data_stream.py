import typing
import random


PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]

ACTIONS = [
        "Attack", "Defend", "Heal", "Cast", "Spell", "Use", "Item", "Dodge",
        "Block", "Charge", "Escape", "Explore", "Search", "Steal", "Trade",
        "Craft", "Hunt", "Gather", "Rest", "Summon", "Talk", "Equip"
    ]
def gen_event() -> None:

    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        return name, action


def consume_events() -> None:


def 