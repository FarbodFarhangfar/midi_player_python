from midi_player.parse import Parse
from midi_player import midi

if __name__ == "__main__":
    name = input("file_name\n")
    tempo = int(input("insert tempo\n"))
    instruments = int(input("instrument number\n"))
    parser = Parse()
    notes = input("insert notes\n")
    notes = parser.get_notes(notes)

    duration = input("insert note values\n")
    duration = parser.get_dur(duration)

    play = midi.play_midi(name, notes, duration, tempo, instruments)
