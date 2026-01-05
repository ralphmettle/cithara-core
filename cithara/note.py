from cithara.interval import Interval


# Mapping of natural notes to their semitone distance from C to be used as tokens
NATURAL_PITCHES: dict[str, int] = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11,
}

# Reverse mapping of prior dict for O(1) lookup by pitch
PITCH_TO_NATURAL: dict[int, str] = {v: k for k, v in NATURAL_PITCHES.items()}


class Note:
    def __init__(self, note_name: str) -> None:
        if not note_name:
            raise ValueError("Note string cannot be empty.")
        self._validate_note_string(note_name)
        self.note_name: str = note_name
        self.natural: str = note_name[0]
        self.pitch_class: int = self._get_pitch_class()
        self.enharmonics: list[str] = self._get_enharmonic_equivalents()
        self.canonical_name: str = self._canonise()

    def _validate_note_string(self, note_name: str) -> None:
        _valid_accidentals: tuple[str, str] = ("#", "b")
        if len(note_name) > 1:
            for acc in note_name[1:].lower():
                if acc not in _valid_accidentals:
                    raise ValueError(f"Invalid accidental in '{note_name}': {acc}")
        if note_name[0] not in NATURAL_PITCHES:
            raise ValueError(f"Invalid note name: {note_name[0]}")

    def _get_pitch_class(self) -> int:
        base_pitch: int | None = NATURAL_PITCHES.get(self.natural)
        accidental_shift: int = self._calculate_accidentals(self.note_name)

        if base_pitch is not None:
            return (base_pitch + accidental_shift) % 12
        else:
            raise ValueError("base_pitch was NoneType")

    def _get_enharmonic_equivalents(self) -> list[str]:
        # Take the pitch class of the note, and find natural pitches within 2 semitones that can be altered to reach
        enharmonics: list[str] = []
        for pitch in NATURAL_PITCHES:
            diff = NATURAL_PITCHES[pitch] - self.pitch_class
            if NATURAL_PITCHES[pitch] < self.pitch_class and abs(diff) <= 2:
                new_note: str = pitch + ("#" * abs(diff))
                enharmonics.append(new_note)
            if NATURAL_PITCHES[pitch] > self.pitch_class and diff <= 2:
                new_note: str = pitch + ("b" * diff)
                enharmonics.append(new_note)
        return enharmonics

    def _calculate_accidentals(self, note_name: str) -> int:
        val: int = 0
        for acc in note_name[1:].lower():
            if acc == "#":
                val += 1
            else:
                val -= 1
        return val

    def _canonise(self, use_flats: bool = True) -> str:
        return NoteHelper.note_name_from_pitch_class(self.pitch_class, use_flats)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Note):
            return self.pitch_class == other.pitch_class
        return False

    def __str__(self) -> str:
        return f"{self.note_name}"

    def __repr__(self) -> str:
        return f"<Note: '{self.note_name}'> (pitch class: {self.pitch_class})"


class PitchTransformer:
    @staticmethod
    def name_from_pitch(pitch_class: int) -> str | None:
        for note, pitch in NATURAL_PITCHES.items():
            if pitch_class == pitch:
                return note + "#"

    @staticmethod
    def sharpen(canonise: bool = True, use_flats: bool = False):
        pass

    @staticmethod
    def flatten(canonise: bool = True, use_flats: bool = False):
        pass


class NoteFactory:
    @staticmethod
    def from_pitch_class(pitch_class: int, use_flats: bool = True) -> Note:
        return Note(NoteHelper.note_name_from_pitch_class(pitch_class, use_flats))

    @staticmethod
    def from_natural(pitch_class: int, natural: str) -> Note:
        return Note(NoteHelper.note_name_from_natural(pitch_class, natural))

    @staticmethod
    def from_interval(
        root: Note, interval: Interval, natural: str = "", use_flats: bool = True
    ) -> Note:
        target_pitch = (root.pitch_class + interval.semitones) % 12
        if not natural:
            return NoteFactory.from_pitch_class(target_pitch, use_flats)
        else:
            return NoteFactory.from_natural(target_pitch, natural)


class NoteHelper:
    @staticmethod
    def note_name_from_pitch_class(pitch_class: int, use_flats: bool = True) -> str:
        pitch_class = pitch_class % 12
        if pitch_class in PITCH_TO_NATURAL:
            return PITCH_TO_NATURAL[pitch_class]

        if use_flats:
            target = (pitch_class + 1) % 12
            if target in PITCH_TO_NATURAL:
                return PITCH_TO_NATURAL[target] + "b"
        else:
            target = (pitch_class - 1) % 12
            if target in PITCH_TO_NATURAL:
                return PITCH_TO_NATURAL[target] + "#"
        raise ValueError(f"Invalid input: {pitch_class}")

    @staticmethod
    def note_name_from_natural(pitch_class: int, natural: str) -> str:
        diff = (pitch_class - NATURAL_PITCHES[natural]) % 12
        if diff <= 6:
            return natural + "#" * diff if diff > 0 else natural
        else:
            steps_down = 12 - diff
            return natural + "b" * steps_down
