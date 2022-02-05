import numpy as np
from scipy.io.wavfile import write
from scipy import signal

samplerate = 44600; fs = 1000
rateratio = 2
slength = 6
synthSamples = rateratio * samplerate * slength
samples = samplerate * slength

tsynth = np.linspace(0., slength, synthSamples)
data = np.linspace(0., slength, samples)

amplitude = np.iinfo(np.int16).max

wave1 = 0.5 * amplitude * np.sin(2. * np.pi * fs * tsynth)
wave2 = 0.5 * amplitude * np.sin(2. * np.pi * fs/2 * tsynth)
bass = 0.5 * amplitude * np.sin(2. * np.pi * 90 * tsynth) * signal.square(2 * np.pi * 6 * tsynth)


wave3 = wave1 + wave2 + bass

# Dummy filter
for i in range(int(len(wave3)/rateratio)):
    for j in range(rateratio):
        data[i] += wave3[(i*rateratio) + j]
    data[i] = data[i] / rateratio

write("example.wav", samplerate, data.astype(np.int16))