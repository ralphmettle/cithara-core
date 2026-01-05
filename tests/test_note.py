import pytest
from cithara.interval import Interval
from cithara.note import Note, PitchTransformer, NoteGenerator


@pytest.fixture
def note_b():
    return Note("B")


@pytest.fixture
def note_c():
    return Note("C")


@pytest.fixture
def note_c_sharp():
    return Note("C#")


@pytest.fixture
def note_c_flat():
    return Note("Cb")


@pytest.fixture
def note_d_sharp():
    return Note("D#")


@pytest.fixture
def note_e():
    return Note("E")


@pytest.fixture
def note_e_flat():
    return Note("Eb")


@pytest.fixture
def note_f_sharp():
    return Note("F#")


@pytest.fixture
def note_dbb():
    return Note("Dbb")


# Interval Fixtures
@pytest.fixture
def minor_third():
    return Interval(3)


@pytest.fixture
def major_third():
    return Interval(4)


@pytest.fixture
def note_c_sharp_from_natural():
    return NoteGenerator.from_natural(pitch_class=1, natural="C")


@pytest.fixture
def note_c_flat_from_natural():
    return NoteGenerator.from_natural(pitch_class=-1, natural="C")


@pytest.fixture
def note_d_bb_from_natural():
    return NoteGenerator.from_natural(pitch_class=0, natural="D")


def test_note_initialisation(note_c_sharp):
    assert note_c_sharp.note_name == "C#"
    assert note_c_sharp.natural == "C"
    assert note_c_sharp.pitch_class == 1


def test_invalid_note_raises():
    with pytest.raises(ValueError):
        Note("H")
    with pytest.raises(ValueError):
        Note("C$")
    with pytest.raises(ValueError):
        Note("")


def test_pitch_class_calculation():
    assert Note("C").pitch_class == 0
    assert Note("B#").pitch_class == 0
    assert Note("D#").pitch_class == 3
    assert Note("Eb").pitch_class == 3
    assert Note("F##").pitch_class == 7
    assert Note("Gbb").pitch_class == 5


def test_enharmonic_equivalents(note_e_flat, note_d_sharp):
    enharmonics_of_eb = note_e_flat.enharmonics
    enharmonics_of_d_sharp = note_d_sharp.enharmonics
    assert "D#" in enharmonics_of_eb or "Eb" in enharmonics_of_d_sharp


def test_note_equality(note_d_sharp, note_e_flat, note_c, note_c_sharp):
    assert note_d_sharp == note_e_flat
    assert note_c != note_c_sharp


def test_str_and_repr(note_f_sharp):
    assert str(note_f_sharp) == "F#"
    assert repr(note_f_sharp) == "<Note: 'F#'> (pitch class: 6)"


def test_canonise_method(note_c_sharp, note_e_flat):
    canonised = note_e_flat._canonise()
    assert note_c_sharp._canonise(use_flats=False) == "C#"
    assert canonised in {"D#", "Eb"}


def test_name_from_pitch():
    assert PitchTransformer.name_from_pitch(0) == "C#"
    assert PitchTransformer.name_from_pitch(2) == "D#"


def test_generate_from_pitch_class(
    note_b, note_c, note_c_flat, note_c_sharp, note_d_sharp
):
    assert (
        NoteGenerator.from_pitch_class(pitch_class=0, use_flats=False).note_name
        == note_c.note_name
    )
    assert (
        NoteGenerator.from_pitch_class(pitch_class=-1, use_flats=True).note_name
        == note_b.note_name
    )
    assert (
        NoteGenerator.from_pitch_class(pitch_class=1, use_flats=False).note_name
        == note_c_sharp.note_name
    )
    assert (
        NoteGenerator.from_pitch_class(pitch_class=3, use_flats=False).note_name
        == note_d_sharp.note_name
    )


def test_generate_from_interval(
    note_c, note_e, note_e_flat, minor_third, major_third, note_d_sharp
):
    assert (
        NoteGenerator.from_interval(root=note_c, interval=major_third).note_name
        == note_e.note_name
    )
    assert (
        NoteGenerator.from_interval(root=note_c, interval=minor_third).note_name
        == note_e_flat.note_name
    )
    assert (
        NoteGenerator.from_interval(
            root=note_c, interval=minor_third, use_flats=False
        ).note_name
        == note_d_sharp.note_name
    )
    assert (
        NoteGenerator.from_interval(
            root=note_c, interval=minor_third, natural="E"
        ).note_name
        == note_e_flat.note_name
    )
    assert (
        NoteGenerator.from_interval(
            root=note_c, interval=major_third, natural="E"
        ).note_name
        == note_e.note_name
    )
    assert (
        NoteGenerator.from_interval(
            root=note_c, interval=major_third, natural="F"
        ).note_name
        != note_e.note_name
    )


def test_generate_from_natural(
    note_c_sharp_from_natural,
    note_c_flat_from_natural,
    note_d_bb_from_natural,
    note_b,
    note_c,
    note_c_flat,
    note_c_sharp,
    note_dbb,
):
    assert note_c_sharp_from_natural == note_c_sharp
    assert note_c_sharp_from_natural.note_name == "C#"
    assert note_c_sharp_from_natural.pitch_class == 1
    assert note_c_sharp_from_natural.enharmonics == note_c_sharp.enharmonics

    assert note_c_flat_from_natural == note_c_flat
    assert note_c_flat_from_natural == NoteGenerator.from_natural(11, "C")
    assert note_c_flat_from_natural.note_name == "Cb"
    assert note_c_flat_from_natural.pitch_class == 11
    assert note_c_flat_from_natural == note_c_flat == note_b
    assert (
        note_c_flat_from_natural.enharmonics
        == note_c_flat.enharmonics
        == note_b.enharmonics
    )

    assert note_d_bb_from_natural == note_dbb
    assert note_d_bb_from_natural.note_name == "Dbb"
    assert note_d_bb_from_natural.pitch_class == 0
    assert note_d_bb_from_natural.enharmonics == note_c.enharmonics
