"""
ui.py
"""
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import weather_module as w_m
import forecast_module as f_m
import travel_module as t_m
import user_module as u_m
import customization_module as c_m

def process_log_in(temp_user,base):
    """process log in function"""
    def confirm():
        user_name = user_name_entry.get()
        pswd = psw_entry.get()
        log_success=temp_user.log_in(user_name,pswd)
        if log_success:
            login_window.destroy()
            base.deiconify()
        else:
            error_label.place(relx=0.0,rely=0.0)

    def register():
        user_name = user_name_entry.get()
        pswd = psw_entry.get()
        temp_user.sign_up(user_name,pswd)
        log_success=True
        if log_success:
            login_window.destroy()
            base.deiconify()
        else:
            error_label.place(relx=0.0,rely=0.0)
    base.withdraw()
    login_window = tk.Toplevel(base)
    login_window.title("User")
    login_window.geometry("500x500")
    login_window.resizable(0,0)
    log_label = ttk.Label(login_window, text="请登录:")
    log_label.place(relx=0.45,rely=0.25)
    error_label = ttk.Label(login_window, text="错误的用户名或密码，请重新输入")
    error_label.place_forget()

    # user_name
    usr_name_label = ttk.Label(login_window, text="用户名:")
    usr_name_label.place(relx=0.18,rely=0.35)
    user_name_entry = ttk.Entry(login_window,width=30, justify="center")
    user_name_entry.place(relx=0.3,rely=0.35)

    # pswd
    psw_label = ttk.Label(login_window, text="密码:")
    psw_label.place(relx=0.18,rely=0.45)
    psw_entry = ttk.Entry(login_window,width=30, justify="center")
    psw_entry.place(relx=0.3,rely=0.45)

    #login_button
    login_button = ttk.Button(login_window, text="确认",command=confirm)
    login_button.place(relx=0.3,rely=0.55)

    #signup_button
    signup_button = ttk.Button(login_window, text="注册",command = register)
    signup_button.place(relx=0.52,rely=0.55)

    user_name_entry = ttk.Entry(login_window,width=30, justify="center")
    user_name_entry.place(relx=0.3,rely=0.35)

def change_city():
    """change city"""
    city_button.place_forget()
    city_entry.place(relx=0.6, rely=0.0)
    confirm_button.place(relx=0.83, rely=0.0)

def show_weather(city):
    """change weather"""
    if city:
        key="81b502387a57509a24643d6dfc9affb5"
        base="http://api.openweathermap.org/data/2.5/weather?"
        weather_module=w_m.Weather_module(key,base)
        temp,wea_des = weather_module.get_current_weather(city)
        humi=weather_module.get_humidity(city)
        alert=weather_module.get_alert(city,temp)
        # 绘制未来四小时天气的图表
        plot_forecast(city)
        if not alert:
            alert=["None"]
        optional = "\nAlert:"+ "\n".join(alert)
        temp_info=f"Temperature: {temp}°C\n"
        humi_info=f"Humidity: {humi}%\n"
        des_info=f"Description: {wea_des.capitalize()}"
        weather_info=temp_info+humi_info+des_info
        if ENABLE_ALERT:
            weather_info=weather_info+optional
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "Unable to get location or city name.")

def plot_forecast(city):
    """plot forecast"""
    key="81b502387a57509a24643d6dfc9affb5"
    base="http://api.openweathermap.org/data/2.5/forecast?"
    forecast_module=f_m.Forecast_module(key,base)
    hours, temperatures, humidities = forecast_module.get_forecast(city)
    if hours and temperatures and humidities:
        # 创建一个 Figure 对象
        fig = Figure(figsize=(5, 4), dpi=100)
        ax1 = fig.add_subplot(111)

        # 绘制温度折线图
        ax1.plot(hours, temperatures, 'b-', label="Temperature (°C)")
        ax1.set_xlabel("Hours from Now")
        ax1.set_ylabel("Temperature (°C)", color='tab:blue')
        ax1.tick_params(axis='y', labelcolor='tab:blue')

        # 创建第二个 y 轴，绘制湿度折线图
        ax2 = ax1.twinx()
        ax2.plot(hours, humidities, 'g-', label="Humidity (%)")
        ax2.set_ylabel("Humidity (%)", color='tab:green')
        ax2.tick_params(axis='y', labelcolor='tab:green')

        fig.tight_layout()

        # 将图表嵌入到 Tkinter 窗口
        new_canvas = FigureCanvasTkAgg(fig, master=forecast_frame)
        new_canvas.draw()
        new_canvas.get_tk_widget().grid(row=1, column=1, padx=10, pady=10, sticky='w')
    else:
        messagebox.showerror("Error", "Unable to retrieve forecast data.")

