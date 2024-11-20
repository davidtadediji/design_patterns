from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def power(self):
        pass


class TV(Device):
    def power(self):
        print("TV power toggled!")

class Radio(Device):
    def power(self):
        print("Radio power toggled!")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        self.device.power()


tv = TV()
radio = Radio()

remote_control = RemoteControl(tv)
remote_control.toggle_power()


remote_control = RemoteControl(radio)
remote_control.toggle_power()