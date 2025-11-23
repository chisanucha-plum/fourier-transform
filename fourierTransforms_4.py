import numpy as np
import soundfile as sf

data, sr = sf.read("original.wav")
if data.ndim > 1:
    data = data[:, 0]

F = np.fft.fft(data)
freq = np.fft.fftfreq(len(F), 1/sr)

cutoff = 3000  #  0–3000 Hz
F[np.abs(freq) > cutoff] = 0

output = np.fft.ifft(F).real
output /= np.max(np.abs(output))

sf.write("output_lowpass.wav", output, sr)
