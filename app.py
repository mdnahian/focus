from threading import Thread
from pydub import AudioSegment 
from pydub.playback import play
from audio_filter import noise_reducer
import test
import pyaudio
import wave
import time


enabled = []


CHUNK = 2**16
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		output=True,
		frames_per_buffer=CHUNK)

print p.get_sample_size(FORMAT)



def recordaudio():
	print("recording")

	#frames = []

	#for i in range(0, int(RATE / CHUNK)):
	data = stream.read(CHUNK)
		#frames.append(data)

	with open('modes.txt', 'r') as modes_file:
		if test.from_stream(b''.join(data)) in modes_file.read().split(','):
			stream.write(data, CHUNK)
	#print("* done recording")
	
		


while True:	
	recordaudio()
	#Thread(target=playsound, args=("output.wav",)).start()
