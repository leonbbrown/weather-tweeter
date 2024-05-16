# import the module
import python_weather

import asyncio
import os
index = 6

forecast = []
current_forecast = []

async def getweather(index):


  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('NEWCASTLE')
    
    # returns the current day's forecast temperature (int)
    print(weather.temperature)
    
    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      
      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        forecast.append(hourly)
        
    current_hour = forecast[index]
    print(current_hour)
    time = current_hour.time
    temp = current_hour.temperature
    desc = current_hour.description
    kind = current_hour.kind
    print(time)
    print(temp)
    print(desc)
    print(kind)
    info = f'The temperature in Newcastle Upon Tyne at {time} today is {temp}°C. It is currently {desc} and is {kind}'
    print(info)

    



          
    
          
       

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather(index))

#INDEX 0 = 0
#INDEX 1 = 3
#INDEX 2 = 6
#INDEX 3 = 9
#INDEX 4 = 12
#INDEX 5 = 15
#INDEX 6 = 18
#INDEX 7 = 21



