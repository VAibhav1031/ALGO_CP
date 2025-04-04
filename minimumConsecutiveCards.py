# This  is just the  condition where we can  say the things where we are like
# consecutive card
#

from collections import defaultdict


def minconsecutiveCard(cards: list[int]):
    k = defaultdict(int)
    min_ = float("inf")

    for i, num in enumerate(cards):
        if num in k:
            min_ = min(min_, i - k[num] + 1)

        k[num] = i

    return min_ if min_ != float("inf") else -1


print(minconsecutiveCard([4, 0, 5, 2, 3, 6, 7, 2]))
