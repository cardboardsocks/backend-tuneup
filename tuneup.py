#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Ben McKenzie, Keith Hernandez, google"

import cProfile
import pstats
import functools
import io
import timeit
from pstats import SortKey

def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner 

def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()




@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    watched = {}
    duplicates = []
    for movie in movies:
        if movie not in seen:
            watched[movie] = 1
        else:
            if watched[movie] == 1:
                duplicates.append(movie)
            watched[movie] += 1
    return duplicates
    
def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer('main()')
    r, n = 7, 3  # repeat, number constants
    result = t.repeat(repeat=r, number=n)
    min_of_averages = min(map(lambda x: x / n, result))
    return f"Best time across {r} repeats of {n} runs per repeat: {min_of_averages} sec"


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    print(timeit_helper())


if __name__ == '__main__':
    main()
