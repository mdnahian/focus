from threading import Thread
from pydub import AudioSegment 
from pydub.playback import play
import test
import pyaudio
import wave
import time

CHUNK = 2**18
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		output=True,
		frames_per_buffer=CHUNK)

#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#wf.setnchannels(CHANNELS)
#wf.setsampwidth(p.get_sample_size(FORMAT))
#wf.setframerate(RATE)


def playsound(file_name):
	while True:
		test.from_file("output.wav")
        	#play(AudioSegment.from_wav(file_name))


Thread(target=playsound, args=("output.wav",)).start()





def recordaudio():
	print("* recording")

	#frames = []

	#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	    #frames.append(data)
	stream.write(data, CHUNK)
	print("* done recording")

	#stream.stop_stream()
	#stream.close()
	#p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(data))
	wf.close()

	#test.from_file("output.wav")
	#Thread(target=playsound, args=("output.wav",)).start()



while True:	
	recordaudio()
	#Thread(target=playsound, args=("output.wav",)).start()
