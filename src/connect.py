from djitellopy import Tello

tello = Tello()

ssid = "TP-LINK_3343"
password = "29753277"

tello.connect_to_wifi(ssid, password)
