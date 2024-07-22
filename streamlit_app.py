import streamlit as st
import requests
from datetime import datetime

api_key = st.secrets['API_KEY']


def get_weather(city, api_key):
    base_url ='https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q':city,
        'appid':api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json(), response.status_code


city_name = st.text_input('Enter your city: ')
req, status_code = get_weather(city_name,api_key)



if status_code==200:
    temp = req['main']['temp']
    wind = req['wind']['speed']
    st.write(f'Temperature is {temp} °C')
    st.write(f'Wind speed is {wind} km/h')

elif status_code==404:
    st.write('City not found!')
