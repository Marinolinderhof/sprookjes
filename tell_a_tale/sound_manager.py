from persisten_client import PersistentMPDClient
import asyncio

class SoundManager(object):
    def __init__(self):
        # Persistent MDP client it's wrapper for all actions
        self.client = PersistentMPDClient(host="localhost", port=6600)
        
        # player
        self.client.repeat(0)
        self.client.random(1)
        self.client.single(1)
        self.client.consume(0)
        #playlist
        self.loadPlaylist('queue1')
            
    def loadPlaylist(self, playlist):
        print('[LOAD PLAYLIST] clear')
        self.client.clear()
        print('[LOAD PLAYLIST] loading')
        self.client.load('queue1')
        print('[LOAD PLAYLIST] shuffle')
        self.client.shuffle()

    def status(self):                   
        return self.client.status()
    
    async def poller(self):
        print("Hello World!")

    def nextRandomSong(self):
        print('[NEXT RANDOM SONG]')
        loop = asyncio.get_event_loop()
        # Blocking call which returns when the hello_world() coroutine is done
        loop.run_until_complete(self.poller())
        loop.close()

        self.poller()
        if self.status()['state'] == 'play':
            print('status is play next!')
            self.client.repeat(1)
            self.client.next()
            self.client.repeat(0)
            return
        self.client.play()

    def __del__(self):
        self.client.disconnect()
