import sys


def validate(arg: str) -> int:
    parts = arg.split(":")

    if len(parts) != 2:
        print(f"Error - invalid parameter '{arg}'")
        return -1

    try:
        quantity = int(parts[1])
    except Exception as e:
        print(f"Quantity error for '{parts[0]}': {e}")
        return -1

    return quantity


def make_dict(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:

        parts = arg.split(":")
        quantity = validate(arg)

        if quantity == -1:
            continue

        item = parts[0]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        inventory[item] = quantity

    return inventory


def update_inventory(
        inventory: dict[str, int],
        added_item: list[str]
        ) -> None:

    parts = added_item.split(":")
    quantity = validate(added_item)

    if quantity == -1:
        return

    item = parts[0]

    inventory.update({item: quantity})
    print(f"Updated inventory: {inventory}")


def inventory_system(args: list[str]) -> None:

    inventory = make_dict(args)
    keys = list(inventory.keys())
    values = list(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {keys}")
    total_quantity = sum(values)
    print(f"Total quantity of the {len(values)} items: {total_quantity}")

    if len(keys) < 1:
        update_inventory(inventory, ["magic_item:1"])
        return

    for key in keys:
        ratio = inventory[key] / total_quantity
        print(f"Item {key} represents {round(ratio * 100, 1)}%")

    most_item = keys[0]
    least_item = keys[0]

    for key in keys:
        if inventory[key] > inventory[most_item]:
            most_item = key
        if inventory[key] < inventory[least_item]:
            least_item = key

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )

    update_inventory(inventory, "magic_item:1")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_system(sys.argv[1:])
