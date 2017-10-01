from mpd import MPDClient


class SoundManager(object):

    def __init__(self):
        self.client = MPDClient()
        self.client.connect("localhost", 6600)

    def status(self):
        return self.client.status()
