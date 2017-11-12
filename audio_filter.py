import pyaudio
import numpy as np
import scipy.signal


MAX_INT = 32768.0



def noise_reducer(stream, CHUNK):
	fir = np.zeros(CHUNK * 2)
	fir[:(2*CHUNK)] = 1.
	fir /= fir.sum()

	fir_last = fir
	avg_freq_buffer = np.zeros(CHUNK)
	obj = -np.inf
	t = 10

	# initialize sample buffer
	buffer = np.zeros(CHUNK * 2)

	#for i in np.arange(RATE / CHUNK * RECORD_SECONDS):
	# while True:
    # read audio
	audio_data = np.fromstring(stream, dtype=np.int16)
	normalized_data = audio_data / MAX_INT
	freq_data = np.fft.fft(normalized_data)

	# synthesize audio
	buffer[CHUNK:] = np.random.randn(CHUNK)
	freq_buffer = np.fft.fft(buffer)
	freq_fir = np.fft.fft(fir)
	freq_synth = freq_fir * freq_buffer
	synth = np.real(np.fft.ifft(freq_synth))

	# adjust fir
	# objective is to make abs(freq_synth) as much like long-term average of freq_buffer
	MEMORY=100
	avg_freq_buffer = (avg_freq_buffer*MEMORY + np.abs(freq_data)) / 101
	obj_last = obj

	obj = np.real(np.dot(avg_freq_buffer[1:51], np.abs(freq_synth[1:100:2])) / np.dot(freq_synth[1:100:2], np.conj(freq_synth[1:100:2])))
	if obj > obj_last:
	    fir_last = fir
	fir = fir_last.copy()

	# adjust filter in frequency space
	freq_fir = np.fft.fft(fir)
	#t += np.clip(np.random.randint(3)-1, 0, 64)
	t = np.random.randint(100)

	freq_fir[t] += np.random.randn()*.05

	# transform frequency space filter to time space, click-free
	fir = np.real(np.fft.ifft(freq_fir))
	fir[:CHUNK] *= np.linspace(1., 0., CHUNK)**.1
	fir[CHUNK:] = 0


	# move chunk to start of buffer
	buffer[:CHUNK] = buffer[CHUNK:]

	# write audio
	audio_data = np.array(np.round_(synth[CHUNK:] * MAX_INT), dtype=DTYPE)
	return audio_data.tostring()