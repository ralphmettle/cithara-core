from abc import ABC
from cithara.contextualised_note import ChordTone
from cithara.interval import Interval
from cithara.note import Note, NoteGenerator

# Representation of chord tones as intervals from root
CHORD_FORMULA: dict[str, list[int]] = {
    "minor": (0, 3, 7),
    "major": (0, 4, 7),
    "diminished": (0, 3, 6),
    "augmented": (0, 4, 8),
}


class Chord(ABC):
    def __init__(self, root: Note, type: str) -> None:
        self.root: Note = root
        self.type: str = type
        self.formula: tuple[int] = CHORD_FORMULA.get(self.type, [])
        self._root_position: tuple[ChordTone] = tuple(ChordBuilder.build(
            root=self.root, formula=self.formula
        ))
        self.tones: tuple[ChordTone] = list(self._root_position)
        self.notes: list[str] = [tone.note.note_name for tone in self.tones]
        # inversion type
        self.form: str = "root position"

    def invert(self, inversion: int) -> None:
        if inversion > len(self) - 1:
            raise ValueError("Inversion cannot be larger than the number of tones (0-indexed)")
        if inversion < 0:
            raise ValueError("Inversion must be greater than 0")
        inverted: list[str] = []
        ctr = 0
        while ctr < len(self):
            inverted.append(self._root_position[inversion])
            inversion = (inversion + 1) % len(self)
            ctr += 1
        self.tones = inverted
        self.notes = [tone.note.note_name for tone in inverted]
        match inversion:
            case 0:
                self.form = "root position"
            case 1:
                self.form = "first inversion"
            case 2:
                self.form = "second inversion"
            case 3:
                self.form = "third inversion"
        
    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.notes}>"

    def __str__(self):
        return f"{self.root.note_name} {self.type}{ f" ({self.form})" if self.form != "root position" else ""}: {", ".join(self.notes)}"
    
    def __eq__(self, other: "Chord") -> bool:
        if isinstance(other, Note):
            return set(self.notes) == set(other.notes)
        return NotImplemented

    def __len__(self):
        return len(self.notes)

class MajorChord(Chord):
    def __init__(self, root: Note):
        super().__init__(root=root, type="major")


class MinorChord(Chord):
    def __init__(self, root: Note):
        super().__init__(root=root, type="minor")


class DiminishedChord(Chord):
    def __init__(self, root: Note):
        super().__init__(root=root, type="diminished")


class AugmentedChord(Chord):
    def __init__(self, root: Note):
        super().__init__(root=root, type="augmented")


class ChordBuilder:
    @staticmethod
    def build(root: Note, formula: list[int]) -> list[ChordTone]:
        note_ref = ["C", "D", "E", "F", "G", "A", "B"]
        ctr = 0
        start = note_ref.index(root.natural)

        chord = []
        for interval in formula:
            letter = note_ref[(start + ctr) % 7]
            note = NoteGenerator.from_interval(
                root=root, interval=Interval(interval), natural=letter
            )
            chord.append(
                ChordTone(note=note, root=root, tone=ctr, interval=Interval(interval))
            )
            ctr += 2

        return chord


if __name__ == "__main__":
    maj = MajorChord(Note("C"))
    print(maj)

    mnr = MinorChord(Note("C"))
    print(mnr)

    dim = DiminishedChord(Note("C"))
    print(dim)

    aug = AugmentedChord(Note("C"))
    print(aug)

    maj.invert(1)
    print(maj)
