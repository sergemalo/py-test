#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt
import numpy as np

print("Pyton version:")
print(sys.version)


def plotFFT(signal, sampleRate):
  sampleLengthSec = 1/sampleRate

  sigFFT = np.fft.fft(signal) / time.shape[0]
  freq = np.fft.fftfreq(time.shape[0], sampleLengthSec)

  fig, (ax0, ax1) = plt.subplots(2, 1)
  ax0.set_title("Time Domain")
  ax0.set(xlabel='Time', ylabel='Signal')
  ax0.plot(time, signal)
  ax1.set_title("Frequency Domain")
  ax1.set(xlabel='Freq (Hz)', ylabel='Amplitude')
  ax1.plot(freq, np.abs(sigFFT))

  plt.show()


sampleRate = 100000
sampleLengthSec = 1/sampleRate

time = np.arange(0, 1, sampleLengthSec)

print(len(time))

f1 = 1000
f2 = 10000
a1=5
a2=10
signal = a1*np.sin(2*np.pi * f1 * time)
signal += a2*np.sin(2*np.pi * f2 * time)
#signal = (0 * time)
 
plotFFT(signal, sampleRate)


#sigFFT = np.fft.fft(signal) / time.shape[0]
#freq = np.fft.fftfreq(time.shape[0], sampleLengthSec)

#firstNegInd = np.argmax(freq < 0)
#freqAxisPos = freq[0:firstNegInd]
#sigFFTPos = 2 * sigFFT[0:firstNegInd]  # *2 because of magnitude of analytic signal

#fig, (ax0, ax1) = plt.subplots(2, 1)
#ax0.plot(time, signal)
#ax1.plot(freq, np.abs(sigFFT))

#plt.show()


# plotting the points
#plt.plot(time, signal)
 
#plt.xlabel('Time')
#plt.ylabel('Amplitude')
 
#plt.title('S = f(t)')
 
# function to show the plot
#plt.show()


#plt.xlabel('Freq')
#plt.ylabel('Amplitude')
 
#plt.title('PSD')

#psd = np.fft.fft(amplitude)
#freq = np.fft.fftfreq(time.shape[-1], sampleLengthSec)
#plt.plot(freq, psd.real)
#plt.show()
