import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from common import downsample
from common import gen_sine

# Get the maximum amplitude possible in this representation
amplitude = np.iinfo(np.int16).max

def generate_gains(tspace, amp):
    phases = [0,np.pi/2,-np.pi,(6*np.pi/4)]
    gains = []
    for phase in phases:
        mod = gen_sine(tspace, 1/2, amp,amp, phase)
        gains.append(mod)
    return gains

def plot_gains(x, gains):
    for gain in gains:
        # plotting the points
        plt.plot(x, gain)
        # function to show the plot
    plt.show()

# Create a few constants
samplerate = 44600 # Sampling rate for end file
rateratio = 10     # Up-sampling ratio for synthesis
slength = 8        # Length of clip

fs1 = 1000  # Frequency of the vectors
fs2 = 1500
fs3 = 700
fs4 = 400

# The samples on the synthesis space is given by the sample rate
# times the rate-ratio
synthSamples = rateratio * samplerate * slength
samples = samplerate * slength

# Create a time-base, the x values for our equations
# tsynth exists on the synthesis sampling space
tsynth = np.linspace(0., slength, synthSamples)
data = np.linspace(0., slength, samples)

# Generate the waves, take them to half the amplitude.
wave1 = gen_sine(tsynth, fs1, 0.25 * amplitude)
wave2 = gen_sine(tsynth, fs2, 0.25 * amplitude)
wave3 = gen_sine(tsynth, fs3, 0.25 * amplitude)
wave4 = gen_sine(tsynth, fs4, 0.25 * amplitude)

waves = [wave1, wave2, wave3, wave4]

gains = generate_gains(tsynth, amplitude)
# plot_gains(tsynth,gains)

# Vector modulate
for i in range(len(waves)):
    waves[i] = (waves[i] * gains[i]) / amplitude

# Add all the waves
mix = np.zeros(len(tsynth))
for wave in waves:
    mix += wave

downsample(mix, data)

write("example.wav", samplerate, data.astype(np.int16))