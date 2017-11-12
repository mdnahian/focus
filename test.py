#from pyAudioAnalysis import audioTrainTest as aT
#aT.featureAndTrain(["data/music","data/speech"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
#aT.fileClassification("e.wav", "svmSMtemp","svm")

#from sys import argv
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT
#script, filename = argv
isSignificant = 0.8 #try different values.


def from_stream(stream):
	# P: list of probabilities
	Result, P, classNames = aT.streamClassification(stream, "svmModel", "svm")
	winner = np.argmax(P) #pick the result with the highest probability value.

	# print Result
	# print classNames
	# print winner

	#is the highest value found above the isSignificant threshhold? 
	if P[winner] > isSignificant :
	  print("Sound is in category: " + classNames[winner] + ", with probability: " + str(P[winner]))
	  return classNames[winner]
	else :
	  print("Can't classify sound: " + str(P))

	return None



def from_file(filename):
	# P: list of probabilities
	Result, P, classNames = aT.fileClassification(filename, "svmModel", "svm")
	winner = np.argmax(P) #pick the result with the highest probability value.

	# print Result
	# print classNames
	# print winner

	#is the highest value found above the isSignificant threshhold? 
	if P[winner] > isSignificant :
	  print("Sound is in category: " + classNames[winner] + ", with probability: " + str(P[winner]))
	else :
	  print("Can't classify sound: " + str(P))