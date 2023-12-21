"""Advent of code day 7."""

from __future__ import annotations

from collections import Counter
from enum import Enum, auto


class HandType(Enum):
    """Hand type enum."""

    PART_1 = auto()
    PART_2 = auto()


class CamelCards:
    """Game of camel cards."""

    def __init__(self, rounds: list[tuple[str, ...]], choice: HandType) -> None:
        """Create a game of camel cards."""
        self.hands: list[Hand1 | Hand2] = []
        hand_class: dict[HandType, type[Hand1] | type[Hand2]] = {
            HandType.PART_1: Hand1,
            HandType.PART_2: Hand2,
        }

        for hand, bid_str in rounds:
            self.hands.append(hand_class[choice](hand, int(bid_str)))

        self.hands.sort()

    def __repr__(self) -> str:
        """Return a string representation."""
        return "\t".join(hand.hand for hand in self.hands)

    @property
    def total_winnings(self) -> int:
        """Calculate the total winnings."""
        return sum(hand.bid * rank for rank, hand in enumerate(self.hands, start=1))


class Hand1:
    """Hand for part 1 in camel cards."""

    def __init__(self, hand_str: str, bid: int) -> None:
        """Create a camel cards hand."""
        self.hand = hand_str
        self.bid = bid

        self.strength_order = "23456789TJQKA"

        self.type, self.hand_ranks = self._find_type(hand_str)

    def _find_type(  # pylint: disable=too-many-return-statements
        self, hand_str: str
    ) -> tuple[str, list[str]]:
        """Find hand type."""
        hand_analysis: list[tuple[str, int]] = Counter(hand_str).most_common()
        if hand_analysis[0][1] == 5:
            return "five_of_a_kind", [hand_analysis[0][0]]

        if hand_analysis[0][1] == 4:
            return "four_of_a_kind", [hand_analysis[0][0]]

        if hand_analysis[0][1] == 3 and hand_analysis[1][1] == 2:
            return "full_house", [hand_analysis[0][0], hand_analysis[1][0]]

        if hand_analysis[0][1] == 3:
            return "three_of_a_kind", [hand_analysis[0][0]]

        if hand_analysis[0][1] == 2 and hand_analysis[1][1] == 2:
            return "two_pair", [hand_analysis[0][0], hand_analysis[1][0]]

        if hand_analysis[0][1] == 2:
            return "one_pair", [hand_analysis[0][0]]

        for card_type in self.strength_order[::-1]:
            if card_type in hand_str:
                return "high_card", [card_type]

        raise RuntimeError("No hand found")

    def __lt__(self, other: Hand1):
        """Compare one hand with another."""
        type_ranking = {
            "five_of_a_kind": 7,
            "four_of_a_kind": 6,
            "full_house": 5,
            "three_of_a_kind": 4,
            "two_pair": 3,
            "one_pair": 2,
            "high_card": 1,
        }
        if self.type != other.type:
            return type_ranking[self.type] < type_ranking[other.type]

        card_ranking = {char: i for i, char in enumerate(self.strength_order)}

        for left, right in zip(self.hand, other.hand):
            if left == right:
                continue
            return card_ranking[left] < card_ranking[right]

        raise RuntimeError("Not a valid hand")

    def __repr__(self) -> str:
        """Return a string representation."""
        return f'Hand("{self.hand}",{self.bid})'


class Hand2:
    """Hand for part 2 in camel cards."""

    def __init__(self, hand_str: str, bid: int) -> None:
        """Create a camel cards hand."""
        self.hand = hand_str
        self.bid = bid

        self.strength_order = "J23456789TQKA"

        self.type, self.hand_ranks = self._find_type(hand_str)

    def _find_type(  # pylint: disable=too-many-return-statements,too-many-branches
        self, hand_str: str
    ) -> tuple[str, list[str]]:
        """Find hand type."""
        hand_analysis: list[tuple[str, int]] = Counter(hand_str).most_common()
        hand_analysis_dict = dict(hand_analysis)

        if "J" in hand_analysis_dict:
            joker_count = hand_analysis_dict["J"]

            do_remove_jokers = True

            if hand_analysis[0][0] != "J":
                hand_analysis[0] = (
                    hand_analysis[0][0],
                    hand_analysis[0][1] + joker_count,
                )
            elif len(hand_analysis) > 1:
                hand_analysis[1] = (
                    hand_analysis[1][0],
                    hand_analysis[1][1] + joker_count,
                )
            else:
                do_remove_jokers = False

            if do_remove_jokers:
                hand_analysis.remove(("J", joker_count))

        if hand_analysis[0][1] == 5:
            return "five_of_a_kind", [hand_analysis[0][0]]

        if hand_analysis[0][1] == 4:
            return "four_of_a_kind", [hand_analysis[0][0]]

        if hand_analysis[0][1] == 3 and hand_analysis[1][1] == 2:
            return "full_house", [hand_analysis[0][0], hand_analysis[1][0]]

        if hand_analysis[0][1] == 3:
            return "three_of_a_kind", [hand_analysis[0][0]]

        if hand_analysis[0][1] == 2 and hand_analysis[1][1] == 2:
            return "two_pair", [hand_analysis[0][0], hand_analysis[1][0]]

        if hand_analysis[0][1] == 2:
            return "one_pair", [hand_analysis[0][0]]

        for card_type in self.strength_order[::-1]:
            if card_type in hand_str:
                return "high_card", [card_type]

        raise RuntimeError("No hand found")

    def __lt__(self, other: Hand1):
        """Compare one hand with another."""
        type_ranking = {
            "five_of_a_kind": 7,
            "four_of_a_kind": 6,
            "full_house": 5,
            "three_of_a_kind": 4,
            "two_pair": 3,
            "one_pair": 2,
            "high_card": 1,
        }
        if self.type != other.type:
            return type_ranking[self.type] < type_ranking[other.type]

        card_ranking = {char: i for i, char in enumerate(self.strength_order)}

        for left, right in zip(self.hand, other.hand):
            if left == right:
                continue
            return card_ranking[left] < card_ranking[right]

        raise RuntimeError("Not a valid hand")

    def __repr__(self) -> str:
        """Return a string representation."""
        return f'Hand("{self.hand}",{self.bid})'


def main() -> None:
    """Program starts here."""
    with open("2023/07/test.txt", encoding="utf-8") as file:
        data = [tuple(line.split()) for line in file.read().splitlines()]

    print("Part 1:", part_1(CamelCards(data, HandType.PART_1)))
    print("Part 2:", part_2(CamelCards(data, HandType.PART_2)))


def part_1(camel_cards: CamelCards) -> int:
    """Solve part 1."""
    return camel_cards.total_winnings


def part_2(camel_cards: CamelCards) -> int:
    """Solve part 2."""
    return camel_cards.total_winnings


if __name__ == "__main__":
    main()
