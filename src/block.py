from djitellopy import Tello

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        tello = Tello()

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        tello.connect()
        tello.takeoff()
        tello.move_up(150)
        tello.move_down(80)
        tello.move_up(50)
        tello.move_down(80)
        tello.move_up(50)
        tello.land()
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
