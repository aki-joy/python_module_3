import typing
import random


PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]

ACTIONS = [
        "Attack", "Defend", "Heal", "Cast", "Spell", "Use", "Item", "Dodge"
    ]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    while True:

        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield name, action


def make_ten_event() -> list[tuple[str, str]]:

    events: list[tuple[str, str]] = []
    event_generator = gen_event()

    for _ in range(10):
        events.append(next(event_generator))

    print(f"Built list of 10 events: {events}")

    return events


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:

    while len(events) > 0:

        removed = events.pop(random.randint(0, len(events) - 1))
        yield removed


def data_stream() -> None:

    event_generator = gen_event()

    for i in range(1000):

        log = next(event_generator)
        print(f"Event {i}: Player {log[0]} did action {log[1]}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    data_stream()
    print("")
    events = make_ten_event()
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
