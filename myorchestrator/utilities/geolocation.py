import requests
from datetime import datetime, timedelta
import pytz
from zoneinfo import ZoneInfo
import time


class Location:

    def __init__(self, user_ip):

        self.user_ip = user_ip
        self.cached_timezoneinfo = None
        # self.location_info = self.get_user_timezone()
        # self.zoneinfo = self.location_info["local_time"]
        # self.cache_timeout = self.zoneinfo + timedelta(minutes=60)

    def timezoneinfo_cache(self):

        if self.cached_timezoneinfo is None:
            pass

    def get_timezone(self):

        self.cache_timezoneinfo()

        timezone = None

        try:
            if self.user_ip:
                api_url = f"https://ipapi.co/{self.user_ip}/timezone/"
            else:
                api_url = "https://ipapi.co/timezone/"

            response = requests.get(api_url)  # timeout=5)
            response.raise_for_status()

            timezone = response.text.strip()

            timezone_object = pytz.timezone(timezone)
            current_time = datetime.now(timezone_object)

            location_info = {
                "timezone": timezone,
                "localTime": current_time,
            }

            self.cached_timezoneinfo = location_info

            return self.cached_timezoneinfo

        except requests.exceptions.Timeout:
            return {"error": "geo-API request timed out"}

        except requests.exceptions.RequestException as e:
            return {"error": f"{e}"}

        except pytz.exceptions.UnknownTimeZoneError:
            # if api returns an unexpected string
            return {"error": f"API returned an unknown timezone format: {timezone}"}

        except Exception as error:
            return {f"an unexpected error occured: {error}"}

        # else:
        # return self.cache_timezone_info()




# info = {
#     "timezone": "Africa/Nairobi",
#     "localTime": 
# }

# striffed_time = info.get("localTime").strftime("%H:%M")
# print(striffed_time)