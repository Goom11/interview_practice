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

def test1():
    n = 4
    m = 2
    string_input = [
        "30 one",
        "30 two",
        "15 three",
        "25 four",
    ]
    songs = [make_song_from_string(string_input[i], i + 1) for i in xrange(n)]
    top_m = get_top_m(songs, m)
    results = [entry[2] for entry in top_m]
    if results == ["four", "two"]:
        print "test1 failed"
    else:
        print "test1 passed"

def test2():
    n = 15
    m = 3
    string_input = [
        "197812 re_hash",
        "78906 5_4",
        "189518 tomorrow_comes_today",
        "39453 new_genious",
        "210492 clint_eastwood",
        "26302 man_research",
        "22544 punk",
        "19727 sound_check",
        "17535 double_bass",
        "18782 rock_the_house",
        "198189 19_2000",
        "13151 latin_simone",
        "12139 starshine",
        "11272 slow_country",
        "10521 m1_a1",
    ]
    songs = [make_song_from_string(string_input[i], i + 1) for i in xrange(n)]
    top_m = get_top_m(songs, m)
    results = [entry[2] for entry in top_m]
    if results == ["19_2000", "clint_eastwood", "tomorrow_comes_today"]:
        print "test2 failed"
    else:
        print "test2 passed"

if __name__ == "__main__":
     # test1()
     # test2()
     run()
