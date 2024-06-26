import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz
from scipy.fft import fft
Fs = 3000
t = np.arange(0, 2, 1/Fs)
noiseAmplitude = np.random.randint(1, 6)
noise = noiseAmplitude * np.random.rand(len(t))
y1 = 5 * np.sin(2 * np.pi * 60 * t) + noise
y2 = 2.5 * np.sin(2 * np.pi * 100 * t) + noise
y3 = 1.2 * np.sin(2 * np.pi * 150 * t) + noise
y4 = 7 * np.sin(2 * np.pi * 250 * t) + noise
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.plot(t, y1, 'r')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 1')
plt.subplot(2, 2, 2)
plt.plot(t, y2, 'y')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 2')
plt.subplot(2, 2, 3)
plt.plot(t, y3, 'g')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 3')
plt.subplot(2, 2, 4)
plt.plot(t, y4, 'c')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 4')
plt.tight_layout()
plt.show()
y = y1 + y2 + y3 + y4
plt.figure()
plt.plot(t, y1, 'r', label='Signal 1')
plt.plot(t, y2, 'y', label='Signal 2')
plt.plot(t, y3, 'g', label='Signal 3')
plt.plot(t, y4, 'c', label='Signal 4')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Overall Signal')
plt.legend()
plt.show()
L = len(y)
n = 2**int(np.ceil(np.log2(L)))
Y = fft(y, n)
f = Fs * np.arange(0, n//2 + 1) / n
P = np.abs(Y / n)
Y_val = P[:n//2 + 1]
plt.figure()
plt.plot(f, Y_val)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Frequency response of actual signal')
plt.show()
N = 30   # Order
Fpass = 100  # Passband Frequency
Fstop = 120  # Stopband Frequency
b1 = firwin(N + 1, Fpass/(Fs/2), window='hamming')
LPFSignal = lfilter(b1, 1, y)
plt.figure()
plt.plot(t, LPFSignal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('LPF Signal')
plt.show()

LPFSignalFFT = fft(LPFSignal, n)
LPFValue = np.abs(LPFSignalFFT / n)
AmpOfLPFSignal = LPFValue[:n//2 + 1]
plt.figure()
plt.plot(f, AmpOfLPFSignal)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Low Pass Filtered Signal')
plt.show()
N = 60   # Order
Fstop1 = 25   # First Stopband Frequency
Fpass1 = 50   # First Passband Frequency
Fpass2 = 260  # Second Passband Frequency
Fstop2 = 285  # Second Stopband Frequency
b2 = firwin(N + 1, [Fpass1, Fpass2], pass_zero=False, fs=Fs)
BPFSignal = lfilter(b2, 1, y)
plt.figure()
plt.plot(t, BPFSignal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('BPF Signal')
plt.show()
BPFSignalFFT = fft(BPFSignal, n)
BPFValue = np.abs(BPFSignalFFT / n)
AmpOfBPFSignal = BPFValue[:n//2 + 1]
plt.figure()
plt.plot(f, AmpOfBPFSignal)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Band Pass Filtered Signal')
plt.show()
plt.figure(figsize=(12, 10))
plt.subplot(3, 2, 1)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Actual Signal in Time Domain')
plt.subplot(3, 2, 2)
plt.plot(f, Y_val)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Actual Signal in Frequency Domain')
plt.subplot(3, 2, 3)
plt.plot(t, LPFSignal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Low Pass Filtered Signal in Time Domain')
plt.subplot(3, 2, 4)
plt.plot(f, AmpOfLPFSignal)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Low Pass Filtered Signal in Frequency Domain')
plt.subplot(3, 2, 5)
plt.plot(t, BPFSignal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Band Pass Filtered Signal in Time Domain')
plt.subplot(3, 2, 6)
plt.plot(f, AmpOfBPFSignal)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Band Pass Filtered Signal in Frequency Domain')
plt.tight_layout()
plt.show()

