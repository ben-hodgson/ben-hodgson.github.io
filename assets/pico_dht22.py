import machine
from machine import Pin
from picozero import pico_led, LED
from time import sleep
import network
import socket
import dht

ssid = 'VM317723-2G'
password = 'sbnrsgtc'

def connect():
    #connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
    
def open_socket(ip):
    # open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(temp, hum):
    html = """<html>
              <head>
              <meta http-equiv="refresh" content="5">
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <link rel="icon" href="data:,">
              <style>
              body { text-align: center; font-family: "Helvetica", Arial;}
              table { border-collapse: collapse; width:55%; margin-left:auto; margin-right:auto; }
              th { padding: 12px; background-color: #87034F; color: white; }
              tr { border: 2px solid #000556; padding: 12px; }
              tr:hover { background-color: #bcbcbc; }
              td { border: none; padding: 14px; }
              .sensor { color:DarkBlue; font-weight: bold; background-color: #ffffff; padding: 1px;  
              </style>
              </head>
              <body>
              <h1>BME280 Pi Pico W Weather Station</h1>
              <table><tr><th>Parameters</th><th>Value</th></tr>
              <tr><td>Temperature</td><td><span class="sensor">""" + "{}C".format(temp) + """</span></td></tr>
              <tr><td>Pressure</td><td><span class="sensor"> Pressure </span></td></tr>
              <tr><td>Humidity</td><td><span class="sensor">""" + "{:.02f}%".format(hum) + """</span></td></tr> 
              </html>"""
    return html

def serve(connection):
    led = LED(13)
    sensor = dht.DHT22(Pin(2))   
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request == '/lightoff?':
            pico_led.off()
            state = 'OFF'
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        pico_led.on()
        led.on()
        sleep(0.5)
        pico_led.off()
        led.off()
        sleep(0.5)
        html = webpage(temp, hum)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
