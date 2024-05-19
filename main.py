# import the module
import python_weather
from datetime import datetime
import asyncio
import os
import tweepy
import keys


#INDEX 0 = 0
#INDEX 1 = 3
#INDEX 2 = 6
#INDEX 3 = 9
#INDEX 4 = 12
#INDEX 5 = 15
#INDEX 6 = 18
#INDEX 7 = 21

Client = tweepy.Client(
    consumer_key = keys.consumer_key,
    consumer_secret = keys.consumer_secret,
    bearer_token = keys.bearer_token,
    access_token = keys.access_token,
    access_token_secret = keys.access_token_secret
)


hour_now = int(datetime.now().strftime("%H")) #STR
if 22 <= hour_now <= 23:
  index = 0
elif 2 <= hour_now <= 3:
  index = 1
elif 4 <= hour_now <= 6:
  index = 2
elif 7 <= hour_now <= 9:
  index = 3
elif 10 <= hour_now <= 12:
  index = 4
elif 13 <= hour_now <= 15:
  index = 5
elif 16 <= hour_now <= 18:
  index = 6
elif 19 <= hour_now <= 21:
  index = 7
else:
  index = 0

forecast = []
current_forecast = []

async def getweather(index):


  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('NEWCASTLE')
        
    
    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      
      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        forecast.append(hourly)
        
    current_hour = forecast[index]
    time = current_hour.time
    temp = current_hour.temperature
    desc = current_hour.description
    kind = current_hour.kind
    info = f'The temperature in Newcastle Upon Tyne at {time} today is {temp}°C. It is currently {desc} and is {kind}'
    Client.create_tweet(text=info)
    print(f'Successfuly tweeted: {info}')


if __name__ == '__main__':
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather(index))




