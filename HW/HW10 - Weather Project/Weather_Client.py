import socket
from datetime import datetime

ip = "127.0.0.1"
port = 5230
    
def start_client(city):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((ip , port)) # با این متد به سرور ساخته شده متصلش میکنیم
    client.send(city.encode("utf-8"))
    
    client_data = client.recv(1024).decode("utf-8")  # اندازه ی پیام دریافت شده
    return client_data

while True:
    user_city = input("Enter a city name: ")
    
    result= start_client(user_city)
    
    if user_city == 'exit':
        break
    
    if result =="Invalid City Name":
        print("Invalid City Name")
        
    else:
        print(result)
        


