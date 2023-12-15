"""Advent of code day 7."""

from __future__ import annotations

from collections import Counter

STRENGTH_ORDER = "23456789TJQKA"


class CamelCards:
    """Game of camel cards."""

    def __init__(self, rounds: list[tuple[str, ...]]) -> None:
        """Create a game of camel cards."""
        self.hands: list[Hand] = []

        for hand, bid_str in rounds:
            self.hands.append(Hand(hand, int(bid_str)))

        self.hands.sort()

    def __repr__(self) -> str:
        """Return a string representation."""
        return "\t".join(hand.hand for hand in self.hands)

    @property
    def total_winnings(self) -> int:
        """Calculate the total winnings."""
        return sum(hand.bid * rank for rank, hand in enumerate(self.hands, start=1))


class Hand:
    """Hand in camel cards."""

    def __init__(self, hand_str: str, bid: int) -> None:
        """Create a camel cards hand."""
        self.hand = hand_str
        self.bid = bid

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

        for card_type in STRENGTH_ORDER[::-1]:
            if card_type in hand_str:
                return "high_card", [card_type]

        raise RuntimeError("No hand found")

    def __lt__(self, other: Hand):
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

        card_ranking = {char: i for i, char in enumerate(STRENGTH_ORDER)}

        # A Full house or Two pair
        if len(self.hand_ranks) == 2:
            if self.type == "full_house":
                return (
                    card_ranking[self.hand_ranks[0]] < card_ranking[other.hand_ranks[0]]
                )

            self_best_card_strength = max(
                card_ranking[self.hand_ranks[0]], card_ranking[self.hand_ranks[1]]
            )
            other_best_card_strength = max(
                card_ranking[other.hand_ranks[0]], card_ranking[other.hand_ranks[1]]
            )
            return self_best_card_strength < other_best_card_strength

        # A Five_of_a_kind, Four_of_a_kind, Three_of_a_kind, One pair, High card
        if len(self.hand_ranks) == 1:
            return card_ranking[self.hand_ranks[0]] < card_ranking[other.hand_ranks[0]]

        raise RuntimeError("Not a valid hand")

    def __repr__(self) -> str:
        """Return a string representation."""
        return f'Hand("{self.hand}",{self.bid})'


def main() -> None:
    """Program starts here."""
    with open("2023/07/input.txt", encoding="utf-8") as file:
        data = [tuple(line.split()) for line in file.read().splitlines()]

    print("Part 1:", part_1(CamelCards(data)))
    print("Part 2:", part_2())


def part_1(camel_cards: CamelCards) -> int:
    """Solve part 1."""
    print(camel_cards)
    return camel_cards.total_winnings  # 250581817 too low


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
