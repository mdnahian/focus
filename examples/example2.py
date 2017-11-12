from threading import Thread
from pydub import AudioSegment
from pydub.playback import play




def playsound(file_name):
	play(AudioSegment.from_wav(file_name))




#Load an audio file
myAudioFile = "sound.wav"
sound1 = AudioSegment.from_file(myAudioFile, format="wav")

#Invert phase of audio file
sound2 = sound1.invert_phase()

sound2.export("sound3.wav", format="wav")

thread = Thread(target=playsound, args=("sound.wav",))
thread2 = Thread(target=playsound, args=("sound3.wav",))
thread.start()
thread2.start()




#Merge two audio files
#combined = sound1.overlay(sound2)

#Export merged audio file
#combined.export("sound2.wav", format="wav")

#Play audio file :
#should play nothing since two files with inverse phase cancel each other
#mergedAudio = AudioSegment.from_wav("outAudio.wav")
#play(mergedAudio)
