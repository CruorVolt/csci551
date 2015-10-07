from operator import itemgetter
from random import randrange
import time
import matplotlib.pyplot as plt


def argmax(items):
    return max(enumerate(items), key=itemgetter(1))


def global_alignment(ref, seq, match=1, mismatch=0, gap=0):
    # add garbage character to beginning of strings to ease indexing
    ref = "-"+ref
    seq = "-"+seq
    # build pointer matrix and score matrix
    P = [[0 for j in range(len(seq))] for i in range(len(ref))]
    S = [row[:] for row in P]
    # initialize first columns
    for i in range(1, len(ref)):
        P[i][0] = 1
        S[i][0] = S[i-1][0]+gap
    # initialize first rows
    for j in range(1, len(seq)):
        P[0][j] = 2
        S[0][j] = S[0][j-1]+gap
    # populate the matrix
    for i in range(1, len(ref)):
        for j in range(1, len(seq)):
            pointer, score = argmax([
                S[i-1][j-1]+(match if ref[i] == seq[j] else mismatch),
                S[i-1][j]+gap, S[i][j-1]+gap])
            P[i][j] = pointer
            S[i][j] = score
    # traceback
    ref_out = ''
    seq_out = ''
    i = len(ref)-1
    j = len(seq)-1
    while i != 0 or j != 0:
        if P[i][j] == 0:  # match/mismatch
            ref_out = ref[i]+ref_out
            seq_out = seq[j]+seq_out
            i -= 1
            j -=1
        elif P[i][j] == 1:  # deletion
           seq_out = "-"+seq_out
           ref_out = ref[i]+ref_out
           i -= 1
        elif P[i][j] == 2:  # insertion
           seq_out = seq[j]+seq_out
           ref_out = "-"+ref_out
           j -= 1
    return ref_out, seq_out, S, P


def random_sequence(length):
    bases = ['A', 'C', 'T', 'G']
    return ''.join([bases[randrange(4)] for i in range(length)])

if __name__ == "__main__":
    lengths = [10, 100, 1000, 10000, 100000, 1000000]
    iterations = 100
    avgs = [0]
    for l in lengths:
        avg = 0
        for i in range(iterations):
            ref = random_sequence(l)
            seq = random_sequence(l)
            start = time.time()
            ref, seq, S, P = global_alignment("APPLE", "HAPPE")
            stop = time .time()
            avg += (stop-start)*1000000
        avgs.append(avg/iterations)
    plt.plot(avgs, 'ro')
    m = max(avgs)
    d = 50-m%50
    plt.axis([1, len(lengths), 0, m+d])
    plt.ylabel('Average Run-Time (microseconds)')
    plt.xlabel('Sequence Length (10^X)')
    plt.title('Average Global Alignment Run-Times')
    plt.show()
