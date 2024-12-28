import numpy as np
import sys

if len(sys.argv) != 1 and len(sys.argv) != 4:
    print("CWS cannot be calculated. Not all required data present.")
elif len(sys.argv) == 4:
    Temp = float(sys.argv[1])
    Wind = float(sys.argv[2])
    Humi = float(sys.argv[3])
else:
    # Define weather metrics in vitro:
    Temp = -10 # deg C
    Wind = 25  # km/h
    Humi = 70  # %

# Define parameters
tau = 13   # Universal temperature parameter
alpha = 0.002
beta  = 0.006
gamma = -0.05
T_hat = Temp - tau

wH = alpha * (T_hat + T_hat*np.tanh(10*T_hat))
wW = beta * (Temp + Temp*np.tanh(-10*Temp)) + gamma

phi = (Temp-tau + Wind*wW + Humi*wH)
print(phi)
import python_weather

import asyncio
import os



