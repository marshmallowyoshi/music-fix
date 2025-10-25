import pathlib
import wave

import ffmpy


def generate_base_wav(filepath: pathlib.Path):
    """Create a 1-second silent WAV file at the given filepath."""
    data = [0] * 44100  # 1 second of silence at 44.1kHz
    wav_file = wave.open(str(filepath), "wb")
    wav_file.setnchannels(1)  # mono
    wav_file.setsampwidth(2)  # 2 bytes per sample
    wav_file.setframerate(44100)  # 44.1kHz
    wav_file.writeframes(bytearray(data))
    wav_file.close()


def convert_to_new_ext(filepath: pathlib.Path, new_ext: str) -> pathlib.Path:
    """Convert the given audio file to a new extension using ffmpy."""
    new_filepath = filepath.with_suffix(new_ext)
    ff = ffmpy.FFmpeg(inputs={str(filepath): None}, outputs={str(new_filepath): None})
    ff.run()
    return new_filepath
