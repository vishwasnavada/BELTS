from __future__ import division

import sys

from bluepy.btle import *

import struct

import thread

from time import sleep








def vReadSENSE():

	scanner = Scanner(0)

	devices = scanner.scan(3)

	ble_service = []

	char_sensor = 0

	non_sensor = 0

	bat_char = Characteristic

	temperature_char = Characteristic

	humidity_char = Characteristic

        hall_char = Characteristic

	count = 15

    

	for i in range(3):

		try:

			devices[i].getScanData()

			ble_service.append(Peripheral())

			ble_service[char_sensor].connect("08:6B:D7:FE:11:C9","public")

			char_sensor = char_sensor + 1

			print "Connected %s device with addr %s " % (char_sensor, "08:6B:D7:FE:11:C9")

		except:

			non_sensor = non_sensor + 1

	try:

		for i in range(char_sensor):

			

			services = ble_service[i].getServices()

			characteristics = ble_service[i].getCharacteristics()

			for k in characteristics:

				print k

				if k.uuid=="2a19":

					print "Battery Level"

					bat_char = k

				if k.uuid == "2a6e":

					print "Temperature"

					temperature_char = k

				if k.uuid == "2a6f":

					print "Humidity"

					humidity_char = k

			    if k.uuid == "f598dbc5-2f01-4ec5-9936-b3d1aa4f957f":
                                        
					hall_char = k
				if k.uuid == "d24c4f4e-17a7-4548-852c-abf51127368b":
					lux_char = k

	except:

		return None

	while True:

		bat_data = bat_char.read()

		bat_data_value = ord(bat_data[0])

		

		temperature_data = temperature_char.read()

		temperature_data_value =(ord(temperature_data[1])<<8)+ord(temperature_data[0])

		float_temperature_data_value = (temperature_data_value / 100)

		

		humidity_data = humidity_char.read()

		humidity_data_value= ((ord(humidity_data[1]) <<8)+ord(humidity_data[0]))/100

 		hall_state = hall_char.read()

                hall_state_value = ord(hall_state[0])
                lux_state = lux_char.read()
                lux_state_value = ord(lux_state[0]
              
                f = "Battery_Level=%s Temperature=%s  Humidity=%s Hall_state=%s" % (bat_data_value, float_temperature_data_value, humidity_data_value, hall_state_value)
		print f

		count = 0
		count = count + 1 
		sleep(1)



while True:

	vReadSENSE()