def yes():
    """confirm change city"""
    city = city_entry.get()
    show_weather(city)
    city_button.config(text=city,width=10)
    city_button.place(relx=0.6, rely=0.0)
    city_entry.place_forget()
    confirm_button.place_forget()

def user_widget():
    """create a user widget"""
    def back():
        user_window.destroy()
        root.deiconify()

    def change_l():
        if not l_switch_var.get():
            cus.set_layout("on")
        else:
            cus.set_layout("off")

    def change_n():
        if not n_switch_var.get():
            cus.set_notification("on")
        else:
            cus.set_notification("off")

    def change_a():
        if not a_switch_var.get():
            cus.set_extreme_alert("on")
        else:
            cus.set_extreme_alert("off")
    def c_c():
        c_content=c_entry.get()
        cus.set_color(c_content)
        style.configure("TButton",  foreground=c_content, font=("Arial", 12))
        style.configure("TLabel",  foreground=c_content, font=("Arial", 12))
        style.configure("TEntry",  foreground=c_content, font=("Arial", 12))

    def b_c():
        b_content=b_entry.get()
        cus.set_background(b_content)
        new_image = Image.open(b_content).resize((800, 600))
        new_photo = ImageTk.PhotoImage(new_image)
        # 更新 Canvas 上的图片
        canvas.itemconfig(bg_image_item, image=new_photo)
        canvas.image = new_photo
    root.withdraw()
    user_window = tk.Toplevel(root)
    user_window.title("User")
    user_window.geometry("600x500")
    user_window.resizable(0,0)
    un_label=ttk.Label(user_window, text=f"用户: {usr.username}", font=("Arial", 16),)
    un_label.place(relx=0.4, rely=0.1)
    c_label=ttk.Label(user_window,text="Change Color:",)
    c_label.place(relx=0.2,rely=0.3)
    c_entry=ttk.Entry(user_window,width=16, font=("Arial", 14),   justify="center",)
    c_entry.place(relx=0.5,rely=0.3)
    c_confirm=ttk.Button(user_window,text=chr(8730), command=c_c,)
    c_confirm.place(relx=0.81,rely=0.3)
    l_label=ttk.Label(user_window,text="Change Layout:")
    l_switch_var = tk.BooleanVar(value=False)
    l_label.place(relx=0.2,rely=0.4)
    l_switch=ttk.Checkbutton(user_window, variable=l_switch_var, command=change_l)
    l_switch.place(relx=0.9,rely=0.4)
    n_label=ttk.Label(user_window,text="Enable Notification:")
    n_label.place(relx=0.2,rely=0.5)
    n_switch_var = tk.BooleanVar(value=False)
    n_label.place(relx=0.2,rely=0.5)
    n_switch=ttk.Checkbutton(user_window, variable=n_switch_var, command=change_n)
    n_switch.place(relx=0.9,rely=0.5)
    a_label=ttk.Label(user_window,text="Enable Alert:")
    a_label.place(relx=0.2,rely=0.6)
    a_switch_var = tk.BooleanVar(value=False)
    a_label.place(relx=0.2,rely=0.6)
    a_switch=ttk.Checkbutton(user_window, variable=a_switch_var, command=change_a)
    a_switch.place(relx=0.9,rely=0.6)
    b_label=ttk.Label(user_window,text="Change Background:")
    b_label.place(relx=0.2,rely=0.7)
    b_entry=ttk.Entry(user_window,width=16, font=("Arial", 14),  justify="center")
    b_entry.place(relx=0.5,rely=0.7)
    b_confirm=ttk.Button(user_window,text=chr(8730), command=b_c)
    b_confirm.place(relx=0.81,rely=0.7)

    back_button=ttk.Button(user_window,text="back", command=back)
    back_button.place(relx=0.0,rely=0.0)

