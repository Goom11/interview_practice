#!/usr/bin/python

from heapq import nlargest

class Song(object):
    """Simple Song class used to determine quality of songs on an album"""

    def __init__(self, number, frequency, name):
        self.number = number
        self.frequency = float(frequency)
        self.name = name

    # Alternate constructor
    @classmethod
    def from_input(cls, input, number):
        """Constructs Song object given song number and an input in the format: '#{num_plays} #{name}'"""
        cls(number, frequency, name)

    def get_quality(self, first_frequency):
        """Gets quality based on qi = fi/zi where zi is proportional to 1/i"""
        zipfs = first_frequency / self.number
        return self.frequency / zipfs

def get_top_m(songs, m):
    """Returns an array of top m songs based on quality"""
    num_songs = len(songs)
    first_frequency = songs[0].frequency
    # Each entry is a 3-element list containing the priority, an entry count reversed, and the song
    pq = [[song.get_quality(first_frequency), num_songs - song.number, song] for song in songs]
    return nlargest(m, pq)

def get_songs():
    n, m = map(int, raw_input().split())
    songs = [Circle.from_input(raw_input(), i) for i in xrange(n)]
    return None

def run():
    songs = get_songs()
    top_m = album.get_top_m()
    print [i[2].name for i in top_m]

s1 = Song(1, 100, "a")
s2 = Song(2, 50, "b")
s3 = Song(3, 100, "c")
songs = [s1, s2, s3]
t = get_top_m(songs, 3)
print t
print [i[2].name for i in t]
get_songs()
