from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()
tello.move_up(150)
tello.move_down(80)
tello.move_up(50)
tello.move_down(80)
tello.move_up(50)
tello.land()