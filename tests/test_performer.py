# pylint: disable=missing-docstring,redefined-outer-name

import shutil
from pathlib import Path

import pytest

from music_fix import performer


@pytest.fixture
def example_flac_path():
    return Path("tests/example.flac")


@pytest.fixture
def example_flac(example_flac_path):
    return performer.open_file(example_flac_path)


def test_open_file(example_flac):
    assert (
        example_flac["Display Artist"][0]
        == "Jóhann Jóhannsson; Air Lyndhurst String Orchestra; Anthony Weeden"
    )


def test_get_display_artist(example_flac):
    assert performer.get_display_artist(example_flac) == example_flac["Display Artist"]


def test_check_has_display_artist(example_flac):
    assert performer.has_display_artist(example_flac) is True


def test_set_display_artist(example_flac_path, tmp_path):
    file_copy_path = tmp_path / "example_copy.flac"
    shutil.copy(example_flac_path, file_copy_path)
    copy_flac = performer.open_file(file_copy_path)
    performer.set_display_artist(copy_flac, ["New Artist"])
    assert performer.get_display_artist(copy_flac) == ["New Artist"]
    copy_flac.save()
    reloaded_flac = performer.open_file(file_copy_path)
    assert performer.get_display_artist(reloaded_flac) == ["New Artist"]
