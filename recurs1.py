#
#
# import math
#
#
# def powerSum(X, N):
#     def backrack(remaining, start):
#         if remaining == 0:
#             return 1
#
#         if remaining < 0:
#             return 0
#
#         count = 0
#
#         for i in range(start, math.floor(X ** (1 / N)) + 1):
#             count += backrack(remaining - i**N, i + 1)
#
#         return count
#
#     return backrack(X, 1)
#
#
# print(powerSum(100, 3))
#
#


# CrossWord Puzzle SOlveer
# BAsically we will use the recursion , here but  recursion only doesnt help
# we will use backracking with it  which will help in  getting all valid paths if not  we will backtrack
# place to another
#

# we will be given  10*10 board or crossword area  , where +  will be preoccupied  , - will be place where you have to place the character
# How  you are gonna place ,  first thung to remember , words will be given  in this  way "london;Agra;jakarta" sep by ;
# you can  use the split to convert the thing to the list and do the things


# find  the  places  where we have to place
# horizontall and vertically


def placeChecker(crossword):
    horizontal = []
    vertical = []

    # horizontal
    for r in range(10):
        start_col, length = None, 0
        for c in range(10):
            if crossword[r][c] == "-":
                if start_col is None:
                    start_col = c

                length += 1

            else:
                if length >= 2:
                    horizontal.append(r, start_col, length)
                start_col, length = None, 0

        if length >= 2:
            horizontal.append(r, start_col, length)

    # vertical
    for c in range(10):
        start_row, length = None, 0

        for r in range(10):
            if crossword[r][c] == "-":
                if start_row is None:
                    start_row = r

                length += 1

            else:
                if length >= 2:
                    vertical.append(c, start_row, length)
                start_row, length = None, 0

        if length >= 2:
            vertical.append(c, start_row, length)

    return horizontal, vertical


def crossWordSolver(crossword, words, word_index, horizontal, vertical):
    if word_index == len(words):
        return True

    word = words[word_index]

    # horizontal
    for row, start_col, length in horizontal:
        if len(word) == length and isValid(crossword, word, row, start_col, "H"):
            placed_position = placeCharacters(
                crossword, word, row, start_col, "H")

            if crossWordSolver(crossword, words, word_index + 1, horizontal, vertical):
                return True

            removeWord(crossword, placed_position)

    # vertical
    for col, start_row, length in vertical:
        if len(word) == length and isValid(crossword, word, start_row, col, "V"):
            placed_position = placeCharacters(
                crossword, word, start_row, col, "V")

            if crossWordSolver(crossword, words, word_index + 1, horizontal, vertical):
                return True

            removeWord(crossword, placed_position)

    return False


def isValid(crossword, word, row, col, direction):
    for i in range(len(word)):
        r, c = (row, col + i) if direction == "H" else (row + i, col)

        if crossword[r][c] != "-" and crossword[r][c] != word[i]:
            return False

    return True


def placeCharacters(crossword, word, row, col, direction):
    placed_position = []

    for i in range(len(word)):
        r, c = (row, col + i) if direction == "H" else (row + i, col)

        if crossword[r][c] == "-":
            crossword[r][c] = word[i]

            placed_position.append((r, c))

    return placed_position


def removeWord(crossword, placed_position):
    for r, c in placed_position:
        crossword[r][c] = "-"
