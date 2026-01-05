import pytest
from cithara.interval import Interval


class TestInterval:
    def test_interval_initialisation(self):
        interval = Interval(3)
        assert interval.semitones == 3
        assert interval.interval_name == "Minor Third"

    def test_invalid_interval_raises(self):
        with pytest.raises(ValueError):
            Interval("hello")

        with pytest.raises(ValueError):
            Interval([5])

    def test_handle_large_interval(self):
        interval = Interval(77)
        assert interval.semitones == 5
        assert interval.interval_name == "Perfect Fourth"

    def test_handle_negative_interval(self):
        with pytest.raises(ValueError):
            Interval(-1)
