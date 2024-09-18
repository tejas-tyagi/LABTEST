import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter ,filtfilt;

np.random.seed(0)
minutes = np.range(1440)
base_aqi = np.array([])
noise = np.random.normal(0,5,minutes)
aqireadings = base_aqi + noise

def lowpassfilter(data,cutfre=0.05,order=4):
    b,a = butter(order,cutfre,btype=low,analog=False)
    return filtfilt(b,a,data)

smoothaqi = lowpassfilter(aqireadings)

def computeavg(data):
    return np.mean(data)

mean = computeavg(smoothaqi)

plt.figure(figsize=(12,6))
plt.plot(aqireadings,label="noisy aqi data", alpha=0.5)

plt.plot(smoothaqi,label="smooth aqi data",linewidh=2)

plt.scatter(np.arrange(0,minutes,60),mean,color=red,label="hourly averages")

