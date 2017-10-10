import unittest
from tell_a_tale import SoundManager


class TestInitation(unittest.TestCase):

    def setUp(self):
        self.sm = SoundManager("home/koen/Repos/tell-a-tale/test_music/")
        self.status = self.sm.status()

    def test_settings(self):
        self.assertEqual(self.status["random"], '1')
        self.assertEqual(self.status["single"], '1')

    def test_music_files(self):
        self.assertFalse(len(self.sm.client.listall()) == 0)

    def tearDown(self):
        self.sm.disconnect()


if __name__ == '__main__':
    unittest.main()
