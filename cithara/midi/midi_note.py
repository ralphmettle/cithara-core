from cithara.note import Note


class MIDINote(Note):
    def __init__(self, note_name: str, octave: int, velocity: int = 64) -> None:
        super().__init__(note_name=note_name)
        if velocity > 127:
            raise ValueError(f"Velocity must be between 0-127")
        if octave > 9:
            raise ValueError(f"Octave must be between 0-9")
        self.velocity = velocity
        self.octave = octave
        self.midi_note = (
            octave + 1
        ) * 12 + self.pitch_class  # midi values start at -1 so C-1 = 0

    @property
    def frequency(self) -> float:
        return 440.0 * (2 ** ((self.midi_note - 69) / 12))

    def __repr__(self):
        return f"<MIDINote: '{self.note_name}{self.octave}' (MIDI={self.midi_note} velocity={self.velocity} frequency={self.frequency:.2f})>"


if __name__ == "__main__":
    midi_c = MIDINote("C", 4)
    print(repr(midi_c))
