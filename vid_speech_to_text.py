import soundfile as sf
import os
import tensorflow as tf
import tensorflow_hub as hub
import subprocess
import ffmpeg
import librosa
from pydub import AudioSegment
from google.colab import files
from moviepy.editor import AudioFileClip

from wav2vec2 import Wav2Vec2Processor

class SpeechToText:

    def __init__(self):
        self.model = hub.KerasLayer("saved-model")
        self.tokenizer = Wav2Vec2Processor(is_tokenizer=True)
        self.processor = Wav2Vec2Processor(is_tokenizer=False)
        self.AUDIO_MAXLEN = 246000
        self.DO_PADDING = True

    @tf.function(jit_compile=True)
    def tf_forward(self, speech):
        tf_out = self.model(speech, training=False)
        return tf.squeeze(tf.argmax(tf_out, axis=-1))

    def preprocess_speech(self, audio):
        audio = tf.constant(audio, dtype=tf.float32)
        audio = self.processor(audio)[None]
        if self.DO_PADDING:
            audio = audio[:, :self.AUDIO_MAXLEN]
            padding = tf.zeros((audio.shape[0], self.AUDIO_MAXLEN - audio.shape[1]), dtype=audio.dtype)
            audio = tf.concat([audio, padding], axis=-1)
        return audio

    def webm_2_wav(self, name):
        wav = AudioSegment.from_file(name, format = "webm")
        getaudio = wav.export(name.split(".")[:-1][0]+".wav", format="wav")
        return getaudio

    def mp4_2_wav(self, name):
        input_file = name
        output_file = name.split(".")[:-1][0]+".wav"
        subprocess.call(['ffmpeg', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '2', output_file])
        return output_file

    def mov_2_wav(self, name):
        input_file = name
        output_file = name.split(".")[:-1][0]+".wav"
        audio_clip = AudioFileClip(input_file)
        audio_clip.write_audiofile(output_file)
        return output_file

    def converter(self, uploaded):
        if list(uploaded.keys())[0].split(".")[-1] == "wav":
            output_file = list(uploaded.keys())[0]
            return output_file
        elif list(uploaded.keys())[0].split(".")[-1] == "flac":
            output_file = list(uploaded.keys())[0]
            return output_file
        elif list(uploaded.keys())[0].split(".")[-1] == "webm":
            output_file = self.webm_2_wav(list(uploaded.keys())[0])
            return output_file
        elif list(uploaded.keys())[0].split(".")[-1] == "mp4":
            output_file = self.mp4_2_wav(list(uploaded.keys())[0])
            return output_file
        elif list(uploaded.keys())[0].split(".")[-1] == "mov":
            output_file = self.mov_2_wav(list(uploaded.keys())[0])
            return output_file
    def split_wav(self, audio):
        input_file = audio
        segment_duration = 15000
        audio = AudioSegment.from_wav(input_file)
        segments = []
        for i in range(0, len(audio), segment_duration):
            segment = audio[i:i+segment_duration]
            segments.append(segment)
        names_of_segments = []
        for i, segment in enumerate(segments):
            output_file = os.path.splitext(input_file)[0] + f"_segment{i}.wav"
            segment.export(output_file, format="wav")
            names_of_segments.append(output_file)
        return names_of_segments

    def preprocess_audio(self, output_file):
        speech, samplerate = sf.read(output_file)
        if len(speech.shape) > 1: 
            speech = speech[:,0] + speech[:,1]
        if samplerate != 16000:
            speech = librosa.resample(speech, orig_sr = samplerate, target_sr = 16000)
        return speech

    def process(self):
        uploaded = files.upload()
        output_file = self.converter(uploaded)
        wavs = self.split_wav(output_file)
        preprocessed_wavs = [self.preprocess_audio(wav) for wav in wavs]

        script = ""
        for audio in preprocessed_wavs:
            audio = self.preprocess_speech(audio)
            tf_out = self.tf_forward(audio)
            script = script + self.tokenizer.decode(tf_out.numpy().tolist())
        return script
