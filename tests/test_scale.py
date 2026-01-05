import pytest
from cithara.note import Note
from cithara.scale.major_scale import MajorScale
from cithara.scale.harmonic_minor_scale import HarmonicMinorScale
from cithara.contextualised_note import ScaleDegree

MAJOR_SCALE_TESTS = [
    ("C", ["C", "D", "E", "F", "G", "A", "B"]),
    ("D", ["D", "E", "F#", "G", "A", "B", "C#"]),
    ("F", ["F", "G", "A", "Bb", "C", "D", "E"]),
    ("G", ["G", "A", "B", "C", "D", "E", "F#"]),
]

HARMONIC_MINOR_TESTS = [
    ("C", ["C", "D", "Eb", "F", "G", "Ab", "B"]),
]


class TestScales:

    @pytest.mark.parametrize("root_name, expected_notes", MAJOR_SCALE_TESTS)
    def test_major_scale(self, root_name, expected_notes):
        root = Note(root_name)
        scale = MajorScale(root=root)

        assert scale.root == root
        assert scale.type == "major"
        assert isinstance(scale.notes[0], ScaleDegree)
        assert scale.note_names == expected_notes

        for i, expected_note_name in enumerate(expected_notes):
            assert scale[i].note_name == expected_note_name

    @pytest.mark.parametrize("root_name, expected_notes", HARMONIC_MINOR_TESTS)
    def test_harmonic_minor_scale(self, root_name, expected_notes):
        root = Note(root_name)
        scale = HarmonicMinorScale(root=root)

        assert scale.root == root
        assert scale.type == "harmonic_minor"
        assert isinstance(scale.notes[0], ScaleDegree)
        assert scale.note_names == expected_notes

        for i, expected_note_name in enumerate(expected_notes):
            assert scale[i].note_name == expected_note_name
