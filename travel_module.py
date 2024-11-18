import weather_module as w_m
class travel_module:
    def __init__(self):
        return
        
    def get_travel_weather(self,start_city,end_city):
        start=w_m.Weather_module("81b502387a57509a24643d6dfc9affb5","http://api.openweathermap.org/data/2.5/weather?")
        end=w_m.Weather_module("81b502387a57509a24643d6dfc9affb5","http://api.openweathermap.org/data/2.5/weather?")
        start_temp,start_des=start.get_current_weather(start_city)
        end_temp,end_des=end.get_current_weather(end_city)
        return start_temp,end_temp,start_des,end_des
    
    def get_travel_advice(self,start_city,end_city):
        s_t,e_t,s_d,e_d=self.get_travel_weather(start_city,end_city)
        weather_alerts=[]
        weather_alerts.append(f"{start_city} : {s_d}")
        if s_t > 35:
            weather_alerts.append("高温预警：避免长时间户外活动。")
        elif s_t < 0:
            weather_alerts.append("低温预警：注意保暖，防止冻伤。")
        else:
            weather_alerts.append("起始地点气候较适宜")
        weather_alerts.append(f"{end_city} : {e_d}")
        if e_t > 35:
            weather_alerts.append("高温预警：避免长时间户外活动。")
        elif e_t < 0:
            weather_alerts.append("低温预警：注意保暖，防止冻伤。")
        else:
            weather_alerts.append("目的地点气候较适宜")
        return weather_alerts      

