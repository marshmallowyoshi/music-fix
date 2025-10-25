# pylint: disable=missing-docstring,redefined-outer-name


from pathlib import Path

import pytest

from music_fix import performer


@pytest.fixture
def example_flac(flac_file: Path) -> performer.AnyMusicFile:
    return performer.open_file(flac_file)


def test_open_flac(example_flac: performer.AnyMusicFile):
    assert example_flac is not None


def test_open_wav(writeable_wav_file: Path):
    wav_file = performer.open_file(writeable_wav_file)
    assert wav_file is not None


def test_get_display_artist(example_flac: performer.AnyMusicFile):
    performer.set_display_artist(example_flac, ["New Artist"])
    assert performer.get_display_artist(example_flac) == ["New Artist"]


def test_check_has_display_artist(example_flac: performer.AnyMusicFile):
    assert performer.has_display_artist(example_flac) is False
    performer.set_display_artist(example_flac, ["New Artist"])
    assert performer.has_display_artist(example_flac) is True


def test_set_display_artist(example_flac: performer.AnyMusicFile, flac_file: Path):
    performer.set_display_artist(example_flac, ["Another Artist"])
    modified_file = performer.open_file(flac_file)
    assert performer.get_display_artist(modified_file) == ["Another Artist"]
