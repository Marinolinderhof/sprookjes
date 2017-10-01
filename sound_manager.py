from mpd import MPDClient


class Soundmanager(object):

    def __init__(self):
        self.client = MPDClient()
        self.client.connect("localhost", 6600)

    def status(self):
        self.client.status()
