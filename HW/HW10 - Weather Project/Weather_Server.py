import socket
import requests
from datetime import datetime

ip = '127.0.0.1'
port = 5230

def get_city_weather(city_name: str):
    api_key="3475c4ebec10d30dbfde6b5e54ade090"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    Response = requests.get(url)
    data=Response.json()

    if data["cod"]=='404':
        return "Invalid City Name"
    else:
        temperature=data["main"]["temp"] - 273.15
        feels_like=data["main"]["feels_like"] - 273.15
        weather_desc=data["weather"][0]["description"] # توی کلید آب و هوا یه لیست هست که صفرمین مقدارشو که یه دیکشنریه برمیداریم و ازش توضیحات رو میگیریم
        
        client_time = datetime.now()
        last_update = client_time.strftime("%Y-%m-%d %H:%M:%S")
        
        return "{} Weather:\n**Temperature: {}°C\n**Feels Like: {}°C\n**Description: {}\n**Last Updated: {}".format(city_name,round(temperature,2),round(feels_like,2),weather_desc,last_update)

def start_server():
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ساختن شی از سوکت

    tcpSocket.bind((ip , port)) # شی‌ء مون رو قابل دسترس میکنیم با این متد

    tcpSocket.listen(5) # سوکت رو در حالت شنود قرار میدیم تا بتونه درخواست اتصال کلاینت رو متوجه بشه
    # عدد 5 تعداد درخواست همزمان اتصال کلاینت‌هاست
    print("Server started...")
    # برای برقرار بودن سرور تا بی نهایت
    while True:
        client, addr = tcpSocket.accept()  # با این متد سرور خود را منتظر اتصال یک کلاینت میکنیم
        # client, (ip, port) = tcpSocket.accept()
        print("Received connection from", addr)
        
        city_data=client.recv(1024).decode('utf-8') # دریافت اطلاعات از کلاینت توسط سرور
        # از دیکود استفاده کردیم تا کدی که دریافت میکنیم رو به یک استرینگ قابل قبول تبدیل کنه برای ارسال به تابع
        weather = get_city_weather(city_data)

        client.send(weather.encode('utf-8')) # ارسال پیغام به کلاینت متصل شده بصورت بایت، چون متد سند قابلیت ارسال رشته ندارد
        # برای تبدیل شدن به کد اصلی
        client.close()



start_server()