"""Playlist class for the player"""

"""Should give the functionality for a library of music in our program"""

import glob

class Library:
    def __init__(self):
        #do nothing:)
        #self._musicList
        # self._filepath
        self.position = 0

    def __setFilepath__(self, filepath):
        self._filepath = filepath
        self._musicList = glob.glob(self._filepath.decode(encoding="utf-8") + '*.wav')

    #def __choose__(self, track):

    def __getMusicList__(self):
        return self._musicList
