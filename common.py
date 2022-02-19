import numpy as np

def gen_sine(timespace, freq, amp, offset=0, phase=0):
    return (amp * np.sin((2. * np.pi * freq * timespace)+phase)) + offset

def downsample(wave, data):
    """Dummy down-sample, just an average filter"""

    rateratio = int(len(wave) / len(data))

    for i in range(int(len(wave)/rateratio)):
        for j in range(rateratio):
            data[i] += wave[(i*rateratio) + j]
        data[i] = data[i] / rateratio