import sys


def validate(arg: str) -> int:
    parts = arg.split(":")

    if len(parts) < 2:
        print(f"Error --invalid parameter {parts[0]}")
        return -1

    try:
        quantity = int(parts[1])
    except Exception as e:
        print(f"Quantity error for {parts[0]}: {e}")
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
            print(f"Redundant item {item} -discarding")
            continue

        inventory[item] = quantity

    return inventory


def update_inventory(inventory: dict[str, int], item_added: str) -> None:
    parts = item_added.split(":")
    quantity = validate(item_added)

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
    print(f"Total quantity of the {len(values)} items {total_quantity}")

    for key in keys:
        ratio = inventory[key] / total_quantity
        print(f"Item {key} represents {round(ratio * 100, 1)}%")
    
    print(f"Item most abundant: potion with quantity {max(values)}")
    print(f"Item least abundant: potion with quantity {min(values)}")

    update_inventory(inventory, "magic_potion:1")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_system(sys.argv[1: ])
