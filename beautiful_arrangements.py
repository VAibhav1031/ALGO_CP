def generatePermutations(process, strii):
    #  okay  now  we are doing

    if not strii:
        yield process  # yield olny being used  resume and pause the thing  and  this  will be not good
        # in recursion cause we have to be stopped when we hit the base case so then we use the return thinsg
        return

    ch = strii[0]
    for i in range(len(process) + 1):
        f = process[:i]
        s = process[i : len(process)]
        yield from generatePermutations(f + [ch] + s, strii[1:])


s = generatePermutations([], [1, 2, 3, 4])
for i in s:
    print(i)
