# pylint: disable=redefined-outer-name
import pathlib
import shutil

import pytest
from mocks import mock_generate_audio_files


@pytest.fixture(scope="session")
def _example_wav_file(tmp_path_factory: pytest.TempPathFactory) -> pathlib.Path:
    """Read-only base WAV file to be used for generating other audio files."""
    temp_dir = tmp_path_factory.mktemp("audio_files")
    wav_path = temp_dir / "example.wav"
    mock_generate_audio_files.generate_base_wav(wav_path)
    return wav_path


@pytest.fixture()
def writeable_wav_file(
    _example_wav_file: pathlib.Path, tmp_path_factory: pytest.TempPathFactory
) -> pathlib.Path:

    temp_dir = tmp_path_factory.mktemp("writeable_audio_files")
    writeable_wav_path = temp_dir / "writeable_example.wav"
    shutil.copy(_example_wav_file, writeable_wav_path)
    return writeable_wav_path


@pytest.fixture()
def flac_file(
    _example_wav_file: pathlib.Path, tmp_path_factory: pytest.TempPathFactory
) -> pathlib.Path:

    temp_dir = tmp_path_factory.mktemp("flac_audio_files")
    flac_path = mock_generate_audio_files.convert_to_new_ext(_example_wav_file, ".flac")
    new_flac_path = temp_dir / "example.flac"
    shutil.move(flac_path, new_flac_path)
    return new_flac_path
