import os
import wave

import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, "original.wav")
FILT = os.path.join(BASE, "filtered.wav")


def write_wav(path, data, sr=44100):
    data = np.clip(data, -1, 1)
    data = (data * 32767).astype(np.int16)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(data.tobytes())


def main():
    sr = 44100
    dur = 5.0
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    sig = (
        0.6 * np.sin(2 * np.pi * 440 * t)
        + 0.3 * np.sin(2 * np.pi * 5000 * t)
        + 0.1 * np.sin(2 * np.pi * 12000 * t)
    )

    f = int(0.01 * sr)
    w = np.ones_like(sig)
    w[:f] = np.linspace(0, 1, f)
    w[-f:] = np.linspace(1, 0, f)
    sig *= w
    sig = sig / np.max(np.abs(sig)) * 0.95

    write_wav(ORIG, sig, sr)

    # low-pass via FFT
    spec = np.fft.rfft(sig)
    freqs = np.fft.rfftfreq(sig.size, 1 / sr)
    cutoff = 1000.0
    spec[freqs > cutoff] = 0
    filt = np.fft.irfft(spec, n=sig.size)

    # match level
    def rms(x):
        return np.sqrt(np.mean(x**2))

    scale = rms(sig) / max(rms(filt), 1e-12)
    filt *= scale
    filt = filt / np.max(np.abs(filt)) * 0.95

    write_wav(FILT, filt, sr)
    print("done")


if __name__ == "__main__":
    main()
