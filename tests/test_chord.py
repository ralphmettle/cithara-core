import pytest
import pytest
from cithara.chord.base import (
    Chord,
    MajorChord,
    MinorChord,
    DiminishedChord,
    AugmentedChord,
    ChordBuilder,
)
from cithara.note import Note
from cithara.scale.major_scale import MajorScale


# Fixtures
@pytest.fixture
def note_c():
    return Note("C")


@pytest.fixture
def major_chord_c(note_c):
    return MajorChord(root=note_c)


@pytest.fixture
def minor_chord_c(note_c):
    return MinorChord(root=note_c)


@pytest.fixture
def diminished_chord_c(note_c):
    return DiminishedChord(root=note_c)


@pytest.fixture
def augmented_chord_c(note_c):
    return AugmentedChord(root=note_c)


def test_major_chord_initialisation_from_note(major_chord_c):
    assert major_chord_c.notes == ["C", "E", "G"]


def test_minor_chord_initialisation_from_note(minor_chord_c):
    assert minor_chord_c.notes == ["C", "Eb", "G"]


def test_diminished_chord_initialisation_from_note(diminished_chord_c):
    assert diminished_chord_c.notes == ["C", "Eb", "Gb"]


def test_augmented_chord_initialisation_from_note(augmented_chord_c):
    assert augmented_chord_c.notes == ["C", "E", "G#"]


def test_first_inversion_major_chord(major_chord_c):
    first_inversion = major_chord_c.invert(1)
    assert first_inversion.notes == MajorChord(Note("C"), 1).notes
