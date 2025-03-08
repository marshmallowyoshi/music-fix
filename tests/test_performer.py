from pathlib import Path
import pytest

from music_fix import performer


@pytest.fixture
def example_flac():
    return performer.open_file(Path("tests/example.flac"))


def test_open_file(example_flac):
    assert example_flac["Display Artist"][0] == "Jóhann Jóhannsson; Air Lyndhurst String Orchestra; Anthony Weeden"
