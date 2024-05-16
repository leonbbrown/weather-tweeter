import python_weather
from datetime import datetime
from datetime import time

import asyncio
import os
hour_now = datetime.now().strftime("%H") #STR
Forecast_time = ''

forecast = []

async def getweather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
      weather = await client.get('Newcastle upon Tyne')
      print(weather.temperature)
      for daily in weather.daily_forecasts:
         
        for hour in daily.hourly_forecasts:
               forecast.append(hour)
        print(forecast)
        
            
      
      
          
       
asyncio.run(getweather())
