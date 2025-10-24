from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterable, TypeAlias

import music_tag

if TYPE_CHECKING:
    # Set type alias that should already exist in mutagen!!!!!!!!!
    from mutagen.aac import AAC
    from mutagen.ac3 import AC3
    from mutagen.aiff import AIFF
    from mutagen.apev2 import APEv2File
    from mutagen.asf import ASF
    from mutagen.dsdiff import DSDIFF
    from mutagen.dsf import DSF
    from mutagen.flac import FLAC
    from mutagen.id3 import ID3FileType
    from mutagen.monkeysaudio import MonkeysAudio
    from mutagen.mp3 import MP3
    from mutagen.mp4 import MP4
    from mutagen.musepack import Musepack
    from mutagen.oggflac import OggFLAC
    from mutagen.oggopus import OggOpus
    from mutagen.oggspeex import OggSpeex
    from mutagen.oggtheora import OggTheora
    from mutagen.oggvorbis import OggVorbis
    from mutagen.optimfrog import OptimFROG
    from mutagen.smf import SMF
    from mutagen.tak import TAK
    from mutagen.trueaudio import TrueAudio
    from mutagen.wave import WAVE
    from mutagen.wavpack import WavPack

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


def get_display_artist(music_file: AnyMusicFile) -> list[str]:
    """Get display artist tag"""
    return music_file["display artist"]


def set_display_artist(music_file: AnyMusicFile, artist: Iterable[str]) -> None:
    """Set display artist tag"""
    music_file["display artist"] = list(artist)
    music_file.save()

def is_artist_valid(music_file: AnyMusicFile) -> bool:
    """Check if artist is the same as display artist and only contains one value"""
    ret = True
    if has_display_artist(music_file) and (music_file["display artist"] != music_file["artist"]):
        ret = False
    if len(music_file["artist"]) != 1:
        ret = False
    return ret

# higher level function will save file

def fix_artist_display_mismatch(music_file: AnyMusicFile) -> None:
    """Set artist tag to display artist tag"""
    music_file["artist"] = music_file["display artist"]

def fix_artist_too_many_values(music_file: AnyMusicFile) -> None:
    """Keep only the first artist value"""
    music_file["artist"] = music_file["artist"][0]

def append_to_performers(music_file: AnyMusicFile, performers: list[str]):
    """Append to performers tag"""
    music_file["performers"] = music_file["performers"] + performers

