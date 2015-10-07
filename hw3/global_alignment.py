from operator import itemgetter


def argmax(items):
    return max(enumerate(items), key=itemgetter(1))


def global_alignment(ref, seq, match=1, mismatch=-1, gap=-1):
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


if __name__ == "__main__":
    ref, seq, S, P = global_alignment("APPLE", "HAPPE")
    print ref
    print seq
    print ""
    print "S"
    for row in S:
        print row
    print ""
    print "P"
    for row in P:
        print row
