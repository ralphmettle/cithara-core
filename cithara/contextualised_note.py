from abc import ABC
from cithara.note import Note
from cithara.interval import Interval


class ContextualisedNote(ABC):
    def __init__(self, note: Note, root: Note) -> None:
        self.note: Note = note
        self.root: Note = root

    def __getattr__(self, attr):
        return getattr(self.note, attr)

    def __str__(self) -> str:
        return f"{self.note.note_name} (root: {self.root.note_name})"

    def __repr__(self) -> str:
        return f"<ContextualisedNote(note='{self.note.note_name}', root='{self.root.note_name}')>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, ContextualisedNote):
            return NotImplemented
        return self.note == other.note and self.root == other.root


class ScaleDegree(ContextualisedNote):
    def __init__(self, note: Note, root: Note, degree: int, interval: Interval) -> None:
        super().__init__(note=note, root=root)
        if degree < 0 or degree > 6:
            raise ValueError("Chord tones must be between 0 and 6 (0-indexing used)")
        self.degree: int = degree  # 0-indexed (0 - 6)
        self.interval: Interval = interval

    def __str__(self) -> str:
        return (
            f"{self.note.note_name} (root: {self.root.note_name} degree: {self.degree})"
        )

    def __repr__(self) -> str:
        return f"<ScaleDegree(degree={self.degree}, note='{self.note.note_name}', root='{self.root.note_name}', interval='{self.interval.interval_name}')>"


class ChordTone(ContextualisedNote):
    def __init__(self, note: Note, root: Note, tone: int, interval: Interval) -> None:
        super().__init__(note=note, root=root)
        if tone < 0 or tone > 12:
            raise ValueError("Chord tones must be between 0 and 12 (0-indexing used)")
        super().__init__(note=note, root=root)
        self.tone: int = tone
        self.interval: Interval = interval

    def __str__(self) -> str:
        return f"{self.note.note_name} (root: {self.root.note_name} tone: {self.tone})"

    def __repr__(self) -> str:
        return f"<ChordTone(tone={self.tone}, note='{self.note.note_name}', root='{self.root.note_name}', interval='{self.interval.interval_name}')>"
