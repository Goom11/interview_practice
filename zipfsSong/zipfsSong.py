#!/usr/bin/python

from heapq import nlargest

def make_song(number, plays, name):
    return {
        'number': number,
        'plays': plays,
        'name': name,
        'quality': plays * number,
    }

def make_song_from_string(string_input, number):
    """Constructs song dict given song number and a string in the format:
       '#{num_plays} #{name}'
    """
    frequency, name = string_input.split()
    frequency = int(frequency)
    return make_song(number, frequency, name)

def get_top_m(songs, m):
    """Returns an array of top m songs based on quality"""
    num_songs = len(songs)
    # Each entry is a 3-element list containing the priority (quality), an entry count reversed, and the song name
    pq = [[song['quality'], -song['number'], song['name']] for song in songs]
    # The total array is treated as a priority queue implemented using python's heapq
    return nlargest(m, pq)

def run():
    n, m = map(int, raw_input().split())
    songs = [make_song_from_string(raw_input(), i + 1) for i in xrange(n)]
    top_m = get_top_m(songs, m)
    print '\n'.join([entry[2] for entry in top_m])

if __name__ == "__main__":
    run()
