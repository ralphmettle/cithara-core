import pytest
from cithara.note import Note
from cithara.scale.major_scale import MajorScale
from cithara.scale.harmonic_minor_scale import HarmonicMinorScale
from cithara.contextualised_note import ScaleDegree


@pytest.fixture
def note_c():
    return Note("C")


@pytest.fixture
def note_d():
    return Note("D")


@pytest.fixture
def note_f():
    return Note("F")


@pytest.fixture
def note_g():
    return Note("G")


@pytest.fixture
def c_major(note_c):
    return MajorScale(root=note_c)


@pytest.fixture
def g_major(note_g):
    return MajorScale(root=note_g)


@pytest.fixture
def d_major(note_d):
    return MajorScale(root=note_d)


@pytest.fixture
def f_major(note_f):
    return MajorScale(root=note_f)


@pytest.fixture
def c_harmonic_minor(note_c):
    return HarmonicMinorScale(root=note_c)


def test_initialise_major_scale(
    c_major, g_major, d_major, f_major, note_c, note_g, note_d, note_f
):
    assert c_major.root == note_c
    assert c_major.type == "major"
    assert isinstance(c_major.notes[0], ScaleDegree)
    assert c_major.note_names == ["C", "D", "E", "F", "G", "A", "B"]

    assert g_major.root == note_g
    assert g_major.type == "major"
    assert isinstance(g_major.notes[0], ScaleDegree)
    assert g_major.note_names == ["G", "A", "B", "C", "D", "E", "F#"]

    assert d_major.root == note_d
    assert d_major.type == "major"
    assert isinstance(d_major.notes[0], ScaleDegree)
    assert d_major.note_names == ["D", "E", "F#", "G", "A", "B", "C#"]

    assert f_major.root == note_f
    assert f_major.type == "major"
    assert isinstance(f_major.notes[0], ScaleDegree)
    assert f_major.note_names == ["F", "G", "A", "Bb", "C", "D", "E"]


def test_initialise_harmonic_minor_scale(c_harmonic_minor, note_c):
    assert c_harmonic_minor.root == note_c
    assert c_harmonic_minor.type == "harmonic_minor"
    assert isinstance(c_harmonic_minor.notes[0], ScaleDegree)
    assert c_harmonic_minor.note_names == ["C", "D", "Eb", "F", "G", "Ab", "B"]
