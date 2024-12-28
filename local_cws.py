import python_weather
import os
import numpy as np
import sys
import asyncio

tau = 9   # Universal temperature parameters

if len(sys.argv) < 0 or len(sys.argv) > 3:
    print("Invalid arguments. Please provide a city and/or a date")
elif len(sys.argv) == 2:
    city = sys.argv[1]
    when = 'today'
elif len(sys.argv) == 3:
    city = sys.argv[1]
    when = sys.argv[2]

if when == "today":
    d = 0
elif when == 'tomorrow':
    d = 1

async def getweather() -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        T = weather.temperature
        W = weather.wind_speed
        H = weather.humidity
    return T, W, H

async def getweather_tomorrow() -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        tomorrow_weather = weather[d]
        T = tomorrow_weather.temperature
        W = tomorrow_weather.wind_speed
        H = tomorrow_weather.humidity
    return T, W, H

if when=="today": 
    Temp, Wind, Humi = asyncio.run(getweather())
elif when=='tomorrow':
    Temp, Wind, Humi = asyncio.run(getweather_tomorrow())
        
# Define parameters
alpha = 0.002
beta  = 0.006
gamma = -0.05
T_hat = Temp - tau

wH = alpha * (T_hat + T_hat*np.tanh(10*T_hat))
wW = beta * (Temp + Temp*np.tanh(-10*Temp)) + gamma

phi = round(Temp-tau + Wind*wW + Humi*wH,0)
print(phi)
