# coding=utf-8
import enum
import time


class TimeStatus(enum.Enum):
    MID_NIGHT = 0
    DAY = 1
    NIGHT = 2

    @staticmethod
    def get_status():
        hour_now = TimeStatus.get_hour()
        if hour_now <= 5:
            return TimeStatus.MID_NIGHT
        elif hour_now <= 20:
            return TimeStatus.DAY
        else:
            return TimeStatus.NIGHT

    @staticmethod
    def get_hour():
        return int(time.strftime('%H', time.localtime(time.time())))


class AirType(enum.Enum):
    GOOD = 0
    MODERATE = 1
    LIGHTLY_POLLUTED = 2
    MODERATELY_POLLUTED = 3
    HEAVILY_POLLUTED = 4
    SEVERELY_POLLUTED = 5

    @staticmethod
    def get_air_type(aqi):
        if aqi <= 50:
            return AirType.GOOD
        elif aqi <= 100:
            return AirType.MODERATE
        elif aqi <= 150:
            return AirType.LIGHTLY_POLLUTED
        elif aqi <= 200:
            return AirType.MODERATELY_POLLUTED
        elif aqi <= 300:
            return AirType.HEAVILY_POLLUTED
        else:
            return AirType.SEVERELY_POLLUTED


class WeatherType(enum.Enum):
    SHINE = 'SHINE'
    CLOUDY = 'CLOUDY'
    RAIN = 'RAIN'
    ICE_RAIN = 'ICE_RAIN'
    SNOW = 'SNOW'
    SAND = 'SAND'
    FOGGY_HAZE = 'FOGGY_HAZE'
    WINDY = 'WINDY'
    COLD = 'COLD'
    HOT = 'HOT'
    UNKNOWN = 'UNKNOWN'

    @staticmethod
    def get_weather_type(code):
        if code <= 3:
            return WeatherType.SHINE
        if code <= 9:
            return WeatherType.CLOUDY
        if code <= 18:
            return WeatherType.RAIN
        if code <= 20:
            return WeatherType.ICE_RAIN
        if code <= 25:
            return WeatherType.SNOW
        if code <= 29:
            return WeatherType.SAND
        if code <= 31:
            return WeatherType.FOGGY_HAZE
        if code <= 36:
            return WeatherType.WINDY
        if code == 37:
            return WeatherType.COLD
        if code == 38:
            return WeatherType.HOT
        if code == 99:
            return WeatherType.UNKNOWN