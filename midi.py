from pyknon.music import Note
from pyknon.genmidi import Midi
from config import get_note_dic
import time
import sys
from midi2audio import FluidSynth
import os


class play_midi:
    def __init__(self, name, note_list, duration_list, tempo=80, instrument=0):
        self.notes = []
        self.tempo = tempo
        self.parse_notes(note_list, duration_list)
        self.instrument = instrument
        self._name = name
        self._midi_notes()
        self._play_note()

    def parse_notes(self, note_list, dur):
        if len(note_list) == len(dur):
            notes_dic = get_note_dic()
            for i, notes in enumerate(note_list):
                note = notes[:-1]
                octave = notes[-1]
                duration = dur[i] / 4
                note = notes_dic[note]
                self.notes.append(Note(note, int(octave), duration))
        else:
            raise Exception("duration doest match notes")

    def _midi_notes(self):
        play = Midi(1, tempo=self.tempo, instrument=self.instrument)
        play.seq_notes(self.notes)
        self._save_note(play)

    def checking_for_file(self, name):
        if name is '':
            name = input("please enter a name")
        if not os.path.isdir('results'):
            os.mkdir('results')
        newfile = os.path.join('results', '{}.wav'.format(name))
        while os.path.exists(newfile):
            name = input("{} already exists, please enter a new name".format(name))
            newfile = os.path.join('results', '{}.wav'.format(name))
        return newfile

    def _save_note(self, play):
        name = self._name
        play.write('temp.mid')
        newfile = self.checking_for_file(name)
        fs = FluidSynth()
        fs.midi_to_audio('temp.mid', newfile)
        os.remove('temp.mid')

