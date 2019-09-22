from python_speech_features import mfcc
from python_speech_features import delta
import numpy
from python_speech_features import logfbank
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

(rate, sig) = wav.read("F://University//国创//ProjectLog//基于DTW与标准语音对比//00f0204f_nohash_1.wav")
mfcc_feat = mfcc(sig, rate, winfunc=numpy.hamming)
print(sig)
""" plt.plot(sig)
plt.show() """
plt.plot(mfcc_feat[1])
plt.show()
d_mfcc_feat = delta(mfcc_feat, 2)
""" plt.plot(d_mfcc_feat)
plt.show() """
fbank_feat = logfbank(sig,rate)
print(mfcc_feat.ndim)
print(mfcc_feat.shape)
