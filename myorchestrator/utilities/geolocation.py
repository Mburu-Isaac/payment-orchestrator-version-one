import requests
from datetime import datetime
import pytz



class Location:

    def __init__(
        self, 
        user_ip
    ):
        self.user_ip = user_ip

    def timezoneinfo_cache(self):
        pass

    def get_user_timezone(self):
        
        timezone = None

        try:
            if self.user_ip:
                api_url = f"https://ipapi.co/{self.user_ip}/timezone/"
            else:
                api_url = "https://ipapi.co/timezone/"

            response = requests.get(api_url, timeout=5)
            response.raise_for_status()

            timezone = response.text.strip()

            timezone_object = pytz.timezone(timezone)
            current_time = datetime.now(timezone_object)

            location_info = {
                "timezone": timezone,
                "local_time": current_time,
                "is_valid": True
            }

            return location_info

        except requests.exceptions.Timeout:
            return {"error": "geo-API request timed out"}
        
        except requests.exceptions.RequestException as e:
            return {"error": f"{e}"}

        except pytz.exceptions.UnknownTimeZoneError:
            # if api returns an unexpected string
            return {"error": f"API returned an unknown timezone format: {timezone}"}

        except Exception as error:
            return {f"an unexpected error occured: {error}"}



