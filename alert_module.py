

class alert_module:
    def __init__(self):
        pass

    def send_extreme_weather_alert(self,temp,wind,rain):
        weather_alerts = []
        if temp > 35:
            weather_alerts.append("高温预警：避免长时间户外活动。")
        elif temp < 0:
            weather_alerts.append("低温预警：注意保暖，防止冻伤。")
        
        if wind > 15:
            weather_alerts.append("大风预警：注意安全，避免户外高空活动。")
        
        if rain > 50:
            weather_alerts.append("暴雨预警：谨防积水和路滑，减少出行。")

        return weather_alerts