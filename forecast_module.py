import requests
class forecast_module:
    def __init__(self,key,base):
        self.api_key = key #"81b502387a57509a24643d6dfc9affb5" 
        self.base_url = base #"http://api.openweathermap.org/data/2.5/weather?"

    def get_forecast(self,city):
        complete_url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(complete_url)
            data = response.json()
            if data.get("cod") == "200":
                time_series = data.get("list", [])
                hours = []
                temperatures = []
                humidities = []
                # 提取未来四个时间点的天气数据
                for i in range(4):
                    hour_data = time_series[i]  # 每个数据点代表3小时的天气
                    hours.append(i * 3)  # 假设我们查询的是从当前时间开始的每3小时一次的预报
                    temperatures.append(hour_data["main"]["temp"])
                    humidities.append(hour_data["main"]["humidity"])
                return hours, temperatures, humidities
            else:
                return [], [], []
        except requests.exceptions.RequestException as e:
            return [], [], []
        
    