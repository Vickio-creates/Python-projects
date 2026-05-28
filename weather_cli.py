import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    pass

def get_recommendation(temp, condition):
    pass

def main():
    city = input("Enter a city: ")
    get_weather(city)

main()    