from mpd import MPDClient

class SoundManager(object):

    def __init__(self):
        self.client = MPDClient()
        self.client.connect("localhost", 6600)
        self.client.random(1)
        self.client.setvol(50)
        self.client.single(1)
        print('current playlist')
        print(self.client.playlist())
        print('add default playlist')
        self.client.id('music/t.mp3')
        print(id)
        # self.client.play()

    def status(self):
        return self.client.status()
    
    def pause(self):
        self.client.pause()

    def setVolume(self, volume):
        self.client.setvol(volume)

    def nextRandomSong(self):
        self.client.next()
    