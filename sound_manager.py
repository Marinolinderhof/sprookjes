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
        # print('add song playlist')
        # self.client.add('music/t.mp3')
        self.client.playlistadd('t', './music/' )


        # self.client.play()

    def status(self):
        return self.client.status()
    
    def pause(self):
        self.client.pause()

    def setVolume(self, volume):
        self.client.setvol(volume)

    def nextRandomSong(self):
        self.client.next()
    