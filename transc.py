import os
import csv
import shutil
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from mixer import mixer


def get_large_audio_transcription(dc_01):
    """
    Fatia o audio e
    extrai o texto do audio
    retorna o arquivo do texto e o audio do texto
    """

    nl = '\n'
    titulo = dc_01.get('titulo')
    prep1 = f'tester02.wav'

    r = sr.Recognizer()

    sound = AudioSegment.from_wav(prep1)
    chunks = split_on_silence(sound,
                              min_silence_len=400,
                              silence_thresh=sound.dBFS -16)

    folder_name = "audio-chunks"

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    score = []
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)

            try:
                text = r.recognize_google(audio_listened, language='pt-BR')

            except sr.UnknownValueError:
                pass

            finally:
                mixer(text, dc_01)
                whole_text += f'{text}{nl}'
                dc_01['frase'] = text

                with open(f"scores/{i}_{titulo}.csv", 'w') as f:
                    w = csv.writer(f)
                    w.writerow(dc_01.keys())
                    w.writerow(dc_01.values())

    shutil.rmtree(folder_name)

    files_to_remove = ['tester.mp4', 'tester02.mp4', 'tester02.wav']
    
    for file in files_to_remove:
        os.remove(file)

    f = open('transcricao.txt', "w")
    f.write(whole_text)
    f.close()

    return score
