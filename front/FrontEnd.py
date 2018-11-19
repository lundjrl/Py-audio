import curses
import curses.textpad
import Exceptions

import sys

class FrontEnd:

    """Authors: Will Shreeve, Zachary Thomas, James Lund"""
    """Constructor to setup our program"""
    def __init__(self, player, library):
        self.player = player
        self.library = library
        self.player.play(sys.argv[1])
        curses.wrapper(self.menu)

    """Function to display the GUI menu"""
    def menu(self, args):
        self.stdscr = curses.initscr()
        height, width = self.stdscr.getmaxyx()
        if height < 50 or width < 50:
           raise CLI_Audio_Screen_Size_Exception("Screen too small")
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.stdscr.keypad(True) # enable arrow keys
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.openLibrary()
                self.showLibrary()
                self.stdscr.touchwin()
                self.stdscr.refresh()

    """Updates the song when changeSong is called"""
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())

    """Function for the change song functionality, asks for filepath of song"""
    def changeSong(self):
        height, width = self.stdscr.getmaxyx()
        if height < 60 or width < 60:
            raise CLI_Audio_Screen_Size_Exception("Screen Size too small.")

    """Function opens the directory i.e. library of music"""
    def openLibrary(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the file path for your library?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        self.library.__setFilepath__(path)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()

    """Show the Library/Playlist selected"""
    def showLibrary(self):
        musicList = self.library.__getMusicList__()
        self.stdscr.addstr(18, 10, "Library:")
        i = 0
        for wav in musicList:
            self.stdscr.addstr(20 + i, 10, str(i + 1) +" "+ wav)
            i = i + 1
        changeWindow = curses.newwin(5, 40, 20, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What song # would you like to play?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        songNum = changeWindow.getstr(1,1, 10)
        curses.noecho()
        self.player.play(musicList[int(songNum) - 1])
        self.stdscr.touchwin()
        self.stdscr.refresh()

    """Function that exits the program"""
    def quit(self):
        self.player.stop()
        exit()
