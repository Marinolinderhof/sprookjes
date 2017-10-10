from mpd import MPDClient


class SoundManager(object):

    def __init__(self, directory, host="localhost"):
        self.client = MPDClient()
        self.client.connect(host, 6600)
        self.client.random(1)
        self.client.single(1)

    def status(self):
        return self.client.status()

    def pause(self):
        self.client.pause()

    def setVolume(self, volume):
        self.client.setvol(volume)

    def nextRandomSong(self):
        self.client.next()

    def disconnect(self):
        self.client.disconnect()

    def __del__(self):
        self.disconnect()
