#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x
from hackeriet.mqtt import MQTT

def main():
    mqtt = MQTT() 
    mode = GPIO.BCM
    with SHT1x(12, 8, vdd="5V") as sensor_one:
        temp = sensor_one.read_temperature()
        humidity = sensor_one.read_humidity(temp)
        sensor_one.calculate_dew_point(temp, humidity)
        print(sensor_one)
        mqtt("hackeriet/japonica/temperature", temp)
        mqtt("hackeriet/japonica/humidity", humidity)
        f = open("japonica", "w")
        f.write("%s," % str(temp))
        f.write("%s\n" % str(humidity))
        f.close()
        sleep(2)

    with SHT1x(18, 16, vdd="5V") as sensor_two:
        temp = sensor_two.read_temperature()
        humidity = sensor_two.read_humidity(temp)
        sensor_two.calculate_dew_point(temp, humidity)
        mqtt("hackeriet/elefantfot/temperature", temp)
        mqtt("hackeriet/elefantfot/humidity", humidity)
        f = open("elephantfot", "w")
        f.write("%s," % str(temp))
        f.write("%s\n" % str(humidity))
        print(sensor_two)
        sleep(2)

if __name__ == "__main__":
    main()
