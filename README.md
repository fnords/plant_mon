# plant monitoring
soil humidity monitoring for hackerplants

## Requirements
* PLANTS
* SHT-10 sensors
* 1 stk Raspberry Pi
* a breadboard and some wires

## Wiring the Pi

Wire | Pin #
-----|------
red (VDD) | 02 (5V)
green (GND) | 06 (GND
yellow (SCK) | 08 (GPIO14) and 16 (GPIO23)
blue (DATA) | 12 (GPIO18) and 18 (GPIO24)

Add a 10k resistor between VDD and DATA for each sensor
