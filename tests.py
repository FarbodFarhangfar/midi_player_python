import unittest
from midi_player.parse import Parse
from midi_player.midi import PlayMidi
import pathlib as pl
import os


class TestParse(unittest.TestCase):
    def test_note_parser(self):
        parser = Parse()
        self.assertEqual(parser.get_notes("A B C2 D G8"), ['A5', 'B5', 'C2', 'D5', 'G8'])

    def test_get_duration(self):
        parser = Parse()
        self.assertEqual(parser.get_dur("8 4 2 8 16"), [8, 4, 2, 8, 16])


class TestPlayMidi(unittest.TestCase):

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_parse_note(self):
        note = ['A5', 'B5', 'C2', 'D5', 'G8']
        duration = [8, 4, 2, 8, 16]
        name = "E:/github/midi_player_python/results/test.wav"
        os.remove(name)

        player = PlayMidi("test", note, duration)

        self.assertIsFile(player.get_path())

    def test_checking_for_file(self):
        pass


if __name__ == "__main__":
    unittest.main()
