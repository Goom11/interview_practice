#!/usr/bin/env python

def fly(dataset):
    d, a, b, f = dataset
    elapsed_time = d/(f + b)
    elapsed_dist_a = elapsed_time * a
    elapsed_dist_b = elapsed_time * b
    elapsed_dist_f = elapsed_time * f
    if elapsed_dist_f < 0.01:
        return elapsed_dist_f
    remaining_dist = d - (elapsed_dist_a + elapsed_dist_b)
    elapsed_dist_f = elapsed_dist_f + fly((remaining_dist, b, a, f))
    return elapsed_dist_f

def format_dataset(dataset):
    dataset = [float(el) for el in dataset.split()]
    dataset = dataset[1:]
    return dataset

def get_input():
    k = int(raw_input())
    datasets = [format_dataset(raw_input()) for _ in xrange(k)]
    return datasets

def print_results(results):
    for i, el in enumerate(results):
        print i + 1, round(el, 2)

def main():
    datasets = get_input()
    datasets = [fly(dataset) for dataset in datasets]
    print_results(datasets)

if __name__ == "__main__":
    main()