def travel():
    """travel function"""
    def back():
        travel_window.destroy()
        root.deiconify()

    def travel_plan():
        ori=o_entry.get()
        end=e_entry.get()
        travel_m=t_m.Travel_module()
        advice=travel_m.get_travel_advice(ori,end)
        ad_label=ttk.Label(travel_window,font=("Arial", 14),text="\n".join(advice))
        ad_label.place(relx=0.3,rely=0.6)

    root.withdraw()
    travel_window = tk.Toplevel(root)
    travel_window.title("Travel")
    travel_window.geometry("500x500")
    travel_window.resizable(0,0)

    travel_label=ttk.Label(travel_window,text="旅行",font=("Arial", 14))
    travel_label.place(relx=0.45,rely=0.2)
    o_label=ttk.Label(travel_window,text="起点:",font=("Arial", 14))
    o_label.place(relx=0.3,rely=0.3)
    o_entry=ttk.Entry(travel_window,width=10, font=("Arial", 14),   justify="center")
    o_entry.place(relx=0.5,rely=0.3)
    e_label=ttk.Label(travel_window,text="终点:",font=("Arial", 14))
    e_label.place(relx=0.3,rely=0.4)
    e_entry=ttk.Entry(travel_window,width=10, font=("Arial", 14),   justify="center")
    e_entry.place(relx=0.5,rely=0.4)
    c_button=ttk.Button(travel_window,text="确认",command=travel_plan)
    c_button.place(relx=0.45,rely=0.5)

    back_button=ttk.Button(travel_window,text="back", command=back)
    back_button.place(relx=0.0,rely=0.0)

root = tk.Tk()
root.title("Weather App")
root.geometry("550x500")
usr=u_m.User_module()
root.resizable(0,0)

ENABLE_ALERT=False

initial_image = Image.open("background.jpg").resize((550, 500))
initial_photo = ImageTk.PhotoImage(initial_image)

# 创建 Canvas 显示背景图片
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

# 将背景图片添加到 Canvas
bg_image_item = canvas.create_image(0, 0, image=initial_photo, anchor="nw")
canvas.image = initial_photo
cus=c_m.Customization_module(usr)
process_log_in(usr,root)
switch_color = tk.BooleanVar(value=False)
style = ttk.Style()
print(cus.get_color())
style.configure("TButton",  foreground=cus.get_color(), font=("Arial", 12))
style.configure("TLabel",  foreground=cus.get_color(), font=("Arial", 12))
style.configure("TEntry",  foreground=cus.get_color(), font=("Arial", 12))
city_label = ttk.Label(root, text="City:", font=("Arial", 16))
city_label.place(relx=0.5, rely=0.0)

city_button = ttk.Button(root,text="enter the city", command=change_city)
city_button.place(relx=0.6, rely=0.0)

city_entry = ttk.Entry(root,width=10, font=("Arial", 14),    justify="center")
city_entry.place_forget()

confirm_button = ttk.Button(root, text=chr(8730), command=yes)
confirm_button.place_forget()

user_button = ttk.Button(root,text="User", command=user_widget)
user_button.place(relx=0.72, rely=0.1)

weather_label = ttk.Label(root, text="", font=("Arial", 16))
weather_label.place(relx=0.0, rely=0.0)

forecast_frame = ttk.Frame(root)
forecast_frame.place(relx=0.0, rely=0.2)

travel_button=ttk.Button(root,text="Go Travel", command=travel)
travel_button.place(relx=0.5,rely=0.1)
root.mainloop()
