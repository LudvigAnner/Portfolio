import numpy as np
from scipy.fftpack import fft, fftfreq
''' A file containing useful function '''


class analyzer():
    def __init__(self, interval=3):
        self.interval = interval  # Analysis interval in days

    def variance(x):
        return np.var(x)

    def covariance(x, y):
        return np.cov(x, y)

    def mean(x):
        return np.mean(x)

    def rms(x):
        return np.sqrt(np.mean(y**2))

    def fft(x):
        x_fft = fft(x)

    def time_correlation():
        print('Self correlation function')

    def cross_correlation():
        print('Cross correlation function')
