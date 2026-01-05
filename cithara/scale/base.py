from abc import ABC
from cithara.note import Note, NoteFactory
from cithara.interval import Interval
from cithara.contextualised_note import ScaleDegree

# Mapping of scale varieties to their interval patterns from the root
# NOTE: Modes are to be handled internally by scales (hence "minor" not being included here)
SCALE_FORMULA: dict[str, list[int]] = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
    "melodic_minor": [0, 2, 3, 5, 7, 9, 11],
}


class Scale(ABC):
    def __init__(self, root: Note, type: str) -> None:
        type = type.strip()
        if type not in SCALE_FORMULA:
            raise ValueError(f"Invalid scale type: {type}")

        self.root: Note = root
        self.type: str = type
        self.formula: list[int] = SCALE_FORMULA.get(self.type, [])
        self.notes: list[ScaleDegree] = ScaleFactory.create(
            root=self.root, formula=self.formula
        )

        # 0-indexed method of getting a specifc scale degree
        @classmethod
        def degree(self, degree: int):
            # How do I want to represent the degree?
            # Should I allow for "extended degrees" i.e. mod(7) operation?
            # Do I expect the user to only pass in a number 1-7?
            pass

    @property
    def note_names(self) -> list[str]:
        """Return the scale’s notes as a list of strings."""
        return [deg.note.note_name for deg in self.notes]


class ScaleFactory:
    @staticmethod
    def create(root: Note, formula: list[int]) -> list[ScaleDegree]:
        diatonic_notes = ["C", "D", "E", "F", "G", "A", "B"]
        degree = 0
        start = diatonic_notes.index(root.natural)

        scale = []
        for interval in formula:
            letter = diatonic_notes[(start + degree) % 7]
            interval_obj = Interval(interval)
            note = NoteFactory.from_interval(
                root=root, interval=interval_obj, natural=letter
            )
            scale.append(
                ScaleDegree(note=note, root=root, degree=degree, interval=interval_obj)
            )
            degree += 1

        return scale
