def echo():
    while True:
        received = yield "Ready"  # primer herer it will pause and resume
        yield f"Echo {received}"


s = echo()
# start the  generator object  after that it saved state and stopped.
print(next(s))
print(
    s.send(101)
)  # send use to send the value and  resume the generator object to continue from last state
print(next(s))
print(s.send(10))  # you will wonder like  why doesnt show me the


# basically send helps us in many way we can use this  to  go and  send  the value on demand to current object


def accumulator():
    num = 0

    while True:
        x = yield num
        if x is not None:
            num += x


accum = accumulator()
print(next(accum))
print(accum.send(2))
print(accum.send(5))


def even_squared(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i**2, i

        i += 1


a = even_squared(5)
print(a)
for _ in range(
    3
):  # the reason it  worked  with 3  without the  stop iteration error when we are  using greater than 3
    # solution is  our generator  will give only those object which are valid  in this  there are only three valid  objects  0 , 2 and 4 else is skipped
    print(next(a))


#  Infinite Sequence
# Task: Create an infinite generator cycle_pattern() that cycles through the sequence "A", "B", "C" repeatedly.

# solution:


def infinite_sequence():
    a = ord("A")
    while True:
        if a > ord("C"):
            a = ord("A")

        yield chr(a)
        a += 1


iun = infinite_sequence()
print(next(iun))
print(next(iun))
print(next(iun))
print(next(iun))

print()


def infinite_sequence1():
    while True:
        yield "A"
        yield "B"
        yield "C"


op = infinite_sequence1()
print(next(op))
print(next(op))
print(next(op))
print(next(op))


###
# Task: Write a generator chunked(data, size) that splits data into chunks of size.
# Example:
# python
#
# >>> list(chunked([1, 2, 3, 4, 5], 2))  # [[1, 2], [3, 4], [5]]

# chunking the data


def chunked(data, size):
    for i in range(0, len(data), size):
        yield data[i: i + size]


sc = list(chunked([1, 2, 3, 4, 5], 2))

print(sc)

#
# Pipeline Processing
#
# Task: Build a pipeline of 3 generators:
#
#     read_lines(file): Yields lines from a file.
#
#     filter_lines(lines, keyword): Yields lines containing keyword.
#
#     count_chars(lines): Yields the character count of each line.
#
# Example:
# For a file with:
#
# Hello
# Python World
# Generator
#
# The pipeline count_chars(filter_lines(read_lines(file), "o")) should yield 5 (for "Hello"), then 7 (for "Python World").
#

# solution :


def read_lines(files):
    with open(files) as f:
        for lines in f:
            yield lines.strip()


#
# def filter_lines1(lines, key):
#     for line in lines:
#         key = key.lower()
#         if key in line:
#             yield line


def filter_lines(lines, key):
    for line in lines:
        if key in line:
            yield line


def count_chars(lines):
    for line in lines:
        yield len(line)


def addLineNumbers(lines):
    for i, line in enumerate(lines, 1):
        yield f"{i}: {line}"


s = count_chars(addLineNumbers(filter_lines(read_lines("new.txt"), "o")))

print(list(s))


######


def skipShortLines(lines, min_len):
    for line in lines:
        if len(line) >= min_len:
            yield line


a = count_chars(filter_lines(skipShortLines(read_lines("new.txt"), 4), "o"))
print(list(a))


# Write a Python program to create a generator function that generates the powers of a number up to a specified exponent.

print()


def powe_uptoExp(base, exp):
    s = 0
    while s != exp + 1:
        yield s, base**s

        s += 1


base = int(input("Enter the base : "))
exp = int(input("Enter the exp : "))
gen_pow = powe_uptoExp(base, exp)

for _ in range(exp + 1):
    print(next(gen_pow))


# running Average : write a program  which helps in generating the average of the sequence of the number

###
print("\n#### Welcome to Running Average  Calculator\n")


def runningAverage():
    count = 0
    total = 0
    while True:
        recv = yield (total / count) if count > 0 else 0
        total += recv
        print(f"Current Sum --> {total}")

        count += 1


a = runningAverage()

next(a)  # prime  the generator


while True:
    inp = input(">: ")

    if inp == "e":
        break

    inp_ = int(inp)
    print("The current average is : ", a.send(inp_))


# make a generator for generating all factors of the number
def factorGenerator(num):
    """
    THIS IS  A generator FUNCTION WHICH HELPS IN GENERATING THE  FACTORS OF GIVEN NUMBER (ARGUMENT)
    num(arg) : int
    """

    # so it is basic  we have to return the number which can divide the num
    i = 1
    while i != num + 1:
        if num % i == 0:
            yield i

        i += 1


a = list(factorGenerator(1000))
print(a)


# Generate the next Armstrong number :
# first step we can build isArmstrongNumber function
# then we will increment value one by one and check then next Armstrong
# memory wise it maybe good and all , but execution time will  incease stilll bad


# what are the other ways we can use to


# normal
