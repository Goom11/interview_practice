#!/usr/bin/env python

import itertools as it

def islands(seq):
    top = max(seq)
    if top == 0:
        return 0
    seq = [list(group) for _, group in it.groupby(seq, lambda x: x == top)]
    cur_islands = sum(1 for x in seq if top in x)
    seq = list(it.chain(*seq))
    seq = [el if el != top else top - 1 for el in seq]
    cur_islands = cur_islands + islands(seq)
    return cur_islands

def format_seq(seq):
    seq = [int(el) for el in seq.split()]
    seq = seq[1:]
    return seq

def get_input():
    k = int(raw_input())
    seqs = [format_seq(raw_input()) for _ in xrange(k)]
    return seqs

def print_results(results):
    for i, r in enumerate(results):
        print i + 1, r

def main():
    seqs = get_input()
    seqs = [islands(seq) for seq in seqs]
    print_results(seqs)

if __name__ == "__main__":
    main()
