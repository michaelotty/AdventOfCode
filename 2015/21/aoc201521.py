"""Advent of code Day 21 part 1 and 2."""

from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import combinations, product
from operator import itemgetter


@dataclass(kw_only=True, frozen=True)
class Item:
    """Item from the shop."""

    name: str
    cost: int
    damage: int
    armor: int


class Character:
    """Character attributes."""

    def __init__(self, damage: int = 0, armor: int = 0, hit_points: int = 100) -> None:
        """Define variables."""
        self.hit_points: int = hit_points
        self.damage: int = damage
        self.armor: int = armor
        self.money_spent: int = 0
        self.inventory: list[Item] = []

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"HP: {self.hit_points}\nDA: {self.damage}\nAR: {self.armor}"

    @property
    def alive(self) -> bool:
        """If the character is alive or not, i.e dead if hp <= 0."""
        return self.hit_points > 0

    def attack(self, opponent: Character) -> None:
        """Get attacked by opponent."""
        opponent.hit_points -= max(self.damage - opponent.armor, 1)

    def add_item(self, item: Item) -> None:
        """Add an item to the inventory and applies the buff."""
        self.money_spent += item.cost
        self.damage += item.damage
        self.armor += item.armor
        self.inventory.append(item)


def extract_shop_data(file_name: str) -> dict:
    """Open the shop file and extracts data into dict format."""
    with open(file_name, encoding="utf-8") as file:
        shops_file = file.read().split("\n\n")

    shops = {}
    for shop in shops_file:
        name, items_str = shop.split(":")
        titles = tuple(title.lower() for title in re.findall(r"\w+", items_str)[:3])
        items = re.findall(r"\n(.+) +(\d+) +(\d+) +(\d+)", items_str)
        names = tuple(x[0].strip().lower().replace(" +", "_") for x in items)
        shops[name.lower()] = [
            Item(name=item_name, **dict(zip(titles, map(int, value[1:]))))
            for item_name, value in zip(names, items)
        ]

    return shops


def does_player_win(player: Character, enemy: Character) -> bool:
    """Play out the game and finds if the player wins."""
    while player.alive:
        player.attack(enemy)
        if not enemy.alive:
            return True
        enemy.attack(player)
    return False


def main() -> None:
    """Program starts here."""
    shop = extract_shop_data("shop.txt")
    shop["armor"].append(Item(name="no_armor", cost=0, damage=0, armor=0))

    winning_combos = []
    losing_combos = []

    with open("2015/21/input.txt", encoding="utf-8") as file:
        enemy_file = {
            name.lower().replace(" ", "_"): int(value)
            for name, value in re.findall(r"(.*): (\d+)", file.read())
        }

    for weapon, armor in product(shop["weapons"], shop["armor"]):
        for i in range(3):
            for rings in combinations(shop["rings"], i):
                enemy = Character(**enemy_file)
                player = Character()
                items = (weapon, armor, *rings)
                for item in items:
                    player.add_item(item)
                if does_player_win(player, enemy):
                    winning_combos.append((player.money_spent, player.inventory))
                else:
                    losing_combos.append((player.money_spent, player.inventory))
    print(sorted(winning_combos, key=itemgetter(0))[0][0])
    print(sorted(losing_combos, key=itemgetter(0))[-1][0])


if __name__ == "__main__":
    main()
