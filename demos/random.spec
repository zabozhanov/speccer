import random

set up
    seq = range(10)

doesn't lose any elements
    random.shuffle(seq)
    seq.sort()

    seq == range(10)

chooses element in sequence
    random.choice(seq) in seq

