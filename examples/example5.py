from threading import Thread
import pyaudio
import numpy as np

CHUNK = 2**9
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True, output=True,
              frames_per_buffer=CHUNK)

while True: #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    Thread(target=stream.write(data, CHUNK)).start()
    #peak=np.average(np.abs(data))*2
    #bars="#"*int(50*peak/2**16)
    #print bars

stream.stop_stream()
stream.close()
p.terminate()
