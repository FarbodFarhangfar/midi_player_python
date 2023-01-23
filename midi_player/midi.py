from .pyknon.music import Note
from .pyknon.genmidi import Midi

from .config import NoteDic

import time
import sys
import os


class PlayMidi:
    def __init__(self, name, note_list, duration_list, tempo=80, instrument=0):
        self._path = ''
        self._notes = []
        self._tempo = tempo
        self._instrument = instrument
        self._name = name

        self._parse_notes(note_list, duration_list)

        self._midi_notes()


    def get_path(self):
        return self._path

    def get_notes(self):
        return self._notes

    def _parse_notes(self, note_list, dur):
        if len(note_list) == len(dur):
            notes_dic = NoteDic()
            notes_dic = notes_dic.get_note_dic()
            for i, notes in enumerate(note_list):
                note = notes[:-1]
                octave = notes[-1]
                duration = dur[i] / 4
                note = notes_dic[note]
                self._notes.append(Note(note, int(octave), duration))
        else:
            raise Exception("duration doest match notes")

    def _midi_notes(self):
        play = Midi(1, tempo=self._tempo, instrument=self._instrument)
        play.seq_notes(self._notes)
        return self._save_note(play)

    def _checking_for_file(self, name):
        if name == '':
            name = input("please enter a name")
        if not os.path.isdir('results'):
            os.mkdir('results')
        newfile = os.path.join('E:/github/midi_player_python/results', '{}.wav'.format(name))
        while os.path.exists(newfile):
            name = input("{} already exists, please enter a new name".format(name))
            newfile = os.path.join('E:/github/midi_player_python/results', '{}.wav'.format(name))
        return newfile

    def _save_note(self, play):
        name = self._name
        newfile = self._checking_for_file(name)
        play.write(newfile)
        self._path = newfile
