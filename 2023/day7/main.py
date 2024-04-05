import dataclasses
from collections import Counter


def card_strengths(card_counts):
    return sorted(card_counts.values(), reverse=True)


def card_strengths_solution2(card_counts):
    if 'J' in card_counts:
        j_count = card_counts['J']
        if j_count != 5:
            card_counts.pop('J', None)
            most_cards = max(card_counts, key=card_counts.get)
            card_counts[most_cards] += j_count
    return sorted(card_counts.values(), reverse=True)


@dataclasses.dataclass(frozen=True)
class CamelCards:
    cards: str
    counts: list
    counts_with_joker: list
    bid: int

    @classmethod
    def from_line(cls, line):
        cards, bid = line.split()
        counts = card_strengths(Counter(cards))
        counts_with_joker = card_strengths_solution2(Counter(cards))
        return cls(
            cards=cards,
            counts=counts,
            counts_with_joker=counts_with_joker,
            bid=int(bid)
        )


def read_file():
    cards = []
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            cards.append(CamelCards.from_line(line))
    return cards


def solution():
    cards = read_file()
    order = {key: i for i, key in enumerate(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6',  '5', '4', '3', '2'])}

    for x in [4, 3, 2, 1, 0]:
        cards = sorted(cards, key=lambda card: order[card.cards[x]], reverse=True)

    sorted_cards = sorted(cards, key=lambda card: card.counts)

    counter = 1
    winnings = 0
    for x in sorted_cards:
        winnings += (x.bid * counter)
        counter += 1
    print(f' solution 1: {winnings}')


def solution_2():
    cards = read_file()
    order = {key: i for i, key in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])}

    for x in [4, 3, 2, 1, 0]:
        cards = sorted(cards, key=lambda card: order[card.cards[x]], reverse=True)

    sorted_cards = sorted(cards, key=lambda card: card.counts_with_joker)

    counter = 1
    winnings = 0
    for x in sorted_cards:
        winnings += (x.bid * counter)
        counter += 1
    print(f' solution 2: {winnings}')


if __name__ == '__main__':
    solution()
    solution_2()
