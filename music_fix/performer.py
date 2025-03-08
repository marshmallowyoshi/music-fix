from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeAlias

import music_tag

if TYPE_CHECKING:
    # Set type alias that should already exist in mutagen!!!!!!!!!
    from mutagen.id3 import ID3FileType
    from mutagen.asf import ASF
    from mutagen.apev2 import APEv2File
    from mutagen.flac import FLAC
    from mutagen.mp3 import MP3
    from mutagen.oggflac import OggFLAC
    from mutagen.oggspeex import OggSpeex
    from mutagen.oggtheora import OggTheora
    from mutagen.oggvorbis import OggVorbis
    from mutagen.oggopus import OggOpus
    from mutagen.trueaudio import TrueAudio
    from mutagen.wavpack import WavPack
    from mutagen.mp4 import MP4
    from mutagen.musepack import Musepack
    from mutagen.monkeysaudio import MonkeysAudio
    from mutagen.optimfrog import OptimFROG
    from mutagen.aiff import AIFF
    from mutagen.aac import AAC
    from mutagen.ac3 import AC3
    from mutagen.smf import SMF
    from mutagen.tak import TAK
    from mutagen.dsf import DSF
    from mutagen.dsdiff import DSDIFF
    from mutagen.wave import WAVE

    AnyMusicFile: TypeAlias = (
        ID3FileType
        | ASF
        | APEv2File
        | FLAC
        | MP3
        | OggFLAC
        | OggSpeex
        | OggTheora
        | OggVorbis
        | OggOpus
        | TrueAudio
        | WavPack
        | MP4
        | Musepack
        | MonkeysAudio
        | OptimFROG
        | AIFF
        | AAC
        | AC3
        | SMF
        | TAK
        | DSF
        | DSDIFF
        | WAVE
    )
else:
    AnyMusicFile = Any


def open_file(file_path: Path) -> AnyMusicFile:
    """Open file and return mutagen object"""
    return music_tag.load_file(file_path).mfile


def has_display_artist(music_file: AnyMusicFile) -> bool:
    """Check if display artist tag exists"""
    return "display artist" in music_file


def get_display_artist(music_file: AnyMusicFile) -> str:
    """Get display artist tag"""
    return music_file["display artist"]


def set_display_artist(music_file: AnyMusicFile, artist: str) -> None:
    """Set display artist tag"""
    music_file["display artist"] = artist
    music_file.save()
