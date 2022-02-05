import numpy as np
from scipy.io.wavfile import write
from scipy import signal

# Create a few constants
# The target sample rate is given below.
# We will take this as a reference but operate on a
# different higher sample rate. We define how higher
# using the rate-ratio constant. The higher the ratio
# the more samples there will be, and thus, more
# processing time.
samplerate = 44600
rateratio = 10
slength = 6

fs1 = 1000  # Frequency of tone 1
fs2 = fs1/2 # Frequency of tone 2
fsB = 90    # Frequency of tone 3 (bass)

# The samples on the synthesis space is given by the sample rate
# times the rate-ratio
synthSamples = rateratio * samplerate * slength
samples = samplerate * slength

# Create a time-base, the x values for our equations
# tsynth exists on the synthesis sampling space
tsynth = np.linspace(0., slength, synthSamples)
data = np.linspace(0., slength, samples)

# Get the maximum amplitude possible in this representation
amplitude = np.iinfo(np.int16).max

# Generate the waves, take them to half the amplitude.
wave1 = 0.5 * amplitude * np.sin(2. * np.pi * fs1 * tsynth)
wave2 = 0.5 * amplitude * np.sin(2. * np.pi * fs2 * tsynth)
mod = signal.square(2 * np.pi * 1 * tsynth) + 1
bass = 0.5 * amplitude * np.sin(2. * np.pi * fsB * tsynth) * mod

# Add all the waves
wave3 = wave1 + wave2 + bass

# Dummy down-sample, just an average filter
for i in range(int(len(wave3)/rateratio)):
    for j in range(rateratio):
        data[i] += wave3[(i*rateratio) + j]
    data[i] = data[i] / rateratio

write("example.wav", samplerate, data.astype(np.int16))