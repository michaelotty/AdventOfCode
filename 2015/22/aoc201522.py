"""Advent of code Day 22"""

from __future__ import annotations

# import re
from operator import itemgetter

# from spells import Effect, Spell


class Character:
    """Character attributes"""

    def __init__(self, damage: int = 0, armor: int = 0, hit_points: int = 100) -> None:
        """Defines variables"""
        self.hit_points: int = hit_points
        self.damage: int = damage
        self.armor: int = armor
        self.money_spent: int = 0

    def __str__(self) -> str:
        return f"HP: {self.hit_points}\nDA: {self.damage}\nAR: {self.armor}"

    @property
    def alive(self) -> bool:
        """If the character is alive or not, i.e dead if hp <= 0"""
        return self.hit_points > 0

    def attack(self, opponent: Character) -> None:
        """The opponent attacks the self"""
        opponent.hit_points -= max(self.damage - opponent.armor, 1)


def does_player_win(player: Character, enemy: Character) -> bool:
    """Plays out the game and finds if the player wins"""
    while player.alive:
        player.attack(enemy)
        if not enemy.alive:
            return True
        enemy.attack(player)
    return False


def main() -> None:
    """Main function"""
    winning_combos = []
    losing_combos = []

    # with open("2015/22/input.txt", encoding="utf-8") as file:
    #     enemy_file = {
    #         name.lower().replace(" ", "_"): int(value)
    #         for name, value in re.findall(r"(.*): (\d+)", file.read())
    #     }

    # for weapon, armor in (0, 0):
    #     for i in range(3):
    #         enemy = Character(**enemy_file)
    #         player = Character()
    #         if does_player_win(player, enemy):
    #             winning_combos.append((player.money_spent, player.inventory))
    #         else:
    #             losing_combos.append((player.money_spent, player.inventory))
    print(sorted(winning_combos, key=itemgetter(0))[0][0])
    print(sorted(losing_combos, key=itemgetter(0))[-1][0])


if __name__ == "__main__":
    main()
