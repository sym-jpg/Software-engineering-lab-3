"""weather module"""
import requests
import alert_module as a_m
class weather_module:
    def __init__(self,key,base):
        self.api_key = key #"81b502387a57509a24643d6dfc9affb5"
        self.base_url = base #"http://api.openweathermap.org/data/2.5/weather?"

    def get_current_weather(self,city):
        complete_url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(complete_url)
            data = response.json()
            # 检查响应是否包含错误信息
            if data.get("cod") != "404":
                main_data = data.get("main", {})
                weather_data = data.get("weather", [{}])[0]

                # 如果数据中缺少 "main" 或 "weather" 部分，则返回错误信息
                if not main_data or not weather_data:
                    return 0,"Error: Weather data is incomplete."

                temperature = main_data.get("temp", "N/A")
                weather_description = weather_data.get("description", "N/A")

                return temperature,weather_description
            else:
                # 城市没有找到时，API 返回 "cod" = "404"
                return 0,"City not found!"
        except requests.exceptions.RequestException as e:
            return 0,f"Error fetching data: {e}"

    def get_humidity(self,city):
        complete_url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(complete_url)
            data = response.json()
            # 检查响应是否包含错误信息
            if data.get("cod") != "404":
                main_data = data.get("main", {})
                weather_data = data.get("weather", [{}])[0]

                # 如果数据中缺少 "main" 或 "weather" 部分，则返回错误信息
                if not main_data or not weather_data:
                    return "Error: Weather data is incomplete."
                humidity = data['main']['humidity']
                return humidity
            else:
                # 城市没有找到时，API 返回 "cod" = "404"
                return "City not found!"
        except requests.exceptions.RequestException as e:
            return f"Error fetching data: {e}"

    def get_multi_city_weather(self, city_list):
        for city in city_list:
            self.get_current_weather(city)

    def get_alert(self,city,temp):
        complete_url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        # 获取降雨量和风速
        rain = data.get("rain", {}).get("1h", 0)  # 最近1小时降雨量，默认为0
        wind_speed = data.get("wind", {}).get("speed", 0)  # 风速
        alert = a_m.alert_module()
        return alert.send_extreme_weather_alert(temp,wind_speed,rain)
