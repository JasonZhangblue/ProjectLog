from python_speech_features import mfcc
from python_speech_features import delta
import numpy as np
from python_speech_features import logfbank
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from numpy import array, zeros, full, argmin, inf, ndim
from scipy.spatial.distance import cdist
from math import isinf,sqrt
import dtw


def dtw(x, y, warp=1, w=inf, s=1.0):
    #使用其他的代码对dtw进行了初步的实现，下一步是自己写该算法的代码
    assert len(x)
    assert len(y)
    assert isinf(w) or (w >= abs(len(x) - len(y)))
    assert s > 0

    
    r, c = len(x), len(y)
    if not isinf(w):
        D0 = full((r + 1, c + 1), inf)
        for i in range(1, r + 1):
            D0[i, max(1, i - w):min(c + 1, i + w + 1)] = 0
        D0[0, 0] = 0
    else:
        D0 = zeros((r + 1, c + 1))
        D0[0, 1:] = inf
        D0[1:, 0] = inf
    D1 = D0[1:, 1:]  # view
    for i in range(r):
        for j in range(c):
            if (isinf(w) or (max(0, i - w) <= j <= min(c, i + w))):
                D1[i, j] = np.linalg.norm(x[i]-y[i])
    C = D1.copy()
    jrange = range(c)
    for i in range(r):
        if not isinf(w):
            jrange = range(max(0, i - w), min(c, i + w + 1))
        for j in jrange:
            min_list = [D0[i, j]]
            for k in range(1, warp + 1):
                i_k = min(i + k, r)
                j_k = min(j + k, c)
                min_list += [D0[i_k, j] * s, D0[i, j_k] * s]
            D1[i, j] += min(min_list)
    if len(x) == 1:
        path = zeros(len(y)), range(len(y))
    elif len(y) == 1:
        path = range(len(x)), zeros(len(x))
    return D1[-1, -1] / sum(D1.shape),D1
def dtw_test(mfcc_standard,mfcc_test):
    #使用动态时间规整对两者的mfcc特征进行一个比较，并通过评分公式给出评分
    M,N=len(mfcc_standard),len(mfcc_test)
    print(M,N)
    cost=np.zeros((M,N))
    for m in range(0,M):
        for n in range(0,N):
            d[m,n]=np.linalg.norm(mfcc_standard[m],mfcc_test[n])

def distance(x,y):
    return sqrt(x*x+y*y)
if __name__==  "__main__":

    (rate, sig) = wav.read(
        "F://University//国创//ProjectLog//基于DTW与标准语音对比//00f0204f_nohash_1.wav")
    (rate_test, sig_test) = wav.read(
        "F://University//国创//ProjectLog//基于DTW与标准语音对比//0c2d2ffa_nohash_0.wav")
    """ plt.plot(sig_test) """
    mfcc_feat = mfcc(sig, rate, winfunc=np.hamming)
    mfcc_feat_test = mfcc(sig_test, rate_test, winfunc=np.hamming)
    d_mfcc_feat = delta(mfcc_feat, 2)
    d_mfcc_feat_test = delta(mfcc_feat_test, 2)
    fbank_feat = logfbank(sig_test, rate_test)
    plt.plot(d_mfcc_feat)
    a=np.array(mfcc_feat)
    print(a)
    print(np.shape(mfcc_feat))
    #通过DTW比较两个语音的相似程度
    a,D1=dtw(mfcc_feat, mfcc_feat_test,
                 warp=1,w=inf,  s=1.0)
    print(a)
    plt.plot(D1)
    plt.show()
