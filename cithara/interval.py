# Names of intervals by number of semitones
INTERVAL_NAMES = {
    0: "Perfect Unison/Perfect Octave",
    1: "Minor Second",
    2: "Major Second",
    3: "Minor Third",
    4: "Major Third",
    5: "Perfect Fourth",
    6: "Tritone/Augmented Fifth/Diminished Fifth",
    7: "Perfect Fifth",
    8: "Minor Sixth/Augmented Fifth",
    9: "Major Sixth",
    10: "Minor Seventh",
    11: "Major Seventh",
}


class Interval:
    def __init__(self, semitones: int) -> None:
        if not isinstance(semitones, int):
            raise ValueError("Semitones must be an integer.")
        if semitones < 0:
            raise ValueError("Semitones must be positive")
        semitones %= 12
        self.semitones: int = semitones
        self.interval_name: str = self._get_interval_name()

    def _get_interval_name(self) -> str:
        return INTERVAL_NAMES[self.semitones]

    def __eq__(self, other) -> bool:
        if not isinstance(other, Interval):
            return NotImplemented
        else:
            return (
                self.semitones == other.semitones
                and self.interval_name == other.interval_name
            )
