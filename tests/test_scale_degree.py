import pytest
from cithara.interval import Interval
from cithara.note import Note
from cithara.contextualised_note import ScaleDegree


def test_scale_degree_initialisation():
    scale_degree = ScaleDegree(
        note=Note("C"), root=Note("A"), degree=3, interval=Interval(3)
    )
    assert scale_degree.note.note_name == "C"
    assert scale_degree.interval.semitones == 3
    assert scale_degree.interval.interval_name == "Minor Third"


def test_scale_degree_representation():
    scale_degree = ScaleDegree(
        note=Note("C"), root=Note("A"), degree=3, interval=Interval(3)
    )
    assert str(scale_degree) == "C (root: A, degree: 3)"
    assert (
        repr(scale_degree)
        == f"<ScaleDegree degree=3, note='C', root='A', interval='Minor Third'>"
    )
