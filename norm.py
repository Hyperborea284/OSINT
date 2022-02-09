from pydub import AudioSegment
import subprocess


def match_target_amplitude(sound, target_dbfs):
    """
    Normaliza o audio
    """

    change_in_dbfs = target_dbfs - sound.dBFS
    return sound.apply_gain(change_in_dbfs)


def normalize():
    sound = AudioSegment.from_file("tester.mp4")
    normalized_sound = match_target_amplitude(sound, -20.0)
    normalized_sound.export("tester02.mp4", format="mp4")
    command = "ffmpeg -i tester02.mp4 -ab 160k -ac 2 -ar 44100 -vn tester02.wav"
    subprocess.call(command, shell=True)